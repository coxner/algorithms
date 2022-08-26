#binary search is much faster then linear search each time the loop runs estimates elimate half of the potential cells
#values could be contained in 

def binary_search(array, value):
    #establish lower and upper bounds of where value we are searching for could be
    lower_bound = 0
    upper_bound = array.length() - 1

    #loop that keeps inspecting the middlemost value
    while lower_bound <= upper_bound:
        #caculate the middle point of the array
        midpoint = (lower_bound + upper_bound) / 2
        #find mid_point value
        value_at_midpoint = array[midpoint]
        #if value we are looking for = midpoint loop is done if not we change the lower bound to either guess higher or lower
        if value < value_at_midpoint:
            #if value is less then midpoint value we re assign the upperbound -1 is because we know it is not the middle value
            upper_bound = midpoint -1 
        elif value > midpoint :
            #if value is greater then midpoint we re assign the lower value
            lower_bound = midpoint + 1
        elif value == midpoint :
            return midpoint 
    #loop needs to be edited to return null if the value is not found         
    return array[value]
