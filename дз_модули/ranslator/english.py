def translate(text):
    words = {
        "Привет": "Hello",
        "мир": "world",
        "пока": "goodbye",
        "спасибо": "thank you",
        "да": "yes",
        "нет": "no"
    }

    for rus, eng in words.items():
        text = text.replace(rus, eng)
    return text
