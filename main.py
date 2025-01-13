from random import randint

def print_instructions():
    print("""
    Welcome to the Dice Rolling Simulator!

    This program simulates rolling a dice multiple times. Here's how it works:

    1. You will be asked to enter the number of sides on the dice (e.g., 6 for a standard die).
    2. You will also be asked how many times you want to roll the dice.
    3. The program will then roll the dice the specified number of times, showing the result of each roll.

    The dice rolls are random, and each roll is independent of the previous ones.

    Let's get started!
    """)

def roll_dice(num_sides, num_rolls):
    print(f"Rolling a {num_sides}-sided dice {num_rolls} times...\n")
    for i in range(1, num_rolls + 1):
        roll = randint(1, num_sides)
        print(f"Roll {i}: {roll}")

if __name__ == '__main__':
    print_instructions()

    sides = int(input("Enter the number of sides on the dice (e.g., 6 for a typical die): "))
    rolls = int(input("Enter the number of times to roll the dice: "))

    roll_dice(sides, rolls)
