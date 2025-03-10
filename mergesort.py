def main():
    def merge_sort(arr: list) -> list:
        if len(arr) > 1:
            #Dividirem arr en 2 parts
            right_arr = arr[len(arr)//2:]
            left_arr = arr[:len(arr)//2]
            
            #Divide
            merge_sort(right_arr)
            merge_sort(left_arr)
            
            #Merge
            i = 0 #left_arr index
            j = 0 #right_arr index
            k = 0 #merged arr idx
            #Considerem que els elements estan repartits de manera igual als dos arrays
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else: #Elements iguals o left_arr[i] > right_arr[j] 
                    arr[k] = right_arr[j]
                    j += 1
                
                k += 1
                
            #Imaginem que els elements més petits s'han guardat només en un array, 
            # no hi hauria cap element de l'altre array a la solucio final
            #Punter 'k' hauria incrementat, pero mínim un punter ('i' o 'j') no hauria incrementat,
            # El punter de l'array amb elements més grans no hauría incrementat
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1
                
        return arr          


    arr_test = [8,7,6,5,4,3,2,1]
    arr = merge_sort(arr_test)
    print(arr)

if __name__ == "__main__":
    main()