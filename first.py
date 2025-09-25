import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Replace this with your OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'
CITY = 'London'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch data
response = requests.get(URL)
data = response.json()

# Extract relevant data
weather_list = data['list']
weather_data = []

for entry in weather_list:
    dt = datetime.fromtimestamp(entry['dt'])
    temp = entry['main']['temp']
    humidity = entry['main']['humidity']
    weather_data.append({'datetime': dt, 'temperature': temp, 'humidity': humidity})

# Convert to DataFrame
df = pd.DataFrame(weather_data)

# Save CSV (optional)
df.to_csv(f'{CITY}_weather.csv', index=False)
print(df.head())
