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
for line in handle:
    number = int(line)
    if counter % 2 == 0:
        if number > median:
            if heap_min.length() > heap_max.length():
                node = heap_min.extract_root()
                heap_max.insert(node)
            heap_min.insert(number)
            node = heap_max.extract_root()
            median = node + number
            heap_max.insert(node)
            med_sum += median    

        else:
            if heap_max.length() > heap_min.length():
                node = heap_max.extract_root()
                heap_min.insert(node)
            heap_max.insert(number)
            node = heap_min.extract_root()
            median = node + number
            heap_min.insert(node)
            med_sum += median    

    elif counter % 2 == 1:
        if number > median:
            heap_min.insert(number)
            median = heap_min.extract_root()
            heap_min.insert(median)
            med_sum += median
        else:
            heap_max.insert(number)
            median = heap_max.extract_root()
            heap_max.insert(median)
            med_sum += median        
print(med_sum % 10000)