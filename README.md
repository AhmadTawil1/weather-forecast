# Weather Forecast App

A Streamlit-based web application that provides weather forecasts for any location worldwide. The app displays temperature trends and sky conditions for up to 5 days in advance.

## Features

- Real-time weather data from OpenWeatherMap API
- Temperature visualization using Plotly
- Sky condition display with custom icons
- User-friendly interface with location search
- Forecast period selection (1-5 days)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AhmadTawil1/weather-forecast.git
cd weather-forecast
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Enter a location name and select the forecast period and data type (Temperature or Sky)

## Project Structure

- `main.py`: Main application file with Streamlit interface
- `backend.py`: Backend logic for fetching weather data
- `images/`: Directory containing weather condition icons
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not tracked in git)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- Ahmad Tawil
- Email: ahmadtawil.se@outlook.com
- GitHub: [AhmadTawil1](https://github.com/AhmadTawil1) 