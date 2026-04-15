import data_generator as dg

dimensiuni = [100, 1000, 5000, 10000, 50000, 100000]
for n in dimensiuni:
    print(f"Generăm date pentru N = {n} ---")
    
    # 1. Random 
    lista_random = dg.get_random_list(n)
    dg.save_list_to_file(lista_random, f"random_{n}.txt")
    
    # 2. Sortate
    lista_sortata = dg.get_sorted_list(n)
    dg.save_list_to_file(lista_sortata, f"sortate_{n}.txt")
    
    # 3. Invers sortate
    lista_inversata = dg.get_reversed_sorted_list(n)
    dg.save_list_to_file(lista_inversata, f"invers_sortate_{n}.txt")
    
    # 4. Aproape sortate
    lista_aproape = dg.get_nearly_sorted_list(n)
    dg.save_list_to_file(lista_aproape, f"aproape_sortate_{n}.txt")
    
print("\nToate fisierele au fost create in folderul 'date_test'")