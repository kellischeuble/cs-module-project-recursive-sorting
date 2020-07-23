# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # Get the total number of elements
    elements = len(arrA) + len(arrB)
    # Create an array filled with 'elements' number of 0s
    merged_arr = [0] * elements

    # Your code here
    a_end = len(arrA)
    b_end = len(arrB)

    # Index tracker variables
    a_idx = 0
    b_idx = 0
    main_idx = 0

    # while we're not at the end of arrA or arrB
    while a_idx < a_end and b_idx < b_end:
        # If the left most value at arrA is less than the left most value at
        # arrB
        if arrA[a_idx] <= arrB[b_idx]:
            # Overwrite the 0 in the main array with arrA's value
            merged_arr[main_idx] = arrA[a_idx]

            # Increment the index trackers
            a_idx += 1
            main_idx += 1
        else:
            # Otherwise, overwrite the 0 in the main array with arrB's value
            merged_arr[main_idx] = arrB[b_idx]

            # Increment the index trackers
            b_idx += 1
            main_idx +=1

    # If we're at the end of arrB but not at the end of arrA
    while a_idx < a_end:
        merged_arr[main_idx] = arrA[a_idx]
        a_idx += 1
        main_idx += 1

    # If we're at the end of arrA but not at the end of arrB
    while b_idx < b_end:
        merged_arr[main_idx] = arrB[b_idx]
        b_idx += 1
        main_idx += 1


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    arr_size = len(arr)

    if arr_size < 2:
        return arr

    mid = arr_size // 2

    sortedLeft = merge_sort(arr[:mid])
    sortedRight = merge_sort(arr[mid:arr_size+1])

    return merge(sortedLeft, sortedRight)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1

    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]):
        return

    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end):

        # If element 1 is in right place 
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers 
            start += 1
            mid += 1
            start2 += 1
    return arr

def merge_sort_in_place(arr, l, r):
        if (l < r):
            mid = (l + r) // 2

            merge_sort_in_place(arr, l, mid)
            merge_sort_in_place(arr, mid + 1, r)
            merge_in_place(arr, l, mid, r)
        return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
