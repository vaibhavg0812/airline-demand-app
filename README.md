# Airline Booking Market Demand Analyzer

This is a Flask-based web app that allows users to upload airline booking CSV data and view visualizations and summaries of market demand.

## 🚀 Features
- Upload `.csv` file with fields: `Date, Origin, Destination, Passengers`
- Visualize:
  - Daily passenger trends (Line Chart)
  - Top 5 busiest routes (Bar Chart)
  - Summary table with total and average passengers

## 🛠️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/airline-demand-app.git
cd airline-demand-app
```

### 2. Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

Then visit `http://localhost:5000` in your browser.

## 🧪 Sample CSV Format
```csv
Date,Origin,Destination,Passengers
2025-01-01,DEL,BOM,120
2025-01-01,DEL,BLR,90
2025-01-02,DEL,BOM,150
```

## 📄 License
MIT License
