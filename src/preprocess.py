
import pandas as pd

def clean_data(input_file="videos.csv", output_file="clean_videos.csv"):
    # Load raw data
    df = pd.read_csv(input_file)

    # Replace NaN values with empty strings
    df["title"] = df["title"].fillna("")
    df["description"] = df["description"].fillna("")

    # Combine title + description → this is what embeddings will use
    df["text"] = df["title"] + " " + df["description"]

    # Remove rows where text is empty
    df = df[df["text"].str.strip() != ""]

    # Save clean dataset
    df.to_csv(output_file, index=False)

    print(f"Cleaned data saved to {output_file}")

# Run the function
if __name__ == "__main__":
    clean_data()
