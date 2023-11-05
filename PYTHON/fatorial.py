#Fatorial: Crie um programa que calcule o fatorial de um número inteiro não negativo fornecido pelo usuário. O fatorial de um número N é o produto de todos os inteiros de 1 a N.

n = int(input('Digite um número inteiro não negativo para cálculo de seu fatorial: '))
f=1
for i in range(1, n+1):
    f*=i

print(f'O fatorial de {n} é: {f}')
