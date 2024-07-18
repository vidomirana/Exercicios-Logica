def insertion_sort(list):           #     j
    for i in range(1, len(list)):   #  (3|2 1 4)
        value = list[i]             #     i
        j = i
        while j > 0 and list[j-1] > value:
            list[j] = list[j-1]
            j -= 1
        list[j] = value
    return list


lista = [5,7,1,3,2,4,6]

sorted = insertion_sort(lista)
print(sorted)

#Esse algoritmo tem complexidade O(n^2)

