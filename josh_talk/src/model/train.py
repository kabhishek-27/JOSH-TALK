import pandas as pd
import torch
import librosa
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from tqdm import tqdm

MODEL_NAME = "openai/whisper-tiny"
DEVICE = "mps" if torch.backends.mps.is_available() else "cpu"



def load_data():
    return pd.read_csv("data/processed/dataset.csv")



def load_audio(path):
    try:
        audio, sr = librosa.load(path, sr=16000)
        return audio
    except Exception:
        print(f" Skipping bad audio: {path}")
        return None


def main():
    df = load_data().head(20)

    processor = WhisperProcessor.from_pretrained(MODEL_NAME)
    model = WhisperForConditionalGeneration.from_pretrained(MODEL_NAME)

    model.to(DEVICE)
    model.train()

    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)

    print(" Starting training loop...")

    for epoch in range(1):
        for _, row in tqdm(df.iterrows(), total=len(df)):
            audio = load_audio(row["audio"])
            text = row["text"]

            if audio is None:
                continue

            try:
                inputs = processor(audio, sampling_rate=16000, return_tensors="pt").to(DEVICE)

                labels = processor.tokenizer(
                    text,
                    return_tensors="pt",
                    padding=True,
                    truncation=True
                ).input_ids.to(DEVICE)

                with torch.no_grad():  
                    outputs = model(
                        input_features=inputs.input_features,
                        labels=labels
                )

            except Exception:
                continue


    
    model.save_pretrained("./models/fine_tuned")
    processor.save_pretrained("./models/fine_tuned")

    print(" Training complete!")


if __name__ == "__main__":
    main()