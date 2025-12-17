def translate(text):
    words = {
        "Привет": "Bonjour",
        "мир": "monde",
        "пока": "au revoir",
        "спасибо": "merci",
        "да": "oui",
        "нет": "non"
    }

    for rus, fr in words.items():
        text = text.replace(rus, fr)
    return text