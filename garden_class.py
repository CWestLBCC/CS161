class GardenClass:
    def __init__(self):
        self.inventory_flowers = ["rose", "dahlia", "scotch broom", "daffodil"]
        self.inventory_garden = ["tomato", "zucchini", "carrot"]
        self.fruit_tuple = ("apple", "plum", "cherry")

    def get_value_flower_input(self):
        tries = 3
        while tries > 0:
            user_input_flower = input("Enter one flower to grow in the garden: ")
            if user_input_flower.isalpha():
                return user_input_flower
            else:
                print("This is an incorrect entry, please try again.")
                tries -= 1
        print("Incorrect entry, this program will end.")
        return None

    def add_flower(self, flower):
        self.inventory_flowers.append("sunflower")
        self.inventory_flowers.append(flower)

    def remove_flower(self, flower):
        if flower in self.inventory_flowers:
            self.inventory_flowers.remove(flower)
        else:
            print(f"{flower} not found in the flower inventory.")

    def add_to_garden(self):
        self.inventory_garden.extend(["green bean", "pumpkin", "squash"])

    def concatenate_fruit(self):
        fruit_list = list(self.fruit_tuple)
        return self.inventory_flowers + self.inventory_garden + fruit_list

    def sort_concatenated_list(self):
        total_complete_list = self.concatenate_fruit()
        total_complete_list.sort()
        return total_complete_list

    def total_count_plants(self):
        count_inventory_flowers = len(self.inventory_flowers)
        count_inventory_garden = len(self.inventory_garden)
        count_fruit_tuple = len(self.fruit_tuple)
        return count_inventory_flowers + count_inventory_garden + count_fruit_tuple
