import math


#class ArrayReader:

#  def __init__(self, arr):
#    self.arr = arr

#  def get(self, index):
#    if index >= len(self.arr):
#      return math.inf
#    return self.arr[index]

class Solution: # O(LogN) Time & O(1) Space. 
  def searchInfiniteSortedArray(self, reader, key):
    start, end = 0, 1
    while reader.get(end) < key:
      newStart = end 
      end += (end - start + 1) * 2
      start = newStart

    return self.binarySerach(reader, key, start, end)

  def binarySerach(self, reader, key, start, end):
    while start <= end: 
      middle = start + (end - start) // 2 
      if reader.get(middle) < key:
        start = middle + 1
      elif reader.get(middle) > key: 
        end = middle - 1
      else: 
        return middle
    return -1  

    
      
