"""
Given an array of positive numbers and a positive 
number 'k', find the  maximum sum of any 
contiguous subarray of size 'k'
"""


def maxSumSubArray(arr, k):
    position = 0
    maxSum = 0
    sum = 0
    for i, v in enumerate(arr):
        sum += v
        if i >= (k - 1):
            maxSum = max(maxSum, sum)
            sum -= arr[position]
            position += 1

    return maxSum


print(maxSumSubArray([2,1,5,1,3,2], 3))
print(maxSumSubArray([2, 3, 4, 1, 5], 2))
