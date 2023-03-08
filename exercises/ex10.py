
import os

palavra = "amor"
letras_acertadas = ""
tentativas = 0

while True:

    letra_digitada = input("Digite uma letra: ")
    tentativas += 1

    if len(letra_digitada) < 1:
        print("Digite somente uma letra.")
        continue

    if letra_digitada in palavra:
        letras_acertadas += letra_digitada
    
    palavra_formada = ""
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    
    print(f"Palavra formada: {palavra_formada}")

    if palavra_formada == palavra:
        os.system('clear')
        print("VOCÊ GANHOU!")
        print(f"A palavra era {palavra}")
        print(f"Tentativas {tentativas}")
        letras_acertadas = ""
        tentativas = 0