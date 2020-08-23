# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def extract_file():
    handle = open('data_QuickSort.txt')
    print(handle)
    list = []
    for line in handle:
        list.append(float(line))
    return list


def pick_pivot(list, l, r):
    options = [list[l], list[r], list[(r + l) // 2]]
    middle = sum(options) - max(options) - min(options)
    print(options)
    print(middle)
    if middle == list[l]:
        pass
    elif middle == list[r]:
        c = list[l]
        list[l] = list[r]
        list[r] = c
        #print(list)
    else:
        c = list[l]
        list[l] = list[(r + l) // 2]
        list[(r + l) // 2] = c
        #print(list)





def swap(a, b):
    c = a
    a = b
    b = c

def partition(list, l, r):
    p = list[l]
    i = l + 1
    comparisons = r - l
    #print('l and r', l, r)
    for j in range(l + 1 , r + 1):
        #print(i, j, l, r, p)

        if j < len(list)  and list[j] < p:
            c = list[j]
            list[j] = list[i]
            list[i] = c
            i = i + 1

    f = list[l]
    list[l] = list[i - 1]
    list[i - 1] = f
    #print('list', list)
    return comparisons, (i-1)

def quick_sort_function(list, s, e):
    print(e - s)
    if(e-s <= 1):
        print('end')
        return 0
    pi = pick_pivot(list)
    comparisions = partition(list, s, e)
    if(s < pi):
        comparisions += quick_sort_function(list,s, pi)
    if(pi < e):
        comparisions += quick_sort_function(list, pi, e)
    return comparisions


def quick_sort(list, l, r):
    # Use a breakpoint in the code line below to debug your script.
    #print(l, r)
    #print(r - l)
    if r - l < 1:
        #print('base')
        return 0
    else:
        pick_pivot(list, l, r)

        comparisons, pivot = partition(list, l, r)
        #print('pivot:' + str(pivot))
        comparisons += quick_sort(list, l, pivot - 1)
        comparisons += quick_sort(list, pivot + 1, r)

        return comparisons


# Press the green button in the gutter to run the script.
list = extract_file()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(quick_sort(list, 0, len(list)- 1))
#print(list)