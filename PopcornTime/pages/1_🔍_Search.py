import streamlit as st
from app.search_engine import autocomplete_results

st.title("🔍 Search Movies & TV Shows")
st.markdown("Find your favorite movies or shows using our AI-powered TMDb search.")

query = st.text_input("Start typing...", "")

if query:
    results = autocomplete_results(query)
    if results:
        for i in range(0, len(results), 6):
            cols = st.columns(6)
            for idx, item in enumerate(results[i:i+6]):
                with cols[idx]:
                    st.image(item["poster"], use_column_width=True)
                    st.caption(f"🎬 {item['name']}")
    else:
        st.error("❌ No results found. Try another title.")
else:
    st.info("🔎 Type a movie or show name to begin searching.")
