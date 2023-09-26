import os
import pickle

# Define a simple Item class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Define locations and items
locations = {
    "forest": {
        "description": "You find yourself in a dense forest. There is a hidden treasure somewhere.",
        "items": [Item("sword", "A shiny sword"), Item("key", "A rusty key")],
        "color": "\033[92m"  # Green
    },
    "cave": {
        "description": "You enter a dark cave. It's too dark to see anything.",
        "items": [Item("torch", "A flickering torch"), Item("gem", "A precious gem")],
        "color": "\033[93m"  # Brown
    },
    "river": {
        "description": "You reach a fast-flowing river. There's a bridge across it.",
        "items": [Item("map", "A torn map"), Item("food", "Some dried fruits")],
        "color": "\033[94m"  # Blue
    }
}

# Function to display player inventory
def display_inventory(inventory):
    print("\nYour Inventory:")
    if not inventory:
        print("\033[91m" + "Empty" + "\033[0m")  # Red
    else:
        for item in inventory:
            print("\033[92m" + f"- {item.name}: {item.description}" + "\033[0m")  # Green

# Function to save game data to a file using pickle
def save_game(player_location, player_inventory):
    game_data = {"location": player_location, "inventory": player_inventory}
    with open("save_game.dat", "wb") as file:
        pickle.dump(game_data, file)

# Function to load game data from a file using pickle
def load_game():
    if os.path.exists("save_game.dat"):
        with open("save_game.dat", "rb") as file:
            return pickle.load(file)
    return None

# Main game loop
def play_game():
    player_inventory = []
    game_data = load_game()
    if game_data:
        player_location = game_data["location"]
        player_inventory = game_data["inventory"]
        print("Welcome back! You continue your adventure.")
    else:
        player_location = "forest"
        print("Welcome to the Adventure Game!")

    while True:
        location_info = locations[player_location]
        print(location_info["color"] + "\nCurrent Location:", player_location.capitalize() + "\033[0m")
        print(location_info["color"] + locations[player_location]["description"] + "\033[0m")
        display_inventory(player_inventory)

        action = input("What do you want to do? (explore/move/take/quit): ").lower()

        if action == "quit":
            save_game(player_location, player_inventory)
            print("\033[1m\033[95mYour progress has been saved. Goodbye!\033[0m")
            break
        elif action == "explore":
            print("You search the area but find nothing of interest.")
        elif action == "move":
            new_location = input("Where do you want to go? (forest/cave/river): ").lower()
            if new_location in locations:
                player_location = new_location
            else:
                print("\033[91m" + "Invalid location." + "\033[0m")  # Red
        elif action == "take":
            item_name = input("Which item do you want to take? (sword/key/torch/gem/map/food): ").lower()
            for item in locations[player_location]["items"]:
                if item.name == item_name:
                    player_inventory.append(item)
                    locations[player_location]["items"].remove(item)
                    print("\033[92m" + f"You have taken the {item_name}." + "\033[0m")  # Green
                    break
            else:
                print("\033[91m" + "Item not found." + "\033[0m")  # Red
        else:
            print("\033[91m" + "Invalid choice. Please enter a valid number." + "\033[0m")  # Red

if __name__ == "__main__":
    play_game()
