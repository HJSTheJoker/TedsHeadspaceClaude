from flask import Flask, render_template, request, jsonify
import requests
from decouple import config
from datetime import datetime, timedelta

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
    api_key = config('NEWS_API_KEY', default='6fbde6c1143444cfaff56a5588e17108')
    categories = ['sports', 'technology']
    all_articles = []

    for category in categories:
        news_url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}'
        response = requests.get(news_url)
        category_articles = response.json().get('articles', [])
        all_articles.extend(category_articles)

    # Fetch additional AI-related news
    ai_news_url = f'https://newsapi.org/v2/everything?q=artificial+intelligence&sortBy=publishedAt&apiKey={api_key}'
    ai_response = requests.get(ai_news_url)
    ai_articles = ai_response.json().get('articles', [])
    all_articles.extend(ai_articles)

    # Filter and sort articles
    reputable_sources = ['BBC News', 'CNN', 'The New York Times', 'Reuters', 'Associated Press', 'The Guardian', 'The Washington Post', 'NBC News', 'ABC News', 'CBS News', 'Time', 'TechCrunch', 'Wired', 'The Verge', 'Engadget', 'Ars Technica']
    
    filtered_articles = [
        article for article in all_articles 
        if article['source']['name'] in reputable_sources 
        and article.get('urlToImage') 
        and article.get('description')
    ]

    # Sort by publishedAt date
    sorted_articles = sorted(filtered_articles, key=lambda x: datetime.strptime(x['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"), reverse=True)

    # Limit to 20 most recent articles
    return jsonify(sorted_articles[:20])

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
