def selection_sort(input_list):
   for indx in range(len(input_list)):
      min_indx = indx
      for j in range(indx +1, len(input_list)):
         if input_list[min_indx] > input_list[j]:
             min_indx = j
   # Swap values in favor of min value
   input_list[indx], input_list[min_indx] = input_list[min_indx], input_list[indx]
l = [19,4,78,98,77]
selection_sort(l)
print(l)