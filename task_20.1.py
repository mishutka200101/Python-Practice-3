alphabet = ["А", "а", "Е", "е", "Ё", "ё", "И", "и", "О", "о", "У", "у", "Ы", "ы", "Э", "э", "Ю", "ю", "Я", "я"]


def translate(text: str):
    text = list(text)
    for j in range(0, len(text)):
        for i in alphabet:
            if i in text:
                text.pop(text.index(i))
    text = "".join(text)
    text = text.replace(".", "").replace(",", "").replace("-", "").replace("   ", " ").replace("  ", " ")
    print(text)
