def merge_sort(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list
  
   # Find the median and split
   median = len(unsorted_list) // 2
   left = unsorted_list[:median]
   right = unsorted_list[median:]

   left = merge_sort(left)
   right = merge_sort(right)
   return list(merge(left, right))

# Merge the two lists together
def merge(left,right):
   res = []
   while len(left) != 0 and len(right) != 0:
      if left[0] < right[0]:
         res.append(left[0])
         left.remove(left[0])
      else:
         res.append(right[0])
         right.remove(right[0])
   if len(left) == 0:
      res = res + right
   else:
      res = res + left
   return res
unsorted_list = [14,3,6,32,30,9,16,29]
print(merge_sort(unsorted_list))