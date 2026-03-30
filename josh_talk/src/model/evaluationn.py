import pandas as pd
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from jiwer import wer
import torch
import librosa

MODEL_PATH = "openai/whisper-tiny"
DEVICE = "mps" if torch.backends.mps.is_available() else "cpu"


def load_audio(path):
    try:
        audio, sr = librosa.load(path, sr=16000)
        return audio
    except:
        return None


def main():
    print(" Loading dataset...")

    df = pd.read_csv("data/processed/dataset.csv").head(20)

    processor = WhisperProcessor.from_pretrained(MODEL_PATH)
    model = WhisperForConditionalGeneration.from_pretrained(MODEL_PATH).to(DEVICE)

    predictions = []
    references = []

    print(" Running evaluation...")

    for _, row in df.iterrows():
        audio = load_audio(row["audio"])
        text = row["text"]

        if audio is None:
            continue

        try:
            inputs = processor(audio, sampling_rate=16000, return_tensors="pt").to(DEVICE)

            with torch.no_grad():
                pred_ids = model.generate(inputs.input_features)

            pred = processor.batch_decode(pred_ids, skip_special_tokens=True)[0]

            predictions.append(pred)
            references.append(text)

        except Exception:
            continue

    score = wer(references, predictions)

    print("\n WER:", score)


if __name__ == "__main__":
    main()