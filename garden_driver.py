# Import the Garden class
from garden_class import GardenClass

# Create an instance of GardenClass
my_garden = GardenClass()

# Call the methods
user_input_flower = my_garden.get_value_flower_input()
if user_input_flower:
    my_garden.add_flower(user_input_flower)
    print("Appended -Sunflower- and User_Input_Flower at end:", my_garden.inventory_flowers)
    # Continue interacting with other methods 

# Execute the driver file:
from garden_class import GardenClass

def main():
    my_garden = GardenClass()
    user_input_flower = my_garden.get_value_flower_input()
    if user_input_flower:
        my_garden.add_flower(user_input_flower)
        print("Appended -Sunflower- and User_Input_Flower at end:", my_garden.inventory_flowers)
        print("Flowers to eradicate from the garden:", my_garden.inventory_flowers[2])
        my_garden.remove_flower("scotch broom")
        print("Remove -Scotch Broom- from the flower list:", my_garden.inventory_flowers)
        my_garden.add_to_garden()
        print("Append a list to the end of the garden list:", my_garden.inventory_garden)
        print("The fruit trees currently grown in this garden are:", my_garden.fruit_tuple)
        print("Total Complete List:", my_garden.concatenate_fruit())
        print("Total Complete List (sort, remove quotes, add commas):", ", ".join(my_garden.sort_concatenated_list()))
        print("Total count of types of plants in the garden:", my_garden.total_count_plants())

if __name__ == "__main__":
    main()
