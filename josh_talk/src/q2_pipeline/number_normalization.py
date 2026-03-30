mapping = {
    "एक":1, "दो":2, "तीन":3, "चार":4,
    "पांच":5, "दस":10, "सौ":100
}

def normalize_numbers(text):
    words = text.split()
    result = []

    for w in words:
        if w in mapping:
            result.append(str(mapping[w]))
        else:
            result.append(w)

    return " ".join(result)