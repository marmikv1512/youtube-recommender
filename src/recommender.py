
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity # type: ignore

class YouTubeRecommender:
    def __init__(self, data_file="clean_videos.csv", embed_file="embeddings.npy"):
        # Load cleaned data
        self.df = pd.read_csv(data_file)

        # Load embeddings (generated earlier)
        self.embeddings = np.load(embed_file)

    def recommend(self, index, top_n=5):
        # Compute similarity scores for selected video
        sim_scores = cosine_similarity(
            [self.embeddings[index]], 
            self.embeddings)
        [0]

        # Get top N similar videos (excluding itself)
        similar_indices = sim_scores.argsort()[-top_n-1:-1][::-1]

        # Return recommended videos as a dataframe
        return self.df.iloc[similar_indices][["title", "thumbnail", "videoId"]]

# Run a test
if __name__ == "__main__":
    rec = YouTubeRecommender()
    result = rec.recommend(0, top_n=5)
    print(result)
