import time
import sorting_algorithms as sa
import data_generator as dg

def measure_time(sort_function, data, num_runs=1):
    total_time = 0
    for _ in range(num_runs):
        lista_de_lucru = data.copy() 
        
        start_time = time.time()
        sort_function(lista_de_lucru)
        end_time = time.time()
        
        total_time += (end_time - start_time)
        
    return total_time / num_runs

N = 10000 # Dimensiunea pe care vrem să o testam acum
nume_fisier = f"random_{N}.txt" # Schimba aici cu "sortate_1000.txt", "invers_sortate_1000.txt" etc.

print(f"Citim datele din fișierul: {nume_fisier}")

lista_test = dg.load_list_from_file(nume_fisier)

algorithms = {
    "Bubble Sort": sa.bubble_sort,
    "Shaker Sort": sa.shaker_sort,
    "Selection Sort": sa.selection_sort,
    "Insertion Sort": sa.insertion_sort,
    "Merge Sort": sa.merge_sort,
    "Quick Sort": sa.quick_sort,
    "Counting Sort": sa.counting_sort,
    "Shell Sort": sa.shell_sort,
    "Timsort": sa.native_sort
}

print("\n" + "="*50)
print(f"  START BENCHMARK - FIȘIER: {nume_fisier}")
print("="*50)

for name, func in algorithms.items():
    try:
        exec_time = measure_time(func, lista_test, num_runs=1)
        print(f"{name:17} -> {exec_time:.6f} secunde")
    except Exception as e:
        print(f"{name:17} -> EROARE: {e}")

print("\nTest complet")