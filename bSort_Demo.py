def main():
    from arraySupport import readRandomList, showList, sortCheck
    from bubblesort import bubblesort
    list = readRandomList()
    showList(list)
    bubblesort(list)
    if sortCheck:
        showList(list, "SortedList")
    else:
        print("\nSorting isn't completed.")

main()
