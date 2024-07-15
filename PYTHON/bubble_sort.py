def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

lista = [5,8,1,2,7,9,3,6,4,0]

ordenado = bubble_sort(lista)
print(ordenado)