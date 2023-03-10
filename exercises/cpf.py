
cpf = "511408978"

contagem = 10
lista = []

for numero in cpf:

    lista.append(int(numero) * contagem)
    contagem -= 1

soma = lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + lista[5] + lista[6] + lista[7] + lista[8]

multi = soma * 10

resto = multi % 11

print(resto)