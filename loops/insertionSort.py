import array

def main():

    arr = [7,12,8,5]
    insertion_sort(arr)
    print("Sorted array:", arr)

def insertion_sort(A):
    for j in range (1, len(A)):
        key = A[j]
        i  = j - 1 
        while i >= 0 and A[i] > key: 
            A[i+1] = A[i]
            i= i - 1
        #end while
        A[i+1] = key
    #end for
    return A

main()





