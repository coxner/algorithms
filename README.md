# algorithms

## Jump Around
- [Sorting Algorithms](#sorting-algorithms)
  - [Bubble Sort](#bubble-sort)
  - [Merge Sort](#merge-sort)
  - [Quicksort](#quicksort)
- [Trees](#trees)
- [Files](#Files)


## Pattern Searching

Pattern searching is a short but somewhat complex algoritm used to scan a group of text for a particular pattern. Not the most efficent because for every character in the original text we must compare it with the pattern. It has a asymptotic notation of 0(nk). 

Naive pattern search is a simple way to systemically look through a text for a given pattern. This algorithm iterates over each character in a text and then counts the following number of matching characters to find the pattern. It is preferred for its simplicity and ease of implementation, allowing it to easily be modified for other purposes.

## Sorting Algorithms

## Asymptotic Notation

A general way to caculate a programs runtime is known as asymptotic notation. Caculated by looking at how many instructions the computer has to perform based on the number of inputs known as n. Can also use this to caculate the space a certain program will need. 

![comparisons img](https://github.com/coxner/algorithms/blob/master/img/notation-comparison.png)


### Bubble Sort

Sorting algorithm that has two pointers one left pointer and one right pointer. The algorithm swaps elements of an array torwards the beginning of the array or torwards the end. Think of an array **[2,4,7,1,3]** the left pointer would start on 2 and the right pointer on 4. If the value of the left pointer is greater then the value of the right pointer we swap them. After one pass through our array would look like this **[2,4,1,3,7]**. The logic behind a bubble sort is each time the function runs one value in the array will be placed in its final position at the beginning or end of the array. Above we can see **7** has reached its final spot. If loop ran one more time we would get **[2,1,3,4,7]** now **4,7** are in there final positions within the array. 

#### Efficiency 
Two steps in bubble sort:
  Comparisons: two numbers compared with one antoher.
  Swaps: two numbers are swapped with one another.
  
In data terms we make **(N-1) + (N-2) + (N-3)...** comparisons each time the function is run. With an array containing 10 elements and assuming the worst case scenario we would make 45 comparisons and another 45 for swaps. 

If we look at the growth of N = 10 and # of steps equals 90 we can assume a growth of N^2. In big O notation we would say bubble sort has a effiency of **O(N^2)**

Bubble sort can be viewed [here](https://github.com/coxner/algorithms/blob/master/bubbleSort.py)

### Merge Sort

Divide and conquer algorithm, data is continually broken down into smaller elements until sorting them becomes really simple. 

Two Steps:

  Splitting the data into runs (smaller components)
  Re-combining runs into sorted list known as the merge
  
The splitting works in a recuring fashion. We split the data input to the function in half. We then call the sort on each of those halves which makes them in quarters. The sort then splits the quarters in half this recursive call occurs until all data elements are contained in there own list. After this takes place we begin merging the list. When we begin merging the list we do it by making two element list with the smaller number followed by the larger number. 

#### Merging

Merging works by calling two list we will refer to them as left and right. They are both already sorted. We want to combine into a larger list which we will refer to as both. We will iterate through both list with left_index and right_index. Compare left and right index smaller of two is the first element of both. We increment the index that the smallest # came from and keep comparing left and right to find the second value and so on. Once on list is exausted we know the elements of the remaining list go at the end of the list both. When we have two arrays that are already sorted we only need a pointer at the start of the array.


Merge sort can be viewed [here](https://github.com/coxner/algorithms/blob/master/merge-sort.py)

![merge-sort](https://github.com/coxner/algorithms/blob/master/img/merge-sort.png)


### Quicksort

Recursive algorithm done with comparison sort using > and <. Uses divide and conquer strategy dividing the problem into smaller sub problems. Break list down until we have sub arrays with at most one element. Select a pivot value and every other element is compared to the pivot value. We end up getting a sub array of values smaller then the pivot, the pivot itself, a subarray of elements greater then the pivot. Process is repeated on subarrays until they contain 0 or 1 element. Smaller then array is never compared to the larger then array. 

Quicksort is an unusual algorithm in that the worst case runtime is O(N^2), but the average case is O(N * logN). 

Logic: 
  1. Set comparison value to the end of the list
  2. The left pointer continuously moves one cell to the right until it reaches a value that is greater then or equal to the pivot then stops.
  3. The right pointer continuously moves one cell left until it reaches a value that is less than or equal to pivot then stops. 
  4. Swap values left and right pointer is pointing to
  5. Process continues until pointers are pointing to the same value or the left pointer has moved right of the right pointer 
  6. Finally swap pivot with value left pointer is currently pointing to 
  

Quicksort can be viewed [here](https://github.com/coxner/algorithms/blob/master/quicksort.py)


## Brute Force Algorithms 

Slower but easier to implement. Goes through every possible choice one by one until a solution is found. Rely on counting power to solver problems. Bubble sort and selection sort can be considered brute force algorithms. Time complexity is usually proportional to the size of input data meaning 0(n). Algorithms are slow and should not be used in real-world problems. Are linear problems that will involve code with a for loop to iterate through values and a if statement to check if the target value is equal to the value we are searching the array for. 

![brute-force](https://github.com/coxner/algorithms/blob/master/img/brute-force.png)


## Trees

Structure of a tree can be viewed here. Node based data structure where each node can have links to multiple nodes. Follow a complexity of 0(log N)

![tree-structure](https://github.com/coxner/algorithms/blob/master/img/trees.png)

A simple project built using the tree data structure can be viewed [here](https://github.com/coxner/algorithms/blob/master/treeNodeProject.py)




!!!! REVIST !!!
One of the more common trees are binary trees which follow the following rules.
  - Each node has zero, one or two children
  - If a node has two children it must have one child that is less then the parent and one child that is greater then the parent.
 
 Algorithm for a tree works in the following way.
  - Check the root node
  - If value is found exit 
  - If value is less the the root node search the left subtree
  - If the value is greater search the right subtree 
 
 
 
## Heaps 

Used to maintian a max or min value in a dataset and do so by creating a priority queue. 

A max-heap can be considered a binary tree with two qualities.
  - Root is the max value of the data set
  - Every parent is greater then its child

###### Tree Index Formula 

Here is the formula for caculating the index of a max-heap tree. The index is the formula is refering to the parent index and that is used to caculate the childs index
  - Left Index: (index * 2) + 1
  - Right Index: (index * 2) + 2
  - Parent Index: (index - 1) / 2

![tree-index](https://github.com/coxner/algorithms/blob/master/img/max-heap.png)

!! This structure can be different for every algorithm is not a set practice !!

###### Heapify 

Add an element to the bottom of the tree from there it starts bumping up the node until the trees structure is properly restored. 

###### Heapsort

Heapsort is an algorithm that sorts an array from extracting the root of a heap data structure. It is a time efficent algorithm that has a time complexity of 0(log n). 

Here is how the algorithm works.
  - Build a max heap to store data from a unsorted list
  - Extract the root (larges heap value) and place it into a sorted array
  - Replace the root with the last element of the list then re balance the tree
  - Once the max-heap is empty return the sorted list

Heapsort code can be viewed [here](https://github.com/coxner/algorithms/blob/master/heapsort/max_heap.py) and the implementation of it in a program can be viewed [here](https://github.com/coxner/algorithms/blob/master/heapsort/script.py)


