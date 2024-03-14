
def partition(arr, left, right):
    # Choose the pivot element
    pivot = arr[right]
    i = left - 1

    # Partition the array into elements <= pivot and elements > pivot
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            # Swap elements arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot element in its correct position
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def kth_order_statistic(arr, left, right, k):
    if left == right:
        # If the array has only one element, return it
        return arr[left]

    # Partition the array and get the pivot index
    pivot_index = partition(arr, left, right)

    if k == pivot_index:
        # If k matches the pivot index, return the kth order statistic
        return arr[pivot_index]
    elif k < pivot_index:
        # If k is less than the pivot index, search in the left subarray
        return kth_order_statistic(arr, left, pivot_index - 1, k)
    else:
        # If k is greater than the pivot index, search in the right subarray
        return kth_order_statistic(arr, pivot_index + 1, right, k)

'''
# Input: Read the array and k
arr = list(map(int, input().split()))
k = int(input())

# Find kth order statistic
result = kth_order_statistic(arr, 0, len(arr) - 1, k - 1)

# Output: Print the kth order statistic
print(result)
'''

# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low
#     for j in range(low+1, high+1):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i], arr[low] = arr[low], arr[i]
#     return i

# def kth_smallest(arr, l, h, k):
#     if l <= h:
#         pivotIndex = partition(arr, l, h)
#         if pivotIndex == k - 1:
#             return arr[pivotIndex]
#         elif pivotIndex > k - 1:
#             return kth_smallest(arr, l, pivotIndex - 1, k)
#         else:
#             return kth_smallest(arr, pivotIndex + 1, h, k)
#     return None

# def main():
#     # Reading input
#     numbers = list(map(int, input().split()))
#     k = int(input())

#     # Finding kth smallest value
#     result = kth_smallest(numbers, 0, len(numbers)-1, k)
#     print(result)

# if __name__ == "__main__":
#     main()

def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Merging the sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def find_kth_smallest_via_mergesort(arr, k):
    merge_sort(arr)
    return arr[k-1]  # since array indexing is zero-based

def main():
    # Example usage
    arr = [2, 8, 3, 7, 4, 6, 5]
    k = 4
    kth_smallest_element = find_kth_smallest_via_mergesort(arr, k)
    print(f"The {k}th smallest element is:", kth_smallest_element)

    # Using kth_order_statistic to find the kth smallest element
    # Note: This requires the original, unsorted array, so we redefine it

    arr = [2, 8, 3, 7, 4, 6, 5]
    kth_smallest_element = kth_order_statistic(arr, 0, len(arr) - 1, k - 1)
    print(f"The {k}th smallest element is:", kth_smallest_element)

if __name__ == "__main__":
    main()
