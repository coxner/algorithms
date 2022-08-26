#bubble sort takes the greatest value in the list and ends it to the end of the array then the counter decreases and 
#keep looking through the array by one less value because we know that the end of the array is storing the max value

def bubble_sort(list):
    #keeps track of which index is still unsorted
    unsorted_until_index = len(list) - 1
    #keeps track if array is sorted or not
    sorted = False

    while not sorted:
        #if we get through the loop without if statement being invoked will know the list is fully sorted
        sorted = True
        #starts at beginning of array and goes until the index that has not been sorted
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                #changes back to false if a change in the array has to be made 
                sorted = False
                #swaps the values if i+1 is greater then i
                list[i], list[i+1] = list[i+1], list[i]
        # decreses the number of values unsorted since each time the loop runs one element is placed in its final position        
        unsorted_until_index = unsorted_until_index - 1
list = [65, 55, 45, 35, 25, 15, 5]
bubble_sort(list)
print(list)