//similar to bubble sort but we start by finding the smallest value of the array and moving it to the front

function selectionSort(array) {
    //outer loop for passthrough
    for(var i = 0; i < array.length; i++) {
        //lowest index we've encountered so far
        var lowestNumberIndex = i;
        //inner loop that starts at i+1
        for(var j = i +1; j < array.length; j++){
            //checks each element of the array that has yet to be sorted and looks for the lowest number 
            if(array[j] < array[lowestNumberIndex]){
                lowestNumberIndex = j;
            }
        }
        // checks if the lowest number is already in its correct place in the array if not it adds it there
        if(lowestNumberIndex != i) {
            var temp = array[i];
            array[i] = array[lowestNumberIndex];
            array[lowestNumberIndex] = temp;
        }
    }
    return array;
}