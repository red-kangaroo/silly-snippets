# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

STAT = 5


##################################################
# d6 Roller
##################################################
def roll_explode(base):
    # Roll d6, explode on 6.
    rolled = random.randint(1, 6)
    if rolled == 6:
        base += rolled
        roll_explode(base)
    else:
        base += rolled

    return base


def roll_implode(base, rolls):
    # Roll d6, explode on 6 and implode on 1.
    rolled = random.randint(1, 6)
    if rolled == 6:
        rolls.append(rolled)
        base += rolled
        base, rolls = roll_implode(base, rolls)
    elif rolled == 1:
        minus = random.randint(1, 6)
        base -= minus
        rolls.append(-minus)
    else:
        base += rolled
        rolls.append(rolled)

    return base, rolls


if __name__ == "__main__":
    NBR = 5
    for i in range(NBR):
        rolls = list()
        r, rolls = roll_implode(STAT, rolls)
        print(f"Result: {r: <2}   = {STAT} + {rolls}")
