
def main():
    
    def quick_sort(arr : list) -> list:
        n = len(arr)-1
        #Provarè de posar el pivote al mig quan j creui a i
        i = 0 #used to find element bigger than the pivote
        j = n - 1 #used to find element smaller than the pivote
        p = n #used as a pivot
        while i <= j:#En el moment que la 'j' sigui més petita, surt
            if arr[i] > arr[p] or arr[j] < arr[p]:
                if arr[i] > arr[p] and arr[j] < arr[p]:#Pero si es compleixen les dues
                    #swap elements
                    arr[i] , arr[j] = arr[j] , arr[i]  
                    i +=1
                    j -=1
                #Per tant si la 'j' es més gran, busquem altre element que sigui més petit que el pivot
                if arr[j] > arr[p]:
                    j-=1
                #Per tant si la 'i' es més petit, busquem altre element que sigui més gran que el pivot
                if arr[i] < arr[p]:
                    i+=1         
        arr[p] , arr[i] = arr[i] , arr[p]
    
        arr_left = arr[:i]
        arr_right = arr[i:]
        
        quick_sort(arr_left)
        quick_sort(arr_right)
        
        return arr 
            
        
    test_arr = [22,11,88,66,55,77,33,44]
    arr = quick_sort(test_arr)
    print(arr)

if __name__=="__main__":
    main()
    