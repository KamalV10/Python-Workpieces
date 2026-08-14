text = input("Введите текст: ")
reversed_text = text[::-1]
def toggle_layout(text: str) -> str:
    en_to_ru = {
        'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г',
        'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
        'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о',
        'k': 'л', 'l': 'д', ';': 'ж', "'": 'э',
        'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь',
        ',': 'б', '.': 'ю', '/': '.'
    }

    ru_to_en = {v: k for k, v in en_to_ru.items()}
    result = []

    for char in text:
        lower_char = char.lower()
        if lower_char in en_to_ru:
            new_char = en_to_ru[lower_char]
        elif lower_char in ru_to_en:
            new_char = ru_to_en[lower_char]
        else:
            result.append(char)
            continue

        if char.isupper():
            new_char = new_char.upper()
        result.append(new_char)

    return ''.join(result)
print("Перевёрнутый текст:", reversed_text)
print("Полностью заглавные буквы", text.upper())
print("Полностью строчные буквы", text.lower())
print("Измененная раскладка", result)