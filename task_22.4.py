def find_root_of_equation(k):
    if len(k) == 3:
        roots_of_quadratic_equation(k)
    elif len(k) == 2:
        roots_of_linear_equation(k)
    elif len(k) == 1:
        print(k[0])
    else:
        print(None)
    
def roots_of_quadratic_equation(k):
    a, b, c = k[0], k[1], k[2]
    if a != 0:
        D = b ** 2 - 4 * a * c  # дискриминант
        if D > 0:
            x1 = (-b + D ** 0.5) / (2 * a)  # первый корень
            x2 = (-b - D ** 0.5) / (2 * a)  # второй корень
            print(x1, x2)
        elif D == 0:
            x = -b / (2 * a)
            print(x)
        else:
            print("Дискриминант меньше нуля")
    else:
        print("Передайте ненулевое значние a")
    
def roots_of_linear_equation(k):
    b, c = k[0], k[1]
    if b != 0:
        print(-c/b)
    else:
      print("Деление на 0 запрещено")
   
