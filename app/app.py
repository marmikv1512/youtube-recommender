
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity # type: ignore

st.title("🎥 AI YouTube Video Recommender")

df = pd.read_csv("data/clean_videos.csv")
embeddings = np.load("data/embeddings.npy")

video_titles = df["title"].tolist()
selected_video = st.selectbox("Select a video:", video_titles)

idx = video_titles.index(selected_video)

sim = cosine_similarity([embeddings[idx]], embeddings)[0]
top_indices = sim.argsort()[-6:-1][::-1]

st.subheader("Recommended Videos:")

for i in top_indices:
    row = df.iloc[i]
    st.image(row.thumbnail, width=320)
    st.write(f"**{row.title}**")
    st.markdown(f"[Watch on YouTube](https://youtube.com/watch?v={row.videoId})")
    st.write("---")