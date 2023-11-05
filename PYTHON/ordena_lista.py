#Ordenação de Lista: Crie um programa que receba uma lista de números e os ordene em ordem crescente ou decrescente, dependendo da escolha do usuário.

numeros = [4,3,9,8,1] #[1, 4, 9, 8, 3]
'''while True:
    n = int(input('Digite um número [999 para terminar]: '))
    if n == 999:
        break
    numeros.append(n)
#numeros.insert(2, n) 
print(f'Lista original: {numeros}')

for i in range(0, len(numeros)):
    if  numeros[i] > numeros[i+1]:
'''
for x in range(0, len(numeros)-1):
    for i in range(numeros[x+1], len(numeros)+1):   ###revisar isso aqui, parei no meio do raciocinio
        if numeros[x] > numeros[i]:
            numeros[i], numeros[x] = numeros[x], numeros[i]

print(f'Lista organizada crescente: {numeros}')
