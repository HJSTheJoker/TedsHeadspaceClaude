from flask import Flask, render_template, request, jsonify
import requests
from decouple import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/theme-park')
def theme_park():
    return render_template('theme_park.html')

@app.route('/media-downloader')
def media_downloader():
    return render_template('media_downloader.html')

@app.route('/fetch-news')
def fetch_news():
    api_key = config('NEWS_API_KEY', default='')
    news_url = f'https://newsapi.org/v2/top-headlines?category=technology&apiKey={api_key}'
    response = requests.get(news_url)
    news_data = response.json()['articles']
    return jsonify(news_data)

@app.route('/fetch-parks')
def fetch_parks():
    parks_url = 'https://queue-times.com/parks.json'
    response = requests.get(parks_url)
    return jsonify(response.json())

@app.route('/fetch-rides/<int:park_id>')
def fetch_rides(park_id):
    rides_url = f'https://queue-times.com/parks/{park_id}/queue_times.json'
    response = requests.get(rides_url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
