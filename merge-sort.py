#recursivly (call stack) breaks down input list until it only has one element it then joins that single element with another element to create
# a two element list it then joins that element with another 2 elements to create a 4 element list and so on.
def merge_sort(items):
  # our recursive case  
  if len(items) <= 1:
    return items
  #finding the middle index and splitting our array
  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]
  # recursivly calling merge_sort on are split arrays
  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)
  #merge the arrays and return them 
  return merge(left_sorted, right_sorted)

# orders broken down list
def merge(left, right):
  result = []
  #while left and right have elements
  while (left and right):
    #comparison the determine which element we want to add to our array add left[0] if it is smaller or add right[0] if it is smaller
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  if left:
    result += left
  if right:
    result += right

  return result

unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print(ordered_list1)
print(ordered_list2)
print(ordered_list3)