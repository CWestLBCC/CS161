"""Project 6
West C
This program involves garden information.
"""

# Source:  https://www.w3schools.com/python/python_dictionaries.asp
def create_garden_dict():
    """This function creates a dictionary of garden items."""
    garden_dict = {
        "flowers": ["rose", "dahlia", "scotch broom", "daffodil"],
        "vegetables": ["tomato", "zucchini", "carrot"],
        "fruits": ["apple", "plum", "cherry"]
    }
    return garden_dict

def add_data(garden_dict, category, data):
    """This function adds more data to the garden dictionary."""
    if category in garden_dict:
        garden_dict[category].append(data)
    else:
        print(f"Category '{category}' does not exist in the garden dictionary.")

def change_value(garden_dict, category, old_data, new_data):
    """This function changes a value that is associated with a key in teh dictionary."""
    if category in garden_dict:
        if old_data in garden_dict[category]:
            index = garden_dict[category].index(old_data)
            garden_dict[category][index] = new_data
        else:
            print(f"'{old_data}' does not exist in the '{category}' category.")
    else:
        print(f"Category '{category}' does not exist in the garden dictionary.")

def remove_data(garden_dict, category, data):
    """Function to remove data from the garden dictionary"""
    if category in garden_dict:
        if data in garden_dict[category]:
            garden_dict[category].remove(data)
        else:
            print(f"'{data}' does not exist in the '{category}' category.")
    else:
        print(f"Category '{category}' does not exist in the garden dictionary.")

def index_dictionary(garden_dict, category, index):
    """Function to index the dictionary to find some value stored at the key within it."""
    if category in garden_dict:
        if index < len(garden_dict[category]):
            return garden_dict[category][index]
        else:
            print(f"Index '{index}' is out of range for the '{category}' category.")
    else:
        print(f"Category '{category}' does not exist in the garden dictionary.")

# I could not get this to work no matter how much I troubleshoot.  It's throwing off the other code.
#def garden_no_builtin_function(garden_dict, operation):
    #"""Function thats creates a function that takes a dictionary and accomplishes something similar to a built-in function."""
    #if operation == "min":
        #return no_builtin_min(garden_dict)
    #elif operation == "max":
        #return no_builtin_max(garden_dict)

#def no_builtin_min(garden_dict):
    #min_value = None
    #for key, value in garden_dict.items():
        #if min_value is None or len(value) < min_value:
            #min_value = len(value)
    #return min_value

#def no_builtin_max(garden_dict):
    #max_value = None
    #for key, value in garden_dict.items():
        #if max_value is None or len(value) > max_value:
            #max_value = len(value)
    #return max_value

def garden_function(garden_dict, operation):
    """ Function to create a function that takes a dictionary and accomplishes something similar to a built-in function."""
    if operation == "min":
        return min(len(v) for v in garden_dict.values())
    elif operation == "max":
        return max(len(v) for v in garden_dict.values())

def garden_set():
    """Function to create and use a set."""  
    # Create a set of flowers.
    flower_set = {"rose", "dahlia", "scotch broom", "daffodil"}

    # This will add -Sunflower- to the flowers set. 
    flower_set.add("sunflower")

    # This will remove scotch-broom- from teh flowers set. 
    flower_set.remove("scotch broom")

    def garden_set_function(operation):
        #function to use the flower set.
        if operation == "min":
            return min(flower_set)
        elif operation == "max":
            return max(flower_set)
    return flower_set, garden_set_function

def dict_set_in_functions(garden_dict, flower_set):
    """Function to use both dictionary and set as argument to functions.""" 
    # Behavior with dictionaries:
    print("Behavior with dictionaries:")
    print(f"Garden dictionary before the function: {garden_dict}")
    add_data(garden_dict, "fruit tree", "pear") 
    print(f"Garden dictionary after adding -Pear- to the fruit tree dicitonary: {garden_dict}")

    # Behavior with sets:
    print("\nBehavior with sets:")
    print(f"Flower set before the function: {flower_set}")
    flower_set.add("borage")
    print(f"Flower set after adding -Borage-: {flower_set}")

# Source:  https://www.w3schools.com/python/python_sets.asp
def set_comprehensions():
    """Function to show simple dictionary and set comprehensions."""
    # Define sets representing the plant information
    flowers = [("rose", "summer", 5), ("dahlia", "summer", 10), ("scotch broom", "spring", 5), ("daffodil", "spring", 50)]
    garden = [("tomato", "summer", 5), ("zucchini", "summer", 1), ("carrot", "summer", 5), ("green bean", "summer", 3), ("pumpkin", "fall", 2), ("squash", "fall", 3)]
    fruit_trees = [("apple", "fall", 3), ("plum", "summer", 2), ("cherry", "summer", 1) ]

    def merge_sets(*sets):
        """Simple dictionary comprehension."""
        merged_set = {}
        for x in sets:
            for plant, season, quantity in x:
                if plant not in merged_set:
                    merged_set[plant] = {"season": season, "quantity": quantity}
                else:
                    merged_set[plant]["quantity"] += quantity
        return merged_set

    # Call the merge_sets function with the defined sets
    merged_information = merge_sets(flowers, garden, fruit_trees)

    # Print the merged information
    print(f"\nInventory of seeds or plants and trees for the community garden is: ")
    for plant, details in merged_information.items():
        print(f"{plant}: Season: {details['season']} - Quantity: {details['quantity']}")

# Here is the main functions
def main():
    # Create garden dictionary.
    garden_dict = create_garden_dict()
    print("Garden Dictionary: ", garden_dict)

    # This is how I could add more data -Sunflower- to the garden dictionary.
    add_data(garden_dict, "flowers", "sunflower")
    print("\nAfter adding -Sunflower- to the flowers dictionary: ", garden_dict)

    # This is how I am able to change a value associated with a key in the garden dictionary. 
    change_value(garden_dict, "flowers", "scotch broom", "peony")
    print("\nAfter changing -Scotch Broom- to -Peony- in teh flowers dictionary: ", garden_dict)

    # This is how data can be removed from the garden dictionary.
    remove_data(garden_dict, "fruits", "apple")
    print("\nAfter removing 'Apple' from fruits dictionary: ", garden_dict)

    # Index the dictionary to find some value stored at a key within it.
    print("\nValue at index 2 of flowers dictionary: ", index_dictionary(garden_dict, "flowers", 2))

    # The shortest category in the garden dictionary.
    print("\nThe lenth of the shortest category in garden dictionary is: ", garden_function(garden_dict, "min"))

    # The total quantity of inventory.
    total_quantity_garden = sum(len(v) for v in (garden_dict["flowers"], garden_dict["vegetables"], garden_dict["fruits"]))
    print("\nTotal Quantity using sum:", total_quantity_garden)

    # Create and use a set.
    flower_set, custom_set_function = garden_set()
    print("\nFinal flower set:", flower_set)
    print("Minimum flower in set:", custom_set_function("min"))

    # Use both dictionary and set as arguments to functions.
    dict_set_in_functions(garden_dict, flower_set)

    # Show simple dictionary and set comprehensions.
    set_comprehensions()

# Execute the main function.
if __name__ == "__main__":
    main()

z = input ("Pause, CWest")
