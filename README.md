# 🏆 Elite CDM 2022 Performance Dashboard

An advanced football analytics dashboard for the **2022 FIFA World Cup**, powered by **StatsBomb** data. 

This application provides in-depth tactical analysis, player performance metrics, and passing networks with a premium user interface.

## 🚀 Live Demo
https://cdm2022-dashboard.streamlit.app

## ✨ Key Features
- **Elite UI/UX**: Custom dark-themed interface built with a professional design system.
- **Team Analytics**: Performance progression in the final third, methods of entry (passes vs carries), and spatial intensity heatmaps.
- **Player Geometry**: Detailed passing maps (successful vs incomplete) and individual density charts.
- **Tactical Networks**: Visualizing team passing structures before substitutions.
- **Data Optimization**: Fast loading using Parquet format and memory-efficient data processing.

## 🛠️ Technology Stack
- **Framework**: [Streamlit](https://streamlit.io/)
- **Data Source**: [StatsBomb Free Data](https://github.com/statsbomb/open-data)
- **Visualizations**: `mplsoccer`, `matplotlib`, `seaborn`
- **Data Processing**: `pandas`, `pyarrow`

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd CDM2022
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Extract fresh data**:
   If the data folder is empty or needs updating:
   ```bash
   python data_extractor.py
   ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

---
*Created with ❤️ for football fans and analysts.*
