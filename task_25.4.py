import random
 
st1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g',
       'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
st2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
       'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
st3 = ['2', '3', '4', '5', '6', '7', '8', '9']
st4 = st1 + st2 + st3
 
 
def generate_password(m):
    pas = []
    a1 = random.choice(st1)
    a2 = random.choice(st2)
    a3 = random.choice(st3)
 
    if a1 not in pas:
        pas.append(a1)
    if a2 not in pas:
        pas.append(a2)
    if a3 not in pas:
        pas.append(a3)
    for i in range(0, m - 3):
        while True:
            a = random.choice(st4)
            if a not in pas:
                pas.append(a)
                break
            else:
                continue
    random.shuffle(pas)
    return ''.join(pas)
 
 
def main(n, m):
    list_passw = set()
    while len(list_passw) < n:
        if generate_password(m) not in list_passw:
            list_passw.add(generate_password(m))
    return list_passw
