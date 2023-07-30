list_a = [4, 7, 1, 3]



for i in range(len(list_a)):
    for j in range(len(list_a)):
        print(i, j)
        if list_a[i] == list_a[j]:
            continue
        elif list_a[i] > list_a[j]:
            continue
        else:
            list_a[i], list_a[j] = list_a[j], list_a[i]
        print(list_a)
        print('-----------..-------')

