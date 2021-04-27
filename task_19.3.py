def roots_of_quadratic_equation(a, b, c):
    sp = []
    if a == 0 and b == 0 and c == 0:
        sp.append("all")
        return sp
    elif a == 0 and b == 0:
        return []
    elif a == 0:
        sp.append(-c / b)
    else:
        d = b ** 2 - 4 * a * c
        if d > 0:
            sp.append((-b + d ** 0.5) / (2 * a))
            sp.append((-b - d ** 0.5) / (2 * a))
        elif d == 0:
            sp.append(-b / (2 * a))
        else :
            return []
        return sp
 
result = roots_of_quadratic_equation(2, -8, 0)
if 'all' in result:
   if result == ['all']:
       print('0 0 0')
   else:
       print('fail')
else:
   print(*sorted(result))
