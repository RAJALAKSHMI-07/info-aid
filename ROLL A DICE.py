import random
from datetime import datetime

# Create a list to store roll history
roll_history = []

def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    # Add the roll to the history
    roll_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    roll_history.append((roll_time, results))
    return results

def display_roll_history():
    print("\nRoll History:")
    for i, (roll_time, results) in enumerate(roll_history, start=1):
        result_str = ', '.join(map(str, results))
        print(f"{i}. {roll_time}: {result_str}")

def main():
    while True:
        try:
            print("\nOptions:")
            print("1. Roll Dice")
            print("2. Display Roll History")
            print("0. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                num_dice = int(input("Enter the number of dice you want to roll: "))
                if num_dice < 1:
                    print("Please enter a valid number of dice (1 or more).")
                    continue
                dice_results = roll_dice(num_dice)
                print(f"You rolled {num_dice} dice: {', '.join(map(str, dice_results))}")
            elif choice == '2':
                display_roll_history()
            elif choice == '0':
                print("ByeBye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid number of dice.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    print("Welcome to the Extended Dice Roller!")
    main()
