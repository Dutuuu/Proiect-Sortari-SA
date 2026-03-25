def bubble_sort(arr): #O[n^2]
    arr = arr.copy() #copie pentru a nu modifica lista originala
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
        if not swapped:
            break   
    return arr
def shaker_sort(array): #O[n^2]
    arr = array.copy()
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        
        if not swapped:
            break
            
        swapped = False
        end = end - 1
        
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
                
        start = start + 1
    return arr
def selection_sort(array): #O[n^2]
    arr = array.copy()
    n = len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index]= arr[min_index], arr[i]
    return arr
def insertion_sort(array):  #O[n^2]
    arr= array.copy()
    n = len(arr)
    for i in range(1 , n):
        key = arr[i]
        j = i - 1 
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1 
        arr[j + 1] = key
    return arr
def counting_sort(array):#O[n+k]
    arr=array.copy()
    if not arr:
        return arr
    max_val=max(arr)
    min_val=min(arr)
    range_of_elements= max_val - min_val + 1 #calculeaza gama de valori
    #se creeaza lista pentru numararea aparitiilor si lista finala
    count = [0] * range_of_elements
    output = [0] * len(arr)
    for i in range(len(arr)): #se numara de cate ori apare fiecare element
        count[arr[i] - min_val] +=1
    for i in range(1,len(count)): #modifica array ca sa contina pozitile reale
        count[i] += count[i-1]
    for i in range(len(arr) -1 , -1 , -1):#se construieste lista sortata de la dreapta la stg
        output[count[arr[i]-min_val] - 1]= arr[i]
        count[arr[i] - min_val] -= 1
    for i in range(len(arr)):
        arr[i]=output[i]
    return arr
def shell_sort(arr_input):
    arr = arr_input.copy()
    n = len(arr)
    
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
        
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                
            arr[j] = temp
            
        gap //= 2
        
    return arr
