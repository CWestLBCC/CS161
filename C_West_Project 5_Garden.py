"""Project 5
West C
This program involves garden information.
"""
import string # imports the Python string module.

print("This program collects information about your garden.\n")

inventory_flowers = ["rose", "dahlia", "scotch broom", "daffodil"] # this line creates the list.
inventory_garden = ["tomato", "zucchini", "carrot"] # another list.

total_list = inventory_flowers + inventory_garden
print(f"Total defined list:  {total_list}\n")

# this asks for user input for a flower and verifies that its alphabetic entry, given three tries.
def get_value_flower_input():
    tries = 3
    while tries > 0:
        user_input_flower = input ("Enter one flower to grow in the garden: ") 
        if user_input_flower.isalpha():
            return user_input_flower
        else:
            print("This is an incorrect entry, please try again.")
            tries -= 1
    print("Incorrect entry, this program will end.")
    return None
user_input_flower = get_value_flower_input()

if user_input_flower:
    inventory_flowers.append("sunflower") # append item to the end of the list.
    inventory_flowers.append(user_input_flower) # append the user input flower to the end of the list.
    print (f"Appended -Sunflower- and User_Input_Flower at end:  {inventory_flowers}\n")

    # this will index one item from the flowers list.
    print (f"Flowers to erradicate from the garden:  {inventory_flowers[2]}\n")

    inventory_flowers.remove ("scotch broom") # will remove the plant scotch broom from the flowers list.
    print (f"Remove -Scotch Broom- from the flower list:  {inventory_flowers}\n")

    inventory_garden.extend (["green bean", "pumpkin", "squash"]) # extend adds a whole list to the garden list individually.
    print (f"Append a list to the end of the garden list:  {inventory_garden}\n")

    hardscape_Tuple = ("apple", "plum", "cherry") # Tuple list that will remain unchanged.
    print (f"The hardscapes currently grown in this garden are: {hardscape_Tuple}\n")

    """If I wanted to include the hardscape_Tuple into the rest of the list I would convert the Tuple into a list first.
    Other wise the Tuple would not work for the following code to be included with the other lists."""
    hardscape_list = list(hardscape_Tuple)
    total_complete_list = inventory_flowers + inventory_garden + list(hardscape_list)
    print (f"Total Complete List: , {total_complete_list}\n") # this will print all the lists together.

    # sorted(total_complete_list) # this is where the list can be sorted alphabetically.
    total_complete_list.sort()
    print("Total Complete List (sort, remove quotes, add commas): ", ", ".join (total_complete_list))

    total_complete_list.reverse()
    print("Total Complete List in reverse order (remove quotes, add commas): ", ", ".join (total_complete_list))

def total_count_plants():
    """This function counts the different types of plants in the garden, both individually and then concatenated as a total."""
    count_inventory_flowers = len(inventory_flowers)
    count_inventory_garden = len(inventory_garden)
    count_hardscape_Tuple =  len(hardscape_Tuple)
    total_type_plants = count_inventory_flowers + count_inventory_garden + count_hardscape_Tuple
    return total_type_plants

total_plants_count = total_count_plants()

print (f"Number of types of flowers in the garden:  {len(inventory_flowers)}")
print (f"Number of types of vegetables in the garden:  {len(inventory_garden)}")
print (f"Number of fruit trees in the garden:  {len(hardscape_Tuple)}")
print (f"Total count of types of plants in the garden:  {total_plants_count}")

z = input ("Pause, CWest")