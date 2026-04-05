import time
import sorting_algorithms as sa
import data_generator as dg
def measure_time(sort_function, data, num_runs=1):
    total_time=0
    for _ in range(num_runs):
        # Folosim time.time() pentru a lua ora exactă înainte și după execuție
        start_time = time.time()
        sort_function(data)
        end_time = time.time()
        
        total_time += (end_time - start_time)
        
    return total_time / num_runs
N=10000
print(f"Se genereaza datele si s creaza o lista aleatorie de {N} elemente.")
list_random=dg.get_random_list(N)
algorithms = {
    "Bubble Sort": sa.bubble_sort,
    "Shaker Sort": sa.shaker_sort,
    "Selection Sort": sa.selection_sort,
    "Insertion Sort": sa.insertion_sort,
    "Merge Sort": sa.merge_sort,
    "Counting Sort": sa.counting_sort,
    "Shell Sort": sa.shell_sort,
    "Timsort (Nativ)": sa.native_sort
}
print("\n" + "="*40)
print(f" Start benchmark (N = {N}) - lista aleatoare")
print("="*40)
for name, func in algorithms.items():
    try:
        exec_time = measure_time(func, list_random, num_runs=1)
        print(f"{name:17} -> {exec_time:.6f} secunde")
    except RecursionError:
        print(f"{name:17} -> EROARE: S-a atinst limita de recursivitate a Python-ului!")
    except Exception as e:
        print(f"{name:17} -> Eroare: {e}")
print("\n Test complet!")
