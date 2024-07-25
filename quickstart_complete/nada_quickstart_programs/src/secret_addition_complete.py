import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def intro():
    print_slow("Welcome to the Adventure Game!")
    print_slow("You find yourself in a dark forest.")
    print_slow("There are paths to the north, south, east, and west.")
    print_slow("Which direction will you go?")

def north():
    print_slow("You walk north and find a tranquil lake.")
    print_slow("A mysterious figure emerges from the water.")
    print_slow("Will you (talk) to them or (run) away?")

def south():
    print_slow("You walk south and encounter a wild beast!")
    print_slow("Will you (fight) it or (flee)?")

def east():
    print_slow("You walk east and discover an abandoned cabin.")
    print_slow("Will you (enter) the cabin or (leave)?")

def west():
    print_slow("You walk west and fall into a hidden trap.")
    print_slow("It's too deep to climb out. Game over.")

def main():
    intro()
    while True:
        direction = input("Choose your direction (north, south, east, west): ").lower()
        if direction == "north":
            north()
            break
        elif direction == "south":
            south()
            break
        elif direction == "east":
            east()
            break
        elif direction == "west":
            west()
            break
        else:
            print("Invalid direction. Try again.")
    
    next_step = input("What will you do next? ").lower()
    if direction == "north":
        if next_step == "talk":
            print_slow("The figure offers you a magical sword. You win!")
        elif next_step == "run":
            print_slow("You run back to the forest. Safe but empty-handed.")
        else:
            print_slow("Invalid action. Game over.")
    elif direction == "south":
        if next_step == "fight":
            print_slow("You bravely fight the beast and win! You find a treasure chest.")
        elif next_step == "flee":
            print_slow("You flee back to the forest, but the beast chases and catches you. Game over.")
        else:
            print_slow("Invalid action. Game over.")
    elif direction == "east":
        if next_step == "enter":
            print_slow("Inside the cabin, you find a map leading to a hidden treasure. You win!")
        elif next_step == "leave":
            print_slow("You leave the cabin and wander back into the forest, missing out on potential riches.")
        else:
            print_slow("Invalid action. Game over.")

if __name__ == "__main__":
    main()
