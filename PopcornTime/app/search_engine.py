from app.api import search_movie, get_poster_url

def autocomplete_results(query):
    results = search_movie(query)
    suggestions = []

    for r in results:
        name = r.get('title') or r.get('name')
        poster = get_poster_url(r.get('poster_path'))
        if name:
            suggestions.append({
                "id": r["id"],
                "name": name,
                "poster": poster,
                "media_type": r["media_type"]
            })

    return suggestions
