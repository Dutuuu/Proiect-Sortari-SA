import random
import os
def get_random_list(n, min_val=0, max_val=100000):
    return[random.randint(min_val, max_val) for _ in range(n)]  
def get_sorted_list(n):
    return list(range(n))
def get_reversed_sorted_list(n):
    return list(range(n,0,-1))
def get_nearly_sorted_list(n, swapp_percent = 5):
    arr = list(range(n))
    swaps = int((n*swapp_percent)/100)
    for _ in range(swaps):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
def save_list_to_file(arr, filename):
    if not os.path.exists("date_test"):
        os.makedirs("date_test")
    filepath = os.path.join("date_test", filename)
    with open(filepath, 'w') as f:
        for item in arr:
            f.write(f"{item}\n")
    print(f"Lista a fost salvata in {filepath}")
def load_list_from_file(filename):
    filepath = os.path.join("date_test", filename)
    arr = []
    with open(filepath, 'r') as f:
        for line in f:
            arr.append(int(line.strip()))    
    return arr