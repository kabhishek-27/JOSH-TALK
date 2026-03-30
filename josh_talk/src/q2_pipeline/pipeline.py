from number_normalization import normalize_numbers
from english_detection import detect_english

def process(text):
    text = normalize_numbers(text)
    text = detect_english(text)
    return text