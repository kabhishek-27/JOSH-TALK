import os
import pandas as pd

DATA_DIR = "data/raw"
OUT_CSV = "data/processed/dataset.csv"


def preprocess():
    os.makedirs("data/processed", exist_ok=True)

    rows = []

    if not os.path.exists(DATA_DIR):
        print(" data/raw not found")
        return

    for file in os.listdir(DATA_DIR):
        if file.endswith(".wav"):
            audio_path = os.path.join(DATA_DIR, file)
            text_path = audio_path.replace(".wav", ".txt")

            if not os.path.exists(text_path):
                print(f" Missing text for {file}")
                continue

            text = open(text_path, encoding="utf-8").read().strip()

            rows.append({
                "audio": audio_path,
                "text": text
            })

    if len(rows) == 0:
        print(" No valid data found")
        return

    df = pd.DataFrame(rows)
    df.to_csv(OUT_CSV, index=False)

    print(" Dataset created:", OUT_CSV)
    print("Total samples:", len(rows))


if __name__ == "__main__":
    preprocess()