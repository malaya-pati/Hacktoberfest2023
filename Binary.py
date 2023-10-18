def binary_search(arr, target):
    """
    Perform binary search to find the target in a sorted array.

    Parameters:
    arr (list): A sorted list of elements.
    target: The target element to search for.

    Returns:
    int: Index of the target element in the array if found, -1 otherwise.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
sorted_array = [2, 5, 7, 12, 16, 23, 38, 45, 56]
target_value = 16

result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}.")
else:
    print(f"Element {target_value} not found in the array.")
