# Define your "TreeNode" Python class below
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  #adding a child to the tree with the array children  
  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)

  #code to remove a child from the tree  
  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    #list comprehension for code below
    self.children = [child for child in self.children if child != child_node]
    #new_children = []
    #for child in self.children:
    #  if child != child_node:
    #    new_children.append(child)
    #self.children = new_children
  #Go through the list and print the values not self.value returns the valeu of rooot node
  def traverse(self, nodes_to_visit):
    #new list to go through to print values
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0 :
      #remove item from list so we dont have a infinite loop
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      #adds children of current node to nodes_to_visit list
      #NOTE append will only add one item to the list while += will copy all elements to the list
      nodes_to_visit += current_node.children

root = TreeNode("I am Root")
child = TreeNode("A wee sappling")
bad_seed = TreeNode("Root Rot!")

root.add_child(child)
root.add_child(bad_seed)

root.remove_child(bad_seed)
