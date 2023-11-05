#Soma dos Números Pares: Escreva um programa que calcule a soma de todos os números pares de 1 a N, onde N é fornecido pelo usuário.

n = int(input('Escreva um número inteiro: '))
soma=0
for i in range(1, n+1):
    if i%2==0:
        soma+=i

print(f'A soma de todos os números pares de 1 a {n} é: {soma}')