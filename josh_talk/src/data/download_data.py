import pandas as pd
import requests
import os
from tqdm import tqdm
from pydub import AudioSegment

SAVE_DIR = "data/raw"
os.makedirs(SAVE_DIR, exist_ok=True)


def download_file(audio_url, raw_audio_path):
    try:
        r = requests.get(url, timeout=20)
        if r.status_code == 200:
            with open(path, "wb") as f:
                f.write(r.content)
        else:
            print(f" Failed: {url}")
            return False
        return True
    except Exception as e:
        print(f" Error: {url} -> {e}")
        return False


def convert_to_wav(input_path, output_path):
    try:
        audio = AudioSegment.from_file(input_path)
        audio = audio.set_frame_rate(16000).set_channels(1)
        audio.export(output_path, format="wav")
        return True
    except Exception as e:
        print(f" Conversion failed: {input_path} -> {e}")
        return False


def main():
    df = pd.read_excel("ft_data.xlsx")
    
    
    df.columns = df.columns.str.strip()

    print("Columns:", df.columns)  

    for _, row in tqdm(df.iterrows(), total=len(df)):
        try:
            recording_id = row["recording_id"]

            wav_audio_path = f"{SAVE_DIR}/{recording_id}.wav"
            text_path = f"{SAVE_DIR}/{recording_id}.txt"

            
            from pydub import AudioSegment
            silent = AudioSegment.silent(duration=2000)
            silent.export(wav_audio_path, format="wav")

            
            text = f"यह एक डमी वाक्य है {recording_id}"

            with open(text_path, "w", encoding="utf-8") as f:
                f.write(text)

        except Exception as e:
            print(f" Skipping row: {e}")


if __name__ == "__main__":
    main()