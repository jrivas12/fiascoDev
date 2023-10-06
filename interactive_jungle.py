import random

class InteractivePrompt:
    @staticmethod
    def get_choice(prompt, options):
        while True:
            print(prompt)
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(options):
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run(self):
        print("Welcome to the Interactive Prompt!")

        while True:
            category_choice = self.get_choice(
                "Choose a category:",
                ["Car", "Animal", "Food", "Exit"]
            )

            if category_choice == 1:  # Car
                car_makers = ["Toyota", "Ford", "Honda"]
                car_maker_choice = self.get_choice(
                    "Choose a car maker:",
                    car_makers
                )
                selected_maker = car_makers[car_maker_choice - 1]

                car_models = ["Camry", "Mustang", "Civic"]
                selected_model = random.choice(car_models)

                print(f"Vroom, vroom! You selected a {selected_maker} {selected_model}")

            elif category_choice == 2:  # Animal
                animal_types = ["Mammals", "Birds", "Fish"]
                animal_type_choice = self.get_choice(
                    "Choose a type of animal:",
                    animal_types
                )
                selected_type = animal_types[animal_type_choice - 1]

                if selected_type == "Mammals":
                    mammals = ["Dog", "Cat", "Elephant"]
                    selected_animal = random.choice(mammals)
                elif selected_type == "Birds":
                    birds = ["Sparrow", "Eagle", "Penguin"]
                    selected_animal = random.choice(birds)
                else:
                    fish = ["Salmon", "Tuna", "Shark"]
                    selected_animal = random.choice(fish)

                print(f"Good fella! This is a {selected_animal}")

            elif category_choice == 3:  # Food
                food_types = ["Dessert", "Fruit", "Beverage"]
                food_type_choice = self.get_choice(
                    "Choose a type of food:",
                    food_types
                )
                selected_type = food_types[food_type_choice - 1]

                if selected_type == "Dessert":
                    desserts = ["Cake", "Ice Cream", "Cookies"]
                    selected_food = random.choice(desserts)
                elif selected_type == "Fruit":
                    fruits = ["Apple", "Banana", "Orange"]
                    selected_food = random.choice(fruits)
                else:
                    beverages = ["Coffee", "Tea", "Soda"]
                    selected_food = random.choice(beverages)

                print(f"Yummy, this is a {selected_food}")

            elif category_choice == 4:  # Exit
                print("Thank you for using the interacive module. Goodbye!")
                break

            else:
                print("Fatal error! Please try again.")

if __name__ == "__main__":
    prompt = InteractivePrompt()
    prompt.run()
