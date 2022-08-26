from turtle import position

def insertion(array):
    #start by looping through array beginning at index 1
    for index in range(1, len(array)):
        #assigns position to whatever current index already is 
        position = index
        #assigns value of index
        temp_value = array[index]
        #we check whether value to left of position is greater then temp value loop runs until we find a value that is less then
        #temp_value
        while position > 0 and array[position -1] > temp_value:
            #if value is greater we shift left value one cell to the right
            array[position] = array[position - 1]
            #decrement position by one
            position = position - 1
        #drops temp_value into the gap in the array
        array[position] = temp_value