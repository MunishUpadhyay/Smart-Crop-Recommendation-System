# 🌱 Smart Crop Recommendation System

A machine learning-powered web application that provides intelligent crop recommendations based on soil properties, weather conditions, and geographical location. Built with Streamlit and Python, this system helps farmers make data-driven decisions for optimal crop selection.

## 🎯 Features

- **🌍 Location-Based Recommendations**: Select your state and city for localized predictions.
- **🌤️ Real-Time Weather Integration**: Fetches current weather conditions including temperature, humidity, pressure, and wind speed.
- **🧪 Soil Analysis**: Input soil properties including NPK values, pH levels, and rainfall data.
- **📊 Interactive Visualizations**:
  - Overview of soil and weather conditions
  - Top-5 crop probability rankings
  - Data visualization charts
- **🔮 AI-Powered Predictions**: Machine learning model trained on agricultural data.
- **📱 Responsive Design**: Clean, modern UI with enhanced user experience.

## 🏗️ Project Structure

```
CROP_PREDICTION_PROJECT/
├── .vscode/                    # VS Code configuration
├── data/                       # Dataset files
│   ├── Crop_Recommendation.csv
│   └── Indian_cities_coordinates.csv
├── notebooks/                  # Jupyter notebooks
│   └── train_model.ipynb
├── saved_models/              # Trained ML models
│   └── crop_model.pkl
├── src/                       # Source code modules
│   ├── __pycache__/
│   ├── __init__.py
│   ├── data_loader.py         # Data loading utilities
│   ├── location_mapper.py     # Location mapping functions
│   ├── predictor.py           # ML prediction logic
│   └── weather_api.py         # Weather API integration
├── streamlit_app/             # Streamlit application
│   ├── __init__.py
│   └── app.py                 # Main Streamlit app
├── .env                       # Environment variables
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Internet connection (for weather API)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MunishUpadhyay/crop-recommendation-system.git
   cd crop-recommendation-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file and add your weather API key
   echo "WEATHER_API_KEY=your_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   streamlit run streamlit_app/app.py
   ```

## 🎮 Usage

### 1. Location Selection
- Choose your **State** from the dropdown menu
- Select your **City** to get localized recommendations
- Available locations include major Indian states and cities

### 2. Weather Conditions
The system automatically fetches current weather data including:
- 🌡️ **Temperature** (°C)
- 💧 **Humidity** (%)
- 📊 **Pressure** (hPa)
- 💨 **Wind Speed** (m/s)
- 🌫️ **Weather Description**

### 3. Soil Properties Input
Use the interactive sliders to input your soil parameters:

| Parameter | Range | Description |
|-----------|-------|-------------|
| **Nitrogen (N)** | 0-100 ppm | Nitrogen content in soil |
| **Phosphorus (P)** | 0-100 ppm | Phosphorus content in soil |
| **Potassium (K)** | 0-100 ppm | Potassium content in soil |
| **Soil pH** | 0-14 | Soil acidity/alkalinity level |
| **Rainfall** | 0-500 mm | Annual rainfall in millimeters |

### 4. Get Recommendations
- Click **"🔮 Predict Best Crop"** button
- View the recommended crop with probability score
- Analyze the top-5 crop alternatives
- Review the data visualization charts

## 📊 Sample Results

The system provides comprehensive analysis including:

- **Primary Recommendation**: e.g., "RICE" with detailed explanation
- **Alternative Crops**: Ranked list with probability scores
- **Visual Analytics**:
  - Bar charts showing soil and weather parameter overview
  - Probability distribution of top 5 crops
- **Data Summary**: Complete input parameter visualization

## 🧠 Machine Learning Model

### Model Details
- **Algorithm**: [Random Forest Classifier]
- **Training Data**: Agricultural dataset with soil, weather, and crop yield information
- **Features**: 7 input parameters (N, P, K, pH, Temperature, Humidity, Rainfall)
- **Output**: Multi-class crop classification

### Model Performance
- **Accuracy**: [0.9931818181818182]
- **Validation Method**: [e.g., Cross-validation, Train-Test split]
- **Supported Crops**: Rice, Wheat, Maize, Banana, Papaya, Coconut, Coffee, and many more

## 🛠️ Technologies Used

### Backend
- **Python 3.8+**: Core programming language
- **Scikit-learn**: Machine learning framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing

### Frontend
- **Streamlit**: Web application framework
- **Plotly**: Interactive data visualizations
- **CSS3**: Custom styling and responsive design

### APIs & External Services
- **Weather API**: Real-time weather data integration
- **Geolocation Services**: Location-based recommendations

## 📁 Key Files Description

| File | Description |
|------|-------------|
| `streamlit_app/app.py` | Main Streamlit application with UI components |
| `src/predictor.py` | Machine learning prediction logic |
| `src/weather_api.py` | Weather API integration and data fetching |
| `src/data_loader.py` | Data loading and preprocessing utilities |
| `src/location_mapper.py` | Geographic location mapping functions |
| `data/Crop_Recommendation.csv` | Training dataset for ML model |
| `saved_models/crop_model.pkl` | Trained machine learning model |

## 🎨 UI Features

- **Modern Design**: Clean, professional interface with gradient backgrounds
- **Interactive Elements**: Hover effects, smooth transitions, and animations
- **Responsive Layout**: Mobile-friendly design that works on all devices
- **Data Visualization**: Interactive charts and graphs using Plotly
- **Real-time Updates**: Dynamic content updates based on user input

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Future Enhancements

- [ ] **Mobile App**: Native mobile application
- [ ] **More Crops**: Expand database to include more crop varieties
- [ ] **Market Prices**: Integration with commodity price APIs
- [ ] **Seasonal Analysis**: Time-based crop recommendations
- [ ] **Satellite Data**: Integration with satellite imagery for soil analysis
- [ ] **Multi-language Support**: Support for regional languages
- [ ] **Offline Mode**: Local predictions without internet connectivity

## 🐛 Known Issues

- Weather API rate limits may affect real-time data fetching
- Limited to Indian geographical locations currently
- Requires internet connection for weather data

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

- **Munish Upadhyay** - *Initial work* - [YourGitHub](https://github.com/MunishUpadhyay)

## 🙏 Acknowledgments

- Agricultural research data providers
- Weather API service providers
- Open-source community contributors
- Farmers and agricultural experts for domain knowledge

## 📞 Support

For support, email munishupadhyay183@gmail.com or create an issue in the GitHub repository.

---

**Made with ❤️ for sustainable agriculture and smart farming practices**

🌾 *Helping farmers make data-driven decisions for better crop yields* 🌾