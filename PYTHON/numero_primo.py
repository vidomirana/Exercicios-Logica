#Número Primo: Escreva um programa que determine se um número fornecido pelo usuário é um número primo ou não. Um número primo é aquele que só é divisível por 1 e por si mesmo.

n = int(input('Digite um número inteiro: '))

for i in range(2, n):
    if n%i == 0:
        print(f'{n} não é um número primo')
        break
    if (i==n-1) and (n%i != 0):
        print(f'{n} é um número primo')
