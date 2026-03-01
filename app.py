import streamlit as st
from weather_agent import get_weather

# Page configuration
st.set_page_config(
    page_title="Weather Agent",
    page_icon="bv",
    layout="centered"
)

# Title and description
st.title("Weather Agent ☁️")
st.markdown("Enter a city name to get the current weather conditions.")


api_key = "1c3678986ba05c7ca5cea5a983d317ca"

col1, col2 = st.columns([3, 1])
with col1:
    city = st.text_input("City Name", placeholder="e.g., Hyderabad")

with col2:
    # Add some vertical spacing to align the button
    st.write("")
    st.write("")
    get_weather_btn = st.button("Get Weather", type="primary")

# Logic to fetch and display weather
if get_weather_btn:
    if not city:
        st.warning("Please enter a city name.")
    else:
        with st.spinner(f"Fetching weather for {city}..."):
            try:
                result = get_weather(city=city, api_key=api_key)
                if result.startswith("Error") or "An error occurred" in result:
                    st.error(result)
                else:
                    st.success(f"Weather fetched for {city}!")
                    st.code(result, language="text")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

# Footer
st.markdown("---")
st.markdown("Powered by OpenWeatherMap")
