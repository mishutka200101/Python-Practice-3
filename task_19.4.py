def palindrome(text: str):
    text = text.replace(' ', '')
    text = text.lower()
    if text == text[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")
