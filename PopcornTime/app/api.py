import requests
from app.config import TMDB_API_KEY
import streamlit as st

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

@st.cache_data(show_spinner=False)
def search_movie(query):
    url = f"{BASE_URL}/search/multi"
    params = {"api_key": TMDB_API_KEY, "query": query}
    response = requests.get(url, params=params)
    return response.json().get("results", [])

@st.cache_data(show_spinner=False)
def get_movie_details(movie_id, media_type='movie'):
    url = f"{BASE_URL}/{media_type}/{movie_id}"
    params = {"api_key": TMDB_API_KEY}
    response = requests.get(url, params=params)
    return response.json()

@st.cache_data(show_spinner=False)
def get_movies_by_filter(genre=None, year=None, rating=None, sort_by="popularity.desc"):
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "sort_by": sort_by,
        "with_genres": genre,
        "primary_release_year": year,
        "vote_average.gte": rating or 0
    }
    response = requests.get(url, params=params)
    return response.json().get("results", [])

def get_poster_url(path):
    return IMAGE_BASE + path if path else "https://via.placeholder.com/500x750?text=No+Image"
