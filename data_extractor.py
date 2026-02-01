from statsbombpy import sb
import pandas as pd
import os
import numpy as np

def extract_coords(sr):
    """Safely extract x and y from a series of location lists."""
    x = []
    y = []
    for loc in sr:
        if isinstance(loc, list) and len(loc) >= 2:
            x.append(loc[0])
            y.append(loc[1])
        else:
            x.append(np.nan)
            y.append(np.nan)
    return x, y

def extract_data():
    COMPETITION_ID = 43
    SEASON_ID = 106
    DATA_DIR = 'data'
    
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    print(f"Fetching matches for competition {COMPETITION_ID}, season {SEASON_ID}...")
    matches = sb.matches(competition_id=COMPETITION_ID, season_id=SEASON_ID)
    
    # Keep only necessary match columns
    match_cols = ['match_id', 'match_date', 'home_team', 'away_team', 'home_score', 'away_score']
    matches = matches[match_cols]
    matches.to_csv(os.path.join(DATA_DIR, 'matches.csv'), index=False)
    print(f"Saved {len(matches)} matches.")
    
    all_events = []
    match_ids = matches['match_id'].unique()
    
    # Define exact columns needed for the app logic
    # App uses: match_id, team, player, type, x, y, pass_end_x, pass_end_y, carry_end_x, carry_end_y, pass_outcome, minute, pass_recipient
    cols_interested = [
        'match_id', 'team', 'player', 'type', 'x', 'y', 
        'pass_end_x', 'pass_end_y', 'carry_end_x', 'carry_end_y', 
        'pass_outcome', 'minute', 'pass_recipient'
    ]
    
    # Filter types to only what's visualized
    types_to_keep = [
        "Pass", "Ball Receipt*", "Carry", "Clearance", "Foul Won", 
        "Block", "Ball Recovery", "Duel", "Dribble", "Interception", 
        "Miscontrol", "Shot", "Substitution"
    ]

    for i, mid in enumerate(match_ids):
        print(f"Processing match {i+1}/{len(match_ids)} (ID: {mid})...")
        try:
            events = sb.events(match_id=mid)
            
            # Extract coordinates
            if 'location' in events.columns:
                events['x'], events['y'] = extract_coords(events['location'])
            if 'pass_end_location' in events.columns:
                events['pass_end_x'], events['pass_end_y'] = extract_coords(events['pass_end_location'])
            if 'carry_end_location' in events.columns:
                events['carry_end_x'], events['carry_end_y'] = extract_coords(events['carry_end_location'])
            
            # Handle pass_outcome (fill NaNs with 'Successful' early to save space)
            if 'pass_outcome' in events.columns:
                events['pass_outcome'] = events['pass_outcome'].fillna('Successful')
            else:
                events['pass_outcome'] = 'Successful'

            # Filter rows and columns
            existing_cols = [c for c in cols_interested if c in events.columns]
            events_filtered = events[events['type'].isin(types_to_keep)][existing_cols].copy()
            
            # Optimize data types to save memory
            for col in ['match_id', 'minute']:
                if col in events_filtered.columns:
                    events_filtered[col] = pd.to_numeric(events_filtered[col], downcast='integer')
            
            float_cols = ['x', 'y', 'pass_end_x', 'pass_end_y', 'carry_end_x', 'carry_end_y']
            for col in float_cols:
                if col in events_filtered.columns:
                    events_filtered[col] = pd.to_numeric(events_filtered[col], downcast='float')

            all_events.append(events_filtered)
            
        except Exception as e:
            print(f"Error processing match {mid}: {e}")
            
    if not all_events:
        print("No events collected!")
        return

    print("Combining and final optimization...")
    df_events = pd.concat(all_events, ignore_index=True)
    
    # Save as Parquet for much better compression and faster loading on Streamlit Cloud
    # If parquet is not available, we use compressed CSV
    try:
        import pyarrow
        df_events.to_parquet(os.path.join(DATA_DIR, 'events.parquet'), index=False)
        print(f"Saved {len(df_events)} events to events.parquet")
    except ImportError:
        df_events.to_csv(os.path.join(DATA_DIR, 'events.csv.gz'), index=False, compression='gzip')
        print(f"Saved {len(df_events)} events to events.csv.gz (Parquet not available)")

if __name__ == "__main__":
    extract_data()