from hash_table_class import hash_table



counter = 0
data_table = hash_table()
def two_sum(data, target):
    for i in data.dict.keys():
        a = target - i
        if data.look_up(a) == 1:
            return 1
    return 0







handle = open('two_sum_data.txt')
for line in handle:
    number = int(line)
    if data_table.look_up(number) == 0:
        data_table.insert(number)




for i in range(-10000, 10001):
    counter += two_sum(data_table, i)
    print(i)

print(counter)