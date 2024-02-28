def bubblesort(list):
    i = 0
    n = len(list)
    while i<n-1:
        j = 0
        while j<n-i-1:
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
            j = j+1
        i = i+1
