# Function to create an empty list
def create_an_empty_list():
    return []

# Function to create a list with four elements
def create_a_list():
    return [1, 2, 3, 4]

# Function to add an element to the end of a list
def add_element_to_end_of_list(lst, element):
    lst.append(element)
    return lst

# Function to add an element to the start of a list
def add_element_to_start_of_list(lst, element):
    lst.insert(0, element)
    return lst

# Function to remove the last element from a list
def remove_element_from_end_of_list(lst):
    lst.pop()
    return lst

# Function to remove the first element from a list
def remove_element_from_start_of_list(lst):
    del lst[0]
    return lst

# Function to retrieve the first element from a list
def retrieve_first_element_from_list(lst):
    return lst[0]

# Function to retrieve an element from a specific index in a list
def retrieve_element_from_index(lst, index):
    return lst[index]

# Function to retrieve the last element from a list
def retrieve_last_element_from_list(lst):
    return lst[-1]
