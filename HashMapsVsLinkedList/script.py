from hashmap import HashMap
from linkedlist import LinkedList

N = 6
#note syntax we have to use for 2d array 
def first_linked_list(linked_list):
  current_node = linked_list.get_head_node()
  while current_node.get_value()[0] != "Zachary":
    current_node = current_node.get_next_node()
  return current_node.get_value()[1]

#Insert Data Into HashMap
my_hashmap = HashMap(N)
my_hashmap.assign("Zachary", "Sunburn Sickness")
my_hashmap.assign("Elise", "Severe Nausea")
my_hashmap.assign("Mimi", "Stomach Flu")
my_hashmap.assign("Devan", "Malaria")
my_hashmap.assign("Gary", "Bacterial Meningitis")
my_hashmap.assign("Neeknaz", "Broken Cheekbone")

#Insert Data into LinkedList
my_linked_list = LinkedList(["Zachary", "Sunburn Sickness"])
my_linked_list.insert_beginning(["Elise", "Severe Nausea"])
my_linked_list.insert_beginning(["Mimi", "Stomach Flu"])
my_linked_list.insert_beginning(["Devan", "Malaria"])
my_linked_list.insert_beginning(["Gary", "Bacterial Meningitis"])
my_linked_list.insert_beginning(["Neeknaz", "Broken Cheekbone"])

#Get Zachary's Disease from a HashMap
hashmap_zachary_disease = my_hashmap.retrieve("Zachary") #Checkpoint 1
print("Zachary's disease is {0}".format(hashmap_zachary_disease))
hashmap_runtime = "1" #Checkpoint 2
print("The runtime of retrieving a value from a hashmap is O({0})\n\n".format(hashmap_runtime))


#Get Zachary's Disease from a Linked List
#Write Code here for Checkpoint 3
linked_list_zachary_disease = first_linked_list(my_linked_list)
print("Zachary's disease is {0}".format(linked_list_zachary_disease))
linked_list_runtime = "N" #Checkpoint 4
print("The runtime of retrieving the first value added to a linked list is O({0})\n\n".format(linked_list_runtime))

