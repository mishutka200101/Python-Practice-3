horses = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}


def do_bet(horse: int, bet: int):
    if horses[horse] != 0 or bet == 0:
        print("Что-то пошло не так")
    else:
        horses[horse] = bet
        print("Ваша ставка в размере", bet, "на лошадь", horse, "принята.")
