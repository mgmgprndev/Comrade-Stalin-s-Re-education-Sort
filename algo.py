import random
import time

def stalin_pass(input_list):
    if not input_list:
        return [], []
    tolerated = [input_list[0]]
    purged = []
    for i in range(1, len(input_list)):
        if input_list[i] >= tolerated[-1]:
            tolerated.append(input_list[i])
        else:
            purged.append(input_list[i])
    return purged, tolerated

def is_sorted(input_list):
    for i in range(len(input_list) - 1):
        if input_list[i] > input_list[i+1]:
            return False
    return True

def recursive_stalin_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    purged, tolerated = stalin_pass(input_list)
    if not purged:
        return tolerated
    sorted_purged = recursive_stalin_sort(purged)
    return sorted_purged + tolerated

# TEST
initial_array_random = [random.randint(1, 1000) for _ in range(100000)]

startTime = time.time()
sorted_array_random = recursive_stalin_sort(initial_array_random)
endTime = time.time()
diff = endTime - startTime
print(f"\n\n\nDone in {diff:.12f} seconds")
