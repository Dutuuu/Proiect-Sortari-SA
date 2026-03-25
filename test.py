import data_generator as dg
import sorting_algorithms as sa
lista = dg.get_random_list(10, 0, 10000)
print (f"lista initiala: {lista}\n")
print ("counting_sort: ", sa.counting_sort(lista))
print ("shell_sort", sa.counting_sort(lista))