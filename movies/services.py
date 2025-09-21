import requests
from django.conf import settings


BASE_URL = "https://api.themoviedb.org/3"

def get_popular_movies():
    url = f"{BASE_URL}/movie/popular"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "ja-JP",
        "page": 1
    }
    res = requests.get(url, params=params)
    return res.json().get("results", [])