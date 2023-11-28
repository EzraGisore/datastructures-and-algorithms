##timsort
list =[1,5,6,2,7,9,8,0]
list.sort()
print(list)

list2 =[9,7,6,8,5,3,2,4,0,1]
sorted_list2 = sorted(list2)
print(sorted_list2)

##merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) //2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        ##merge sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

mylist = [5,9,7,4,2,8,1,0,3,6]
result = merge_sort(mylist.copy()) ##make a copy to keep the original
print(result)
##Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
my_list = [5,9,7,4,2,8,1,0,3,6]
result1 = merge_sort(my_list.copy()) ##make a copy to keep the original
print(result1)
##HeapSort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    #build a max heap
    for i in range(n //2 - 1, -1, -1):
        heapify(arr, n, i)
    #extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] #swap
        heapify(arr, i, 0)
my_list1 = [5,9,7,4,2,8,1,0,3,6]
heap_sort(my_list1)
print(my_list1)
##BubbleSort
def bubble_sort(arr):
    n = len(arr)
    #traverse through all array elements
    for i in range(n):
        #flag to optimize if inner loop does not swap any elements
        swapped = False

        # last i elements are already in place
        for j in range(0, n - 1 - 1):
            #swap if element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # if no two elements were swapped in the inner loop, the array is already sorted.
        if not swapped:
            break
my_list2 = [5,9,7,4,2,8,1,0,3,6]
bubble_sort(my_list2)
print(my_list2)
##SelectionSort - selects minimum or maximum element from the unsorted portion and swaps it with the element at the beginning of the unsorted portion.
def selection_sort(arr):
    n = len(arr)
    #traverse through all array elements
    for i in range(n):
        #find the minimum element in unsorted portion
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        #swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

my_list3 = [5,9,7,4,2,8,1,0,3,6]
selection_sort(my_list3)
print(my_list3)

