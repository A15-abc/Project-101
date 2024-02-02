import random

response = "y"

while response.lower() == "y":
    # Generate a random number between 1 and 6 for the dice
    dice_number = random.randint(1, 6)

    # Print the representation of the dice based on the random number
    if dice_number == 1:
        print("---------")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("---------")
    elif dice_number == 2:
        print("---------")
        print("| *     |")
        print("|       |")
        print("|     * |")
        print("---------")
    elif dice_number == 3:
        print("---------")
        print("| *     |")
        print("|   *   |")
        print("|     * |")
        print("---------")
    elif dice_number == 4:
        print("---------")
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("---------")
    elif dice_number == 5:
        print("---------")
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
        print("---------")
    elif dice_number == 6:
        print("---------")
        print("| *   * |")
        print("| *   * |")
        print("| *   * |")
        print("---------")

    # Prompt user to roll the dice again
    response = input("Do you want to roll the dice again? (Enter 'y' for yes, 'n' for no): ")

# Program ends when the user enters 'n'
print("Thanks for playing!")