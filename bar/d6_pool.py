# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

ABILITY = False  # Success also on 5.
INABILITY = False  # Deduct success on any 1.


##################################################
# Dice Pool Roller
##################################################
def roll_success_count(num):
    # Count successes from a pool. Normally success on 6, but see ABILITY and INABILITY.
    result = 0
    rolls = list()

    while num > 0:
        rolled = random.randint(1, 6)
        rolls.append(rolled)

        if ABILITY and rolled >= 5:
            result += 1
        elif INABILITY and rolled == 1:
            result -= 1
        elif rolled == 6:
            result += 1

        num -= 1

    return result, rolls


def roll_highest_explode(num):
    # Roll the pool, take the highest result. If it was a 6, explode.
    result = 0
    rolls = list()

    while num > 0:
        rolled = random.randint(1, 6)
        rolls.append(rolled)

        if rolled > result:
            result = rolled
        num -= 1

    if result == 6:
        add = roll_highest_explode(1)
        result += add[0]
        rolls.extend(add[1])

    return result, rolls


def roll_highest_combine(num):
    # Roll the pool, take the highest result. If there were multiple highest results, add them.
    result = 0
    max_roll = 0
    rolls = list()

    while num > 0:
        rolled = random.randint(1, 6)
        rolls.append(rolled)

        if rolled > max_roll:
            result = rolled
            max_roll = rolled
        elif rolled == max_roll:
            result += rolled
        num -= 1

    return result, rolls


if __name__ == "__main__":
    DICE = 4

    # r = roll_success_count(DICE)
    # print(f"Successes: {r[0]}   {sorted(r[1])}")

    # r = roll_highest_explode(DICE)
    # print(f"Result: {r[0]}   {r[1]}")

    r = roll_highest_combine(DICE)
    print(f"Result: {r[0]}   {r[1]}")
