import random9

def rolldice():
    return random.randint(1, 6)

def main():
    print("Let's roll some dice!")

    while True:
        input("Press Enter to roll the dice...")

        # Call the roll_dice function to get a random number between 1 and 6
        dice_result = rolldice()

        print(f"You rolled: {dice_result}")

        play_again = input("Do you want to roll the dice again? (yes/no): ").lower()

        #checks if the input is yes or y if otherwise , exits the program
        if play_again != 'y' and play_again != 'yes':
            print("Thank you for rolling a dice. Goodbye!")
            break

if __name__ == "__main__":
    main()
