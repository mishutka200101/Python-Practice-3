base = ["", "Иван", "Юлия Иванкова"]


def hello(name: str):
    print("Здравствуйте", name + "!", "Вашу карту ищут...")


def search_card(name: str):
    if name in base:
        print("Ваша карта с номером", base.index(name), "найдена!")
