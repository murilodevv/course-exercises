
nome = "Murilo Machado"

number = 0
novo_nome = ""

while number < len(nome):
    letra = f"*{nome[number]}"
    novo_nome += letra
    
    number += 1

print(novo_nome)