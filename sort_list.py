def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def selection_sort(list):
    n = len(list)
    i = 0
    while i < n-1:
        x = list[i]
        temp = i
        j = i+1

        while j < n:
            if list[j] < x:
                x = list[j]
                temp = j
            j += 1
        
        swap(list, i, temp)
        i += 1

def insertion_sort(list):
    n = len(list)
    i = 0
    while i < n-1:
        j = i+1
        while j > 0 and list[j] < list[j-1]:
            swap(list, j, j-1)
            j -= 1
        i += 1