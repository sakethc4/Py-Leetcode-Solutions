class Solution: # LogN Time & O(1) Space. 
  def searchCeilingOfANumber(self, arr, key):
    n = len(arr)
    if key > arr[n - 1]:
      return -1

    start, end = 0, n - 1
    while start <= end: 
      middle = end - start // 2 
      if key < arr[middle]: 
        end = middle - 1 
      elif key > arr[middle]: 
        start = middle + 1
      else: 
        return middle 

    return start 
    
    # [1, 3, 8, 10, 15]