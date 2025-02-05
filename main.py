import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subbheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get temperature/sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [dict["main"]["temp"] - 273.15 for dict in filtered_data]
            date = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=date, y=temperature, labels={"x": "Date&Time", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        else:
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            images_paths = [images[condition] for condition in sky_condition]
            st.image(images_paths, width=115)
    except KeyError:
        st.write("That place does not exist")