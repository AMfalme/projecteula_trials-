def index_equals_value_search(arr):
  l, r = 0, len(arr)-1
  while l <= r:
    m = (l+r)//2
    if m == arr[m]:
      return m
    if arr[m] > m:
      r = m-1
    else:
      l = m+1
  return -1


def index_equals_value(arr):
  for i, v in enumerate(arr):
    if i == v:
      return i
  return -1


# print(index_equals_value_search([0,1,2,3]))




if 'i' in 'in':
  print('helo')