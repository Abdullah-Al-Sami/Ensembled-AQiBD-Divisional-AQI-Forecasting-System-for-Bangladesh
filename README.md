# 🌍 Ensembled AQIBD  
**Divisional Air Quality Forecasting System for Bangladesh**

Ensembled AQIBD is an intelligent **web-based AQI prediction system** that forecasts air quality severity for different divisions in Bangladesh. It uses **ensemble machine learning models** trained on pollutant and environmental data to provide accurate AQI category predictions, aiding environmental awareness and decision-making.


## 🚀 Project Overview
**Ensembled AQIBD** predicts the **Air Quality Index (AQI)** severity across Bangladesh’s eight divisions.  
The app processes **pollutant and environmental inputs** like SO₂, NO₂, CO, PM2.5, temperature, humidity, and solar radiation, and classifies AQI levels into categories such as *Good, Moderate, Unhealthy, Hazardous*, etc.

---

## ✨ Features
- 🌫️ Predicts AQI severity using an ensemble ML model.  
- 🌦️ Accepts pollutant & environmental parameters as input.  
- 🌍 Supports multiple divisions of Bangladesh.  
- 🧠 Integrates **MinMaxScaler** and **StandardScaler** preprocessing.  
- 💻 Flask-based interactive web app.  
- 📊 Easy-to-extend for research or deployment.

---

## 🧩 System Requirements
- **Python** 3.9+
- **Pip** package manager
- Libraries: `Flask`, `NumPy`, `Pandas`, `scikit-learn`, `pickle`
- (Optional) `virtualenv` for isolated environments

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/Ensembled-AQIBD.git
cd Ensembled-AQIBD

### 2. Create Virtual Environment (Optional)
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On macOS/Linux

### 3. Install Dependencies
pip install -r requirements.txt
