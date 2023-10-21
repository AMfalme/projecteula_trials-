  # check if (mid_value == index) 
  # then return index
  # if (mid < index)
  #     
  #    index_equals_value_search(arr[mid: len(arr)])
  #  else: mid_value > index
  #     
  #     index_equals_value_search(arr[0: mid])
  #  return -1
  # [-8,0,1,2,4]
  # [0, 1,2,3,4]
  
  # [-1, 2, 3, 4, 5]
  # arr[0:2] = 
  # [ 0, 1, 2, 3, 4]
  
  # [-1, 2]
  # [ 0, 1]
  
  # [-1]
  # mid_point = 0, arr_len = 1, arr[1:1] => []
  
  # [-1]
  
  # [0,3]
  
  
  # [1, 2, 3, 4, 5]
  
  # [1], mid_point = 0, arr_len = 1, arr[0:0]
  
  # []
  
  
  arr_len = len(arr)
  mid_point = arr_len//2 #2
  # [-8,0,1,3, 5]
  # [-8,0,1,3,5]
  # [3, 5], 2 + 1 = 3
  if arr_len == 0:
    return -1
  value = arr[mid_point]
  if value == mid_point:
    return mid_point
  # arr.index(value)
  if value < mid_point:
    new_arr = arr[mid_point+1:arr_len]
    return index_equals_value_search(new_arr, mid_point)
  else:
    return index_equals_value_search(arr[0:mid_point])
  return -1
