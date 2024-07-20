class Solution: # O(LogN) Time & O(1) Space. 
  def search(self,arr, key):
    start = 0 
    end = len(arr) - 1
    ascending = arr[start] < arr[end]
    while start <= end: 
      middle = end - start // 2
      if arr[middle] == key:
        return middle

      if ascending: 
        if key < arr[middle]:
          end = middle - 1
        else: 
          start = middle + 1
      else: 
        if key < arr[middle]:
          start = middle + 1
        else: 
          end = middle - 1 
      
    return -1  # element not found