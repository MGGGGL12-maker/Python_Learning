# Roller Dice Python Program

from random import randint

# \u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518
# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│  ●      │",
       "│    ●    │",
       "│      ●  │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│  ●   ●  │",
       "│         │",
       "│  ●   ●  │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│  ●   ●  │",
       "│    ●    │",
       "│  ●   ●  │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "└─────────┘")
    
}

dice = []
total = 0
num_dices = int(input("How many dice?: "))

for d in range(num_dices):
    num = randint(1, 6)
    dice.append(num)
    total += num  

"""for die in range(num_dices):
    for line in dice_art.get(dice[die]):
        print(line)"""

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()
print(f"Total: {total}")