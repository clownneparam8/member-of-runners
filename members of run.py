a = list()
b = input('введите участика(0 - стоп)')
while b != 0:
    a.append(b)
    a.sort()
    print(a)
    b = input('введите участика(0 - стоп)')
