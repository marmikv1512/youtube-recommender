
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

df = pd.read_csv("data/clean_videos.csv")
texts = df["text"].tolist()

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts)

np.save("data/embeddings.npy", embeddings)
print("Embeddings saved.")
