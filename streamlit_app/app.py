import streamlit as st
import sys
import os
import pandas as pd
import plotly.express as px

# Adjust the path to import from the 'src' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import custom modules
from src import data_loader, predictor, location_mapper, weather_api

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="🌾 Smart Crop Recommendation App",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🌱"
)

# --- Custom CSS for Enhanced Aesthetics and Color Scheme ---
st.markdown(
    """
    <style>
    /* Color Palette Variables (Optional, for easy modification) */
    :root {
        --primary-bg: #0B0404; /* Very dark grey */
        --secondary-bg: #1A1A1D; /* Slightly lighter dark grey for elements */
        --text-color: #E0E0E0; /* Off-white for general text */
        --header-color: #00cc96; /* Vibrant green for main titles/accents */
        --accent-blue: #287F83; /* Pearl blue for selectboxes */
        --button-hover: #00996b; /* Darker green for button hover */
        --border-color: #1A1A1D; /* Subtle dark border/grid lines */
        --info-bg: #213c42; /* Dark teal for info boxes */
        --info-text: #afeeee; /* Light cyan for info text */
    }

    body {
        background-color: var(--primary-bg);
        color: var(--text-color);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Titles and Headers */
    h1 {
        color: var(--header-color);
        font-weight: bold;
        font-size: 2.2em; /* Adjusted H1 font size */
    }
    h2, h3, h4, h5, h6 {
        color: var(--header-color);
        font-weight: bold;
    }

    /* Main App Title - Tagline Styling */
    h4[style*="margin-top:-20px"] { /* Targeting the specific tagline h4 */
        color: #888;
        font-weight: normal;
        font-size: 1em;
    }

    /* Streamlit widgets styling */
    .stSelectbox > div > div > div {
        background-color: var(--accent-blue);
        color: white; /* Text inside selectbox */
        border: 1px solid var(--border-color);
        border-radius: 0.5rem;
    }
    .stSlider > div > div {
        background-color: var(--secondary-bg);
        border: 1px solid var(--border-color);
        border-radius: 0.5rem;
    }
    .stSlider .stThumb {
        background-color: var(--header-color);
    }
    .stButton > button {
        background-color: var(--header-color);
        color: white;
        font-weight: bold;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        border: none;
        transition: all 0.2s ease-in-out;
    }
    .stButton > button:hover {
        background-color: var(--button-hover);
        transform: translateY(-2px);
    }

    /* Success, Info, Warning, Error Messages */
    .stAlert div[data-baseweb="alert"] {
        border-radius: 0.5rem;
        padding: 1rem;
    }
    .stAlert [data-testid="stMarkdownContainer"] p {
        font-size: 1.1em;
    }
    .stAlert.streamlit-success {
        background-color: #1a472a;
        color: #e6ffe6;
    }
    .stAlert.streamlit-error {
        background-color: #4a1f1f;
        color: #ffe6e6;
    }
    .stAlert.streamlit-warning {
        background-color: #4a3e1f;
        color: #fffbe6;
    }
    .stAlert.streamlit-info {
        background-color: var(--info-bg);
        color: var(--info-text);
    }

    /* Plotly chart container padding */
    .stPlotlyChart {
        padding: 1rem 0;
    }

    /* Sidebar styling */
    .css-1d391kg { /* This class might change with Streamlit updates */
        background-color: var(--secondary-bg);
    }

    /* --- Metric Component Styling (WITH !important flags) --- */
    div[data-testid="stMetric"] {
        background-color: var(--secondary-bg) !important;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid var(--border-color);
        margin-bottom: 1rem;
    }
    div[data-testid="stMetric"] label {
        color: var(--text-color) !important;
        font-size: 0.9em;
        font-weight: normal;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: var(--header-color) !important;
        font-size: 1.8em;
        font-weight: bold;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
        color: var(--text-color) !important;
    }

    /* Adjust padding for columns slightly */
    /* This class might change in future Streamlit updates */
    .st-emotion-cache-1iy415c {
        padding-top: 0rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --- Main Application Title ---
st.title("🌱 Smart Crop Recommendation System")
st.markdown("<h4 style='color: #888; margin-top: -20px; font-weight: normal;'>Your partner for optimal farming decisions.</h4>", unsafe_allow_html=True)
st.markdown("---")

# --- Data Loading ---
@st.cache_data # Cache data loading for performance
def load_all_data():
    """Loads all necessary data for the application."""
    # Corrected path for location data: assuming 'data' is one level up from 'streamlit_app'
    location_df_loaded = data_loader.load_location_data(path='data/Indian_cities_coordinates.csv')

    # Load the crop prediction model (as per your predictor.py)
    crop_model_loaded = predictor.load_model()

    # Get the state-city mapping using the function from location_mapper, passing the DataFrame
    state_city_map_loaded = location_mapper.get_state_city_mapping(location_df_loaded)

    return location_df_loaded, crop_model_loaded, state_city_map_loaded

location_df, crop_model, state_city_map = load_all_data()

# --- User Input: Location Selection ---
st.subheader("📍 Select Your Location")
col1, col2 = st.columns(2)
with col1:
    state = st.selectbox("State", list(state_city_map.keys()), help="Select the Indian state where your farm is located.")
with col2:
    city = st.selectbox("City", state_city_map[state], help="Select the city within the chosen state.")

# --- Get and Display Weather Data ---
lat, lon = location_mapper.get_lat_lon(location_df, city)

# Initialize weather variables with default values in case data fetching fails
temperature = 25.0
humidity = 70.0
pressure = "N/A"
wind_speed = "N/A"
description = "N/A"

if lat is not None:
    weather_data = weather_api.get_weather(lat, lon)

    if weather_data is not None: # Check if a dictionary was returned successfully
        # Extract data using .get() with a default value to prevent KeyError if a field is missing
        temperature = weather_data.get("temperature", 25.0)
        humidity = weather_data.get("humidity", 70.0)
        pressure = weather_data.get("pressure", "N/A")
        wind_speed = weather_data.get("wind_speed", "N/A")
        description = weather_data.get("description", "N/A").capitalize() # Capitalize for nice display

        st.success(f"**Current Weather in {city}:**")

        # Create two columns for the main layout
        col1, col2 = st.columns(2)

        with col1:
            # First row in the first main column: Temperature and Humidity
            st.subheader("Current Conditions") # Optional: Add a subheader for clarity
            temp_hum_col1, temp_hum_col2 = st.columns(2)
            with temp_hum_col1:
                st.metric("Temperature", f"{temperature:.1f}°C")
            with temp_hum_col2:
                st.metric("Humidity", f"{humidity:.1f}%")

            # Second row in the first main column: Pressure and Wind Speed
            press_wind_col1, press_wind_col2 = st.columns(2)
            with press_wind_col1:
                st.metric("Pressure", f"{pressure} hPa")
            with press_wind_col2:
                st.metric("Wind Speed", f"{wind_speed} m/s")

        with col2:
            # Description in the second main column
            st.subheader("Weather Details") # Optional: Add a subheader for clarity
            st.metric("Description", description)


    else:
        st.warning("⚠️ Could not fetch live weather data. Using default values for prediction.")
        # temperature and humidity already initialized with defaults
else:
    st.error("❌ Unable to retrieve coordinates for the selected city. Please check the city name or data.")
    # temperature and humidity already initialized with defaults

st.markdown("---")

# --- User Input: Soil Details ---
st.subheader("🧪 Enter Soil Properties")
st.markdown("Move the sliders to input your soil's nutritional and environmental parameters.")

colN, colP, colK = st.columns(3)
with colN:
    N = st.slider("Nitrogen (N) - ppm", 0, 140, 60, help="Nitrogen content in parts per million (ppm).")
with colP:
    P = st.slider("Phosphorus (P) - ppm", 5, 145, 60, help="Phosphorus content in parts per million (ppm).")
with colK:
    K = st.slider("Potassium (K) - ppm", 5, 205, 60, help="Potassium content in parts per million (ppm).")

colph, colrain = st.columns(2)
with colph:
    ph = st.slider("Soil pH", 3.5, 10.0, 6.5, 0.1, help="Soil pH value (acidity/alkalinity).")
with colrain:
    rainfall = st.slider("Rainfall (mm)", 20, 300, 100, help="Average annual rainfall in millimeters (mm).")

st.markdown("---")

# --- Feature Bar Chart (Input Summary) ---
st.subheader("📊 Your Input Summary")
st.info("This chart visualizes the values you've entered for crop recommendation, along with fetched weather data.")

features_dict = {
    "Nitrogen (N)": N,
    "Phosphorus (P)": P,
    "Potassium (K)": K,
    "Temperature (°C)": temperature, # Uses fetched or default temp
    "Humidity (%)": humidity,       # Uses fetched or default humidity
    "Pressure (hPa)": pressure if isinstance(pressure, (int, float)) else 0, # Convert N/A to 0 for plotting
    "Wind Speed (m/s)": wind_speed if isinstance(wind_speed, (int, float)) else 0, # Convert N/A to 0 for plotting
    "pH": ph,
    "Rainfall (mm)": rainfall
}

# Create a DataFrame for Plotly Express
features_df = pd.DataFrame(features_dict.items(), columns=['Feature', 'Value'])

fig_input_summary = px.bar(
    features_df,
    x='Feature',
    y='Value',
    labels={'Value': 'Input Value'},
    title="Overview of Entered Soil and Weather Conditions",
    color='Feature', # Color bars by feature
    color_discrete_sequence=px.colors.sequential.Aggrnyl, # A nice green color sequence
    template="plotly_dark" # Use dark theme for the plot
)
# Customize layout for better appearance
fig_input_summary.update_layout(
    xaxis_title_text='Environmental Factor',
    yaxis_title_text='Measured Value',
    hovermode="x unified", # Shows all values on hover
    font=dict(color="white"), # White font for text in plot
    title_font_size=20,
    plot_bgcolor='rgba(0,0,0,0)', # Transparent plot background
    paper_bgcolor='rgba(0,0,0,0)', # Transparent paper background
    xaxis=dict(showgrid=False), # Hide x-axis grid
    yaxis=dict(gridcolor='#31333F') # Lighter grid lines for y-axis
)
st.plotly_chart(fig_input_summary, use_container_width=True)

st.markdown("---")

# --- Predict Crop Button and Results ---
if st.button("🌾 **Predict Best Crop**", help="Click to get the recommended crop based on your inputs."):
    if temperature is not None and humidity is not None:
        # Ensure the order of features matches the model's training order
        # Your model still expects only 7 features: N, P, K, temperature, humidity, ph, rainfall
        features = [N, P, K, temperature, humidity, ph, rainfall]

        # Make prediction
        crop = predictor.predict_crop(crop_model, features)
        st.success(f"### 🎉 Recommended Crop: **`{crop.upper()}`**")
        st.balloons() # Add a celebratory animation

        # Optional: Probability Chart (if model supports predict_proba)
        if hasattr(crop_model, "predict_proba"):
            probas = crop_model.predict_proba([features])[0]
            labels = crop_model.classes_

            # Get top 5 probabilities and sort them
            top_indices = probas.argsort()[::-1][:5] # Get indices of top 5 in descending order
            top5_probs = [(labels[i], probas[i]) for i in top_indices]

            top5_df = pd.DataFrame(top5_probs, columns=["Crop", "Probability"])

            st.subheader("🔍 Top-5 Crop Probabilities")
            st.info("This chart shows the likelihood of various crops being suitable.")

            prob_fig = px.bar(
                top5_df,
                x="Crop",
                y="Probability",
                text=top5_df["Probability"].apply(lambda x: f"{x:.2%}"), # Format as percentage
                title="Top 5 Crop Recommendations by Probability",
                color="Probability", # Color based on probability
                color_continuous_scale=px.colors.sequential.Greens, # Green scale for probabilities
                template="plotly_dark"
            )
            prob_fig.update_layout(
                xaxis_title_text='Crop Type',
                yaxis_title_text='Probability',
                hovermode="x unified",
                font=dict(color="white"),
                title_font_size=20,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(showgrid=False),
                yaxis=dict(gridcolor='#31333F'),
                bargap=0.4 # Space between bars
            )
            # Update text position for better visibility
            prob_fig.update_traces(textposition='outside')

            st.plotly_chart(prob_fig, use_container_width=True)
    else:
        st.warning("Prediction cannot be made as crucial weather data (Temperature/Humidity) is missing or could not be fetched.")

st.markdown("---")
st.markdown("Developed with 💚 for Farmers")