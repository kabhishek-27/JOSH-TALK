def detect_english(text):
    words = text.split()
    output = []

    for w in words:
        if any(char.isascii() for char in w):
            output.append(f"[EN]{w}[/EN]")
        else:
            output.append(w)

    return " ".join(output)