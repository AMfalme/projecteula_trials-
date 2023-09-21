"""
Given an array,
find the average of all contiguous
subarrays of size "K" in it.


Input: Arr = [1, 3, 2, 6, -1, 4, 1, 8,2]
 k = 5
 sub_arr1 = [1, 3, 2, 6, -1] avr = sub_arr1/5 = 2.2
 sub_arr2 = [3, 2, 6, -1, 4] avr = sub_arr2/5 = 2.8
 sub_arr3 = [2, 6, -1, 4, 1] avr = sub_arr3/5 = 2.4
 sub_arr4 = [6, -1, 4, 1, 8] avr = sub_arr4/5 = 3.6
 sub_arr5 = [-1, 4, 1, 8, 2] avr = sub_arr5/5 = 2.8
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""


def average_of_subarray_of_size_k(arr, k):
    
    '''

    Solution 1: 0(n*k)

        double[] result = new double[arr.length - k + 1];
        for (int i = 0; i < arr.length - k; i ++) {
            double sum = 0;
            for (int j = i; j < i + k; j ++) {
                    sum += arr[j];
                }
            result[i] = sum / k;
        }
        return result;
    '''
    results = [] # [arr.length - K + 1]    
    
    for i, v in enumerate(arr[:k]):
        sum = 0
        results.append([])
        
        for j, value in enumerate(arr[i:i+k]):
            sum += value
        avr = sum / k
            
        results[i] = avr
    return results

print(average_of_subarray_of_size_k([1, 3, 2, 6, -1, 4, 1, 8,2], 5))