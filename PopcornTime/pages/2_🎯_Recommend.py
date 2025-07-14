import streamlit as st
from app.recommender import get_recommendations

st.title("🎯 Movie Recommender")
st.markdown("Enter a movie you like, and get AI-powered similar recommendations.")

movie = st.text_input("Enter a known movie title (e.g. Inception, Avatar)", "")

if movie:
    recs = get_recommendations(movie)
    if recs:
        st.success("✅ Recommendations based on your input:")
        for i in range(0, len(recs), 6):
            cols = st.columns(6)
            for idx, rec in enumerate(recs[i:i+6]):
                with cols[idx]:
                    st.subheader(rec["title"])
                    st.caption(f"🎭 {rec['genre']}")
                    st.markdown(f"<small>{rec['overview'][:100]}...</small>", unsafe_allow_html=True)
    else:
        st.warning("No close match found. Try a popular movie name.")
else:
    st.info("Enter a movie name to get recommendations.")
