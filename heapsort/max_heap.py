class MaxHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  #method to check if a node has a child
  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count

  
  # add a node to the tree 
  def add(self, element):
    #increase count of nodes by 1
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    #adds element 
    self.heap_list.append(element)
    #call heapify_up to find out where the node should be placed
    self.heapify_up()
    
  def heapify_up(self):
    print("Heapifying up")
    #sets the idx to the last element in the tree which is where the item we just appened is at
    idx = self.count
    #while the element has a parent
    while self.parent_idx(idx) > 0:
      #set child and parent elements notice how parent uses the helper method
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      #if out parent value is less then our child values we then swap them
      if parent < child:
        print("swapping {0} with {1}".format(parent, child))
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      #set the idx of the value we swapped to the parent idx  
      idx = self.parent_idx(idx)
    print("Heap Restored {0}".format(self.heap_list))
  
  # this method swaps the first and last element, removes and returns the largest value and rebalances the heap
  def retrieve_max(self):
    #base case if there is nothing in heap it is empty
    if self.count == 0:
      print("No items in heap")
      return None
    # max value is the element at index 1 of the list  
    max_value = self.heap_list[1]
    print("Removing: {0} from {1}".format(max_value, self.heap_list))
    #Swaps the first and last value of the heap
    self.heap_list[1] = self.heap_list[self.count]
    #decrease the size of the heap before we remove a value
    self.count -= 1
    #pop() removes the last value since we swapped it we are removing the max value of the heap
    self.heap_list.pop()
    print("Last element moved to first: {0}".format(self.heap_list))    
    # call heapify_down() to rebalance the heap
    self.heapify_down()
    return max_value

  #method to move a node down the heap
  def heapify_down(self):
    idx = 1
    #while the head node has a child
    while self.child_present(idx):
      print("Heapifying down!")
      #gets the largest value of the max-heaps[1] node
      larger_child_idx = self.get_larger_child_idx(idx)
      #assigns child and parent variables
      child = self.heap_list[larger_child_idx]
      parent = self.heap_list[idx]
      # if the parent value is less then the child
      if parent < child:
        self.heap_list[idx] = child
        self.heap_list[larger_child_idx] = parent
      #used to terminate loop  
      idx = larger_child_idx
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("") 

  #helper method used for heapify_down to help us find the larger child when moving down a heap
  def get_larger_child_idx(self, idx):
    #if the right child_idx is greater then count then we know there is no right child and only a left one
    if self.right_child_idx(idx) > self.count:
      print("There is only a left child")
      return self.left_child_idx(idx)
    else:
      #else we assign the values of the left and right child 
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      # we check the values of the left and right child to see which one is larger for when we heapify_down
      if left_child > right_child:
        print("Left child "+ str(left_child) + " is larger than right child " + str(right_child))
        return self.left_child_idx(idx)
      else:
        print("Right child " + str(right_child) + " is larger than left child " + str(left_child))
        return self.right_child_idx(idx)


