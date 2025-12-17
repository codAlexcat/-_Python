def translate(text):
    words = {
        "Привет": "¡Hola",
        "мир": "mundo!",
        "пока": "adiós",
        "спасибо": "gracias",
        "да": "sí",
        "нет": "no"
    }

    for rus, esp in words.items():
        text = text.replace(rus, esp)
    return text