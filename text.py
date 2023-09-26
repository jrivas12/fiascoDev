import os
import pickle
#import colorama
import emoji

colorama.init()

# Define a simple Item class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Define locations and items
locations = {
    "forest": {
        "description": "You find yourself in a dense forest. There is a hidden treasure somewhere.",
        "items": [Item("sword", "A shiny sword"), Item("key", "A rusty key")]
    },
    "cave": {
        "description": "You enter a dark cave. It's too dark to see anything.",
        "items": [Item("torch", "A flickering torch"), Item("gem", "A precious gem")]
    },
    "river": {
        "description": "You reach a fast-flowing river. There's a bridge across it.",
        "items": [Item("map", "A torn map"), Item("food", "Some dried fruits")]
    }
}

# Function to display player inventory
def display_inventory(inventory):
    print("\nYour Inventory:")
    if not inventory:
        print(colorama.Fore.RED + "Empty" + colorama.Style.RESET_ALL)
    else:
        for item in inventory:
            print(colorama.Fore.GREEN + f"- {item.name}: {item.description}" + colorama.Style.RESET_ALL)

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
        print(colorama.Fore.CYAN + "Welcome back! You continue your adventure." + colorama.Style.RESET_ALL)
    else:
        player_location = "forest"
        print(colorama.Fore.CYAN + "Welcome to the Adventure Game!" + colorama.Style.RESET_ALL)

    while True:
        print("\nCurrent Location:", colorama.Fore.YELLOW + player_location.capitalize() + colorama.Style.RESET_ALL)
        print(locations[player_location]["description"])
        display_inventory(player_inventory)

        action = input("What do you want to do? (explore/move/take/quit): ").lower()

        if action == "quit":
            save_game(player_location, player_inventory)
            print(colorama.Fore.MAGENTA + emoji.emojize("Your progress has been saved. Goodbye! :wave:", use_aliases=True) + colorama.Style.RESET_ALL)
            break
        elif action == "explore":
            print(colorama.Fore.YELLOW + "You search the area but find nothing of interest." + colorama.Style.RESET_ALL)
        elif action == "move":
            new_location = input("Where do you want to go? (forest/cave/river): ").lower()
            if new_location in locations:
                player_location = new_location
            else:
                print(colorama.Fore.RED + "Invalid location." + colorama.Style.RESET_ALL)
        elif action == "take":
            item_name = input("Which item do you want to take? (sword/key/torch/gem/map/food): ").lower()
            for item in locations[player_location]["items"]:
                if item.name == item_name:
                    player_inventory.append(item)
                    locations[player_location]["items"].remove(item)
                    print(colorama.Fore.GREEN + f"You have taken the {item_name}." + colorama.Style.RESET_ALL)
                    break
            else:
                print(colorama.Fore.RED + "Item not found." + colorama.Style.RESET_ALL)

if __name__ == "__main__":
    play_game()
