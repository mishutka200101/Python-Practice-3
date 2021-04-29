lastTicket = 123321


def lucky(number: int):
    number_listed = list(str(number))
    last_ticket_listed = list(str(lastTicket))
    while len(number_listed) < 6:
        number_listed.insert(0, "0")
    while len(last_ticket_listed) < 6:
        last_ticket_listed.insert(0, "0")
    if int(number_listed[0]) + int(number_listed[1]) + int(number_listed[2]) == int(number_listed[3]) \
            + int(number_listed[4]) + int(number_listed[5]):
        number_lucky = True
    else:
        return "Несчастливый"
    if number_lucky and int(last_ticket_listed[0]) + int(last_ticket_listed[1]) + int(last_ticket_listed[2]) == \
            int(last_ticket_listed[3]) + int(last_ticket_listed[4]) + int(last_ticket_listed[5]):
        return "Счастливый"
