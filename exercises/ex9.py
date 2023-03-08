
## Calculadora com while

while True:

    print("Bem-vindo a Calculadora com While!")
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    if num1.isdigit() or num2.isdigit():
        operador = input("Digite um operador: + ou - ou * ou /: ")

        if operador == "+":
            soma = int(num1) + int(num2)
            print(f"A soma entre {num1} e {num2} é {soma}")
            choose = input(f"Caso queira sair, digite \"exit\"")
            
            if choose.lower() == "exit":
                break

        if operador == "-":
            soma = int(num1) - int(num2)
            print(f"A subtração entre {num1} e {num2} é {soma}")
            choose = input(f"Caso queira sair, digite \"exit\"")

            if choose.lower() == "exit":
                break

        if operador == "*":
            soma = int(num1) * int(num2)
            print(f"A multiplicação entre {num1} e {num2} é {soma}")
            choose = input(f"Caso queira sair, digite \"exit\"")

            if choose.lower() == "exit":
                break

        if operador == "/":
            soma = int(num1) / int(num2)
            print(f"A divisão entre {num1} e {num2} é {soma}")
            choose = input(f"Caso queira sair, digite \"exit\"")

            if choose.lower() == "exit":
                break
            
    else:
        print("Digite números válidos.")
        continue

    