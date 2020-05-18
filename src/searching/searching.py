import time


def helper(message, value, sleep):
    print(message, value)
    time.sleep(sleep)


# * Returning the value...
# def linear_search(arr, target):
#     # Your code here
#     if not arr:
#         return -1
#     for num in arr:
#         helper("Number", num, 1)
#         helper("Target", target, 1)
#         if target == num:
#             helper("Match Value", num, 1)
#             return num
#     return -1   # not found

# * Returning the index...
def linear_search(arr, target):
    # Your code here
    if not arr:
        return -1

    for i in range(len(arr)):
        helper("Index", i, 1)
        helper("Target", target, 1)
        if arr[i] == target:
            helper("Match", arr[i], 1)
            return i
    return -1

# * Recursive binary search...
# ! Causes infinite loop with the tests, but runs fine here. Returns value instead of index of value.
# Write an iterative implementation of Binary Search

# def binary_search(arr, target):
#     if not arr:
#         return -1
#     # Your code here
#     else:
#         low = 0
#         helper("arr[lowest]", low, 1)
#         high = len(arr) - 1
#         helper("arr[highest]", high, 1)
#         mid = (high - low) // 2
#         helper("Mid", mid, 1)

#         if target == arr[mid]:
#             helper("match value", arr[mid], 1)
#             return mid
#         elif target < arr[mid]:

#             helper(f"{target} <", arr[mid], 1)
#             helper("arr[:mid] new arr is", arr[:mid], 1)
#             return binary_search(arr[:mid], target)
#         else:
#             helper(f"{target} >", arr[mid], 1)
#             helper("arr[mid:] new arr is", arr[mid:], 1)
#             return binary_search(arr[mid:], target)

#     return -1  # not found

# * Non-recursive binary search...


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# test = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
test = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# print(linear_search(test, -6))
print(binary_search(test, 3))
