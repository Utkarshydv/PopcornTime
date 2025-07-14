import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process

# Sample data — replace with real or extended CSV later
movies_data = pd.DataFrame([
    {"id": 1, "title": "Inception", "overview": "Dreams inside dreams", "genre": "Sci-Fi"},
    {"id": 2, "title": "Interstellar", "overview": "Space travel to save Earth", "genre": "Sci-Fi"},
    {"id": 3, "title": "The Dark Knight", "overview": "Batman fights crime in Gotham", "genre": "Action"},
    {"id": 4, "title": "Tenet", "overview": "Time inversion thriller", "genre": "Sci-Fi"},
    {"id": 5, "title": "Dunkirk", "overview": "WW2 evacuation story", "genre": "War"},
    {"id": 6, "title": "Memento", "overview": "A man with short-term memory loss", "genre": "Mystery"},
    {"id": 7, "title": "Avatar", "overview": "Aliens and humans clash on Pandora", "genre": "Sci-Fi"},
    {"id": 8, "title": "Prestige", "overview": "Magicians and deception", "genre": "Drama"},
    {"id": 9, "title": "Gravity", "overview": "Space survival", "genre": "Sci-Fi"},
    {"id": 10, "title": "Blade Runner 2049", "overview": "AI and humanity", "genre": "Sci-Fi"},
])

def get_recommendations(title, n=8):
    tfidf = TfidfVectorizer(stop_words="english")
    movies_data["combined"] = movies_data["overview"] + " " + movies_data["genre"]
    tfidf_matrix = tfidf.fit_transform(movies_data["combined"])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    all_titles = movies_data["title"].tolist()
    matched = process.extractOne(title, all_titles)
    if not matched or matched[1] < 60:
        return []

    idx = movies_data[movies_data["title"] == matched[0]].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    return movies_data.iloc[[i[0] for i in sim_scores]].to_dict(orient="records")
