print("Digite um número")
y = int(input(">>> "))
x = 0
if y <=0:
    print("Número Inválido")
if y > 0:
    while True:
        x = x + 1
        if x < y:
            print(x**2)
        if x ==y:
            print(x**2)
            break
