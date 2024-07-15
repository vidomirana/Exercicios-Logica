def selection_sort(list):
    for i in range(0, len(list)):
        min_value = list[i]
        min_index = i
        for j in range(i+1, len(list)):
            if list[j] < min_value:
                min_value = list[j]
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

lista = [2,6,0,1,8,4,3,7,9,5]

print(selection_sort(lista))