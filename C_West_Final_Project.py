"""C_West_Final_Project.py
West C
This program involves garden information for a community garden.
"""
import string # imports the Python string module.

#print("This program collects information about your garden.\n")
print("This program collects information and helps to manage a community garden.\n") 

#Creating lists.
inventory_flowers = ["rose", "dahlia", "scotch broom", "daffodil"] 
inventory_garden = ["tomato", "zucchini", "carrot"] 

# This is an example of basic testing of the code as it is developing.
#total_list = inventory_flowers + inventory_garden 
#print(f"Total defined list:  {total_list}\n")

total_list = inventory_flowers + inventory_garden
print(f"Current plants grown in the garden:  {total_list}\n")

def get_value_flower_input():
    ''' This function asks for user input for a flower and verifies that it is an alphabetic entry, given three tries.'''
    tries = 3
    while tries > 0:
        user_input_flower = input ("Enter one flower to grow in the garden: ").lower() # ensures user input is lower case
        if user_input_flower.isalpha(): # ensures the user input is alphabetical
            return user_input_flower
        else:
            print("This is an incorrect entry, please try again.")
            tries -= 1
    print("Incorrect entry, this program will end.")
    return None
user_input_flower = get_value_flower_input()

if user_input_flower:
    #inventory_flowers.append("sunflower") # append item to the end of the list. # PROJECT 5
    inventory_flowers.append(user_input_flower) # append the user input flower to the end of the list.
    #print (f"Appended -Sunflower- and User_Input_Flower at end:  {inventory_flowers}\n") # PROJECT 5
    print (f"You chose a new plant to add to this garden.  The new list of flowers is:  {inventory_flowers}\n")

    # this will index one item from the flowers list.
    print (f"Flowers to erradicate from the garden:  {inventory_flowers[2]}\n")

    #inventory_flowers.remove ("scotch broom") # will remove the plant scotch broom from the flowers list. # PROJECT 5
    #print (f"Remove -Scotch Broom- from the flower list:  {inventory_flowers}\n")

    #inventory_garden.extend (["green bean", "pumpkin", "squash"]) # extend adds a whole list to the garden list individually. #PROJECT 5
    #print (f"Append a list to the end of the garden list:  {inventory_garden}\n")

    inventory_garden.extend (["green bean", "pumpkin", "squash"]) # extend adds a whole list to the garden list individually.
    print (f"This gardening season will also add to the garden:  {inventory_garden}\n")

    tree_Tuple = ("apple", "plum", "cherry") # Tuple list that will remain unchanged.
    print (f"The trees currently grown in this garden are: {tree_Tuple}\n")

    """Since the tree_Tuple should be included with the rest of the list.  This converts the Tuple into a list first.
    Other wise the Tuple would not work for the following code to be included with the other lists.  
    This conversion makes the program more understandable for the user."""
    tree_list = list(tree_Tuple)
    total_complete_list = inventory_flowers + inventory_garden + list(tree_list)
    #print (f"Total Complete List: , {total_complete_list}\n") # this will print all the lists together.

    # sorted(total_complete_list) # this is where the list can be sorted alphabetically. # PROJECT 5
    #total_complete_list.sort()
    #print("Total Complete List (sort, remove quotes, add commas): ", ", ".join (total_complete_list))

    # Complete list of plants and trees grown in the garden and sorted alphabetically
    total_complete_list.sort()
    print("The complete list of plants and trees grown in this garden are: ", ", ".join (total_complete_list))

    #total_complete_list.reverse() # PROJECT 5
    #print("Total Complete List in reverse order (remove quotes, add commas): ", ", ".join (total_complete_list))

def total_count_plants():
    """This function counts the different types of plants in the garden, both individually and then concatenated as a total."""
    count_inventory_flowers = len(inventory_flowers)
    count_inventory_garden = len(inventory_garden)
    count_tree_Tuple =  len(tree_Tuple)
    total_type_plants = count_inventory_flowers + count_inventory_garden + count_tree_Tuple
    return total_type_plants

total_plants_count = total_count_plants()

print (f"Number of types of flowers in the garden:  {len(inventory_flowers)}")
print (f"Number of types of vegetables in the garden:  {len(inventory_garden)}")
print (f"Number of fruit trees in the garden:  {len(tree_Tuple)}")
print (f"Total count of types of plants in the garden:  {total_plants_count}")
print (f"Enjoy gardening this season!")

z = input ("Pause, CWest")