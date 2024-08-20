from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        api_key = os.getenv('API_KEY')  # Get the API key from environment variables
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
        response = requests.get(complete_url)
        data = response.json()

        if data['cod'] == 200:
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
        else:
            weather_data = None
        return render_template('index.html', weather=weather_data)
    return render_template('index.html', weather=None)

if __name__ == '__main__':
    app.run(debug=True)
