import random
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
def get_flat_list(n, distinct_vals = 5 ):
    pool = [random.randint(0, 100) for _ in range(distinct_vals)]
    return [random.choice(pool) for _ in range(n)]
