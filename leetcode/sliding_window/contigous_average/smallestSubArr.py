"""
    Given an array of positive numbers and a positive
    number 'S'; find the length of the smallest contiguous
     subarray whose sum is greater than or equal to 'S'.
     Return 0 if no such subArray exists. 
"""


def smallestSubArr(arr, S):
    minLen = 100000000000
    position = 0
    sum = 0
    for i, v in enumerate(arr):
        sum += v
        while sum >= S:
            minLen = min(minLen,i-position +1)
            sum -= arr[position]
            position += 1

    if( minLen == 100000000000 ): 0
    return minLen

print(smallestSubArr([2,1,5,2,3,2],7))
print(smallestSubArr([2, 1, 5, 2, 8], 7))