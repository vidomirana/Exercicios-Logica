#Ordenação de Lista: Crie um programa que receba uma lista de números e os ordene em ordem crescente ou decrescente, dependendo da escolha do usuário.

def organizar(lista, ordem):
    '''
    Função para organizar elementos numéricos de uma lista
    :lista: Lista a ser ordenada
    :ordem: ordem d organização, 'c'=crescente (padrão), 'd'=decrescente
    '''
    lista_copy = lista.copy()  # Cria uma cópia da lista original

    if ordem == 'c':
        for num in range(0, len(lista_copy)):
            for i in range(num+1, len(lista_copy)):
                if lista_copy[num] > lista_copy[i]:
                    lista_copy[i], lista_copy[num] = lista_copy[num], lista_copy[i]
    if ordem == 'd':
        for num in range(0, len(lista_copy)):
            for i in range(num+1, len(lista_copy)):
                if lista_copy[num] < lista_copy[i]:
                    lista_copy[i], lista_copy[num] = lista_copy[num], lista_copy[i]
    return lista_copy

numeros = []
while True:
    n = int(input('Digite um número [999 para terminar]: '))
    if n == 999:
        break
    numeros.append(n)

print(f'Lista original: {numeros}')
print('======================================')

lista_crescente = organizar(numeros, 'c')
lista_decrescente = organizar(numeros, 'd')

print(f'Lista organizada crescente: {lista_crescente}')
print('======================================')
print(f'Lista organizada decrescente: {lista_decrescente}')
