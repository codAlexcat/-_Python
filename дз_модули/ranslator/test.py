from ranslator import english, spanish, french

def translate(text, lang):
    try:
        if lang == "english":
            return english.translate(text)
        elif lang == "spanish":
            return spanish.translate(text)
        elif lang == "french":
            return french.translate(text)

    except ModuleNotFoundError:
        return f"Язык '{lang}' не поддерживается"

    except AttributeError:
        return f"Модуль для языка '{lang}' не содержит функцию translate()"

