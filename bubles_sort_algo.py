def bubblesort(list):

# Swap the elements to arrange in order
   for itr in range(len(list)-1,0,-1):
      for indx in range(itr):
         if list[indx]>list[indx+1]:
            temp = list[indx]
            list[indx] = list[indx+1]
            list[indx+1] = temp
list = [14,11,4,16,77,34,22,25]
bubblesort(list)
print(list)

