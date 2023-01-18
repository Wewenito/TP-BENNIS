def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j] :
                lst[j + 1] = lst[j]
                j -= 1
        lst[j + 1] = key
        print(lst)

list_of_integers = [5, 2, 4, 8, 1, 3]
print("Evolution du tri : ")
insertion_sort(list_of_integers)
print("Liste triée : " + str(list_of_integers))