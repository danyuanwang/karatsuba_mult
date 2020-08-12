# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def extract_file():
    handle = open('data_array_coursera_algo_week2.txt')
    print(handle)
    list = []
    for line in handle:
        list.append(float(line))
    return list




def split_list(list):
    half = len(list)//2
    return list[:half], list[half:]


def count_split_inv(list_first, list_second, n):
    sorted_list = []
    inv = 0
    i = 0
    j = 0
    print(list_first, list_second)
    print(n)
    for k in range(n):
        if i >= len(list_first):
            sorted_list.insert(k, list_second[j])
            j += 1
        elif j >= len(list_second):
            sorted_list.insert(k, list_first[i])
            i += 1

        else:
            if list_first[i] < list_second[j]:
                sorted_list.insert(k, list_first[i])
                i += 1
            elif list_first[i] > list_second[j]:
                sorted_list.insert(k, list_second[j])
                j += 1
                inv += len(list_first) - i

    return inv, sorted_list





def count(list):
    # Use a breakpoint in the code line below to debug your script.
    n = len(list)
    if n == 1:
        print('base')
        return 0, list
    else:
        list_first, list_second = split_list(list)
        x, sorted_first = count(list_first)
        y, sorted_second = count(list_second)
        z, sorted_list = count_split_inv(sorted_first, sorted_second, n)
        print(sorted_list)
        print('answer')
        print(x + y + z)

        return x + y + z, sorted_list
file = extract_file()
count(file)

# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
