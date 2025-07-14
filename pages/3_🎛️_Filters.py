import streamlit as st
from app.api import get_movies_by_filter, get_poster_url

st.title("🎛️ Explore by Filters")
st.markdown("Filter top movies by genre, year, rating, and popularity.")

GENRE_OPTIONS = {
    "Action": "28",
    "Adventure": "12",
    "Animation": "16",
    "Comedy": "35",
    "Crime": "80",
    "Documentary": "99",
    "Drama": "18",
    "Fantasy": "14",
    "Mystery": "9648",
    "Science Fiction": "878"
}

genre = st.selectbox("🎭 Genre", list(GENRE_OPTIONS.keys()))
genre_id = GENRE_OPTIONS[genre]

year = st.slider("📅 Release Year", 1980, 2025, 2020)
rating = st.slider("⭐ Minimum Rating", 0.0, 10.0, 6.0)
sort_by = st.selectbox("📊 Sort By", [
    "popularity.desc", "vote_average.desc", "release_date.desc"
])

movies = get_movies_by_filter(genre=genre_id, year=year, rating=rating, sort_by=sort_by)

if movies:
    st.subheader(f"🎬 {genre} Movies")
    for i in range(0, len(movies), 6):
        cols = st.columns(6)
        for idx, movie in enumerate(movies[i:i+6]):
            with cols[idx]:
                st.image(get_poster_url(movie["poster_path"]), use_column_width=True)
                st.caption(f"{movie['title']} ({movie.get('release_date', '')[:4]})")
else:
    st.warning("No results found for these filters.")
