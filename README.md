<div align="center">
  <img src="2022_FIFA_World_Cup.svg" alt="2022 FIFA World Cup" width="180">

  <h1>🏆 Elite CDM 2022 Performance Dashboard</h1>
  <p><b>Advanced Tactical Intelligence Platform | 2022 FIFA World Cup</b></p>

  [![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
  [![StatsBomb](https://img.shields.io/badge/StatsBomb-Open_Data-red?style=for-the-badge)](https://github.com/statsbomb/open-data)
  [![Plotly](https://img.shields.io/badge/mplsoccer-Pitch_Viz-3F4F75?style=for-the-badge)](https://mplsoccer.readthedocs.io)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
  [![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-cdm2022--dashboard.streamlit.app-success?style=for-the-badge)](https://cdm2022-dashboard.streamlit.app)

  > **A professional-grade World Cup analytics dashboard** powered by StatsBomb open data —  
  > combining tactical networks, player geometry, and spatial heatmaps  
  > into a premium football intelligence experience.

  [🚀 Live Demo](#-live-demo) • [✨ Features](#-key-features) • [🛠️ Stack](#️-technology-stack) • [📦 Installation](#-installation--setup)

</div>

---

## 🚀 Live Demo

Experience the full tactical dashboard live on Streamlit Cloud:

🔗 **[cdm2022-dashboard.streamlit.app](https://cdm2022-dashboard.streamlit.app)**

> No installation required — explore 2022 FIFA World Cup data directly in your browser.

---

## ✨ Key Features

### 🎨 Elite UI/UX
Custom dark-themed interface built with a professional broadcast-inspired design system — delivering a premium analytical experience from the first click.

### 📊 Team Analytics

| Feature | Description |
|---|---|
| 📈 **Performance Progression** | Track team advancement in the final third across matches |
| 🚪 **Methods of Entry** | Compare passes vs carries into dangerous zones |
| 🔥 **Spatial Heatmaps** | High-intensity action density mapped on a real pitch |

### 👤 Player Geometry

| Feature | Description |
|---|---|
| 🗺️ **Passing Maps** | Successful vs incomplete passes with directional vectors |
| 📍 **Density Charts** | Individual action concentration zones per player |

### 🕸️ Tactical Networks

| Feature | Description |
|---|---|
| 🔗 **Pass Networks** | Team passing structures visualized before substitutions |
| 🧠 **Connection Intensity** | Weighted links showing most frequent passing combinations |

### ⚡ Data Optimization

| Feature | Description |
|---|---|
| 🚀 **Parquet Format** | Ultra-fast data loading with columnar storage |
| 💾 **Memory Efficient** | Optimized processing pipeline for smooth performance |

---

## 🛠️ Technology Stack

| Category | Technology | Purpose |
|---|---|---|
| **Framework** | [Streamlit](https://streamlit.io/) | Web application engine |
| **Data Source** | [StatsBomb Free Data](https://github.com/statsbomb/open-data) | Match & event data |
| **Pitch Viz** | [mplsoccer](https://mplsoccer.readthedocs.io/) | Pitch rendering & pass networks |
| **Visualization** | [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/) | Charts & heatmaps |
| **Data Processing** | [Pandas](https://pandas.pydata.org/), [PyArrow](https://arrow.apache.org/) | Data manipulation & Parquet I/O |

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Step-by-step

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd CDM2022
```

**2. Create a virtual environment** *(recommended)*
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. (Optional) Extract fresh data**

> Only needed if the `data/` folder is empty or requires updating:
```bash
python data_extractor.py
```

**5. Launch the application**
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501` 🎉

---

## 📁 Project Structure
```
CDM2022/
├── app.py                  # Main Streamlit entry point
├── data_extractor.py       # StatsBomb data fetcher & Parquet builder
├── requirements.txt        # Python dependencies
├── 2022_FIFA_World_Cup.svg # Tournament logo
├── data/                   # Preprocessed Parquet data files
└── README.md               # Project documentation
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your branch: `git checkout -b feature/NewAnalysis`
3. Commit your changes: `git commit -m 'Add new tactical module'`
4. Push and open a Pull Request

---

<div align="center">

**Built with ❤️ for football fans and data analysts**

⭐ If you find this project useful, please consider giving it a star!

🔗 **[cdm2022-dashboard.streamlit.app](https://cdm2022-dashboard.streamlit.app)**

</div>
