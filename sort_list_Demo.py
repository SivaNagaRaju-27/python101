def main():
    from arraySupport import readRandomList, showList, sortCheck
    from sort_list import insertion_sort
    list = readRandomList()
    showList(list)
    insertion_sort(list)
    if sortCheck(list):
        showList(list, "SortedList")
        print("Good Job")
    else:
        print("\nSorting isn't completed.")
        showList(list, "Fail")

main()