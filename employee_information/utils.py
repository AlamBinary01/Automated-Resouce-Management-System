# utils.py
import requests

def fetch_educational_news():
    url = f'https://newsapi.org/v2/everything?q=tesla&from=2024-07-03&sortBy=publishedAt&apiKey=20f3bdc4678c40e08ae6c8081b071eb1'
    response = requests.get(url)
    data = response.json()
    return data.get('articles', [])


