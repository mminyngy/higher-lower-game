from art import *
from game_data import *
import random
import os

corr = True
score = 0
a_idx = random.randrange(0, len(data))
b_idx = random.randrange(0, len(data))
while a_idx == b_idx:
    b_idx = random.randrange(0, len(data))
print(logo)

while corr == True:
    print(
        f"Compare A: {data[a_idx].get('name')}, a(n) {data[a_idx].get('description')}, from {data[a_idx].get('country')}"
    )
    print("A: " + str(data[a_idx].get('follower_count')))  ##check
    print(vs)
    print(
        f"Against B: {data[b_idx].get('name')}, a(n) {data[b_idx].get('description')}, from {data[b_idx].get('country')}"
    )
    print("B: " + str(data[b_idx].get('follower_count')))  ##check

    ans = input(("Who has more followers? Type 'A' or 'B': ")).upper()

    while ans != 'A' and ans != 'B':
        ans = input(("ERROR: Wrong input! Please type 'A' or 'B': ")).upper()

    if ans == 'A':
        if data[a_idx].get('follower_count') > data[b_idx].get(
                'follower_count'):
            del data[b_idx]
            score += 1
            os.system('clear')
            print(logo)
            print(f"You're rignt! Current score: {score}")
            new_b_idx = random.randrange(0, len(data))
            while a_idx == new_b_idx or b_idx == new_b_idx:
                new_b_idx = random.randrange(0, len(data))
            b_idx = new_b_idx
        else:
            os.system('clear')
            print(logo)
            print(f"Sorry, that's wrong. Final Score: {score}")
            corr = False

    elif ans == 'B':
        if data[b_idx].get('follower_count') > data[a_idx].get(
                'follower_count'):
            del data[a_idx]
            score += 1
            os.system('clear')
            print(logo)
            print(f"You're rignt! Current score: {score}")
            new_b_idx = random.randrange(0, len(data))
            new_a_idx = b_idx
            while new_a_idx == new_b_idx or new_b_idx == a_idx:
                new_b_idx = random.randrange(0, len(data))
            a_idx = new_a_idx
            b_idx = new_b_idx
        else:
            os.system('clear')
            print(logo)
            print(f"That's wrong. Final Score {score}")
            corr = False
