from random import randint

def roll_dice(sides, rolls):
    print(f"Rolling {sides}-sided dice {rolls} times...\n")
    for i in range(1, rolls + 1):
        roll = randint(1, sides)
        print(f"Roll {i}: {roll}")


if __name__ == '__main__':
    sides = int(input("Enter the number of sides on the dice: "))
    rolls = int(input("Enter the number of times to roll the dice: "))

    roll_dice(sides, rolls)
