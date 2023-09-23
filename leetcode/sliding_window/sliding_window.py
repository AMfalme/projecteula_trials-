"""
    Given an array of integers k and threshold,
    return the number of sub-arrays of size k 
    and average greater than or equal to threshold.

    Input: = arr = [2, 2, 2, 2, 5, 5, 5, 8], k = 3,  threshold = 4
    [
        [2,2,2], 6/3 = 2
        [2,2,2], 6/3 = 2
        [2,2,5], 9/3 = 3 
        [2,5,5], 12/3 = 4 (+1)
        [5,5,5], 15/3 = 5 (+1)
        [5,5,8], 18/3 = 6 (+1)
    ]

    Output -> 4
"""


def num_of_subarrays(arr, k, threshold):
    sum = 0
    counter = 0
    window_position = 0
    
    for i, v in enumerate(arr):
        sum += v
        
        if i > k:
            sum -= arr[window_position]
            window_position += 1
            avg =sum/k 
            if avg >= threshold:
                counter += 1
    return counter

print(num_of_subarrays([2, 2, 2, 2, 5, 5, 5, 8], k = 3,  threshold = 4))

print(num_of_subarrays([11, 13, 17, 23, 29, 33, 7, 5, 2, 3], k = 3,  threshold = 5))