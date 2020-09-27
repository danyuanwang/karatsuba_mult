from heap_class_min import heap_min
from heap_class_max import heap_max
import sys
import time


heap_min = heap_min(10000)
heap_max = heap_max(10000)
counter = 1
median = 0
handle = open('heap_data.txt')
med_sum = 0

def get_median(heap_min, heap_max, num_added):
    median_v = 0
    if num_added % 2 == 1:
        if heap_min.length() > heap_max.length():
            median_v = heap_min.extract_root()
            heap_min.insert(median_v)
        else:
            median_v = heap_max.extract_root()
            heap_max.insert(median_v)
    else:
        median_v = heap_max.extract_root()
        heap_max.insert(median_v)
    return median_v

def insert_value(heap_min, heap_max, num_added, value):
    if num_added % 2 == 1:
        if value > median:
            heap_min.insert(value)
        else:
            heap_max.insert(value)
    else:
        if heap_min.length() > heap_max.length():
            other_value = heap_min.extract_root()
            #print(other_value, 'other val')
            #print(heap_min.q, heap_min.n)
            #print(heap_max.q, heap_max.n)
        else:
            other_value = heap_max.extract_root()
        if other_value > value:
            heap_min.insert(other_value)
            heap_max.insert(value)
        else:
            heap_max.insert(other_value)
            heap_min.insert(value)



for line in handle:
    number = int(line)
    insert_value(heap_min, heap_max, counter, number)
    #print(heap_max.q, heap_min.q)
    median = get_median(heap_min, heap_max, counter)
    #print(median)
    med_sum += median
    #print(med_sum)
    counter += 1
print(med_sum)