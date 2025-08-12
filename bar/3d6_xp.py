# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random

stats = [
    "Strength",
    "Dexterity",
    "Vitality",
    "Intelligence",
    "Awareness",
    "Charisma"
]
max_stat_len = 12


##################################################
# XP Stat Roller
##################################################
def roll_stats():
    xp_all = list()

    while len(xp_all) < 10:
        xp = 0

        for s in stats:
            score = math.ceil((random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) / 2)
            xp += 10 - score

            print(f"{s: <{max_stat_len}}:{score: 3}")

        xp_all.append(xp)
        print(f"XP: {xp}\n\n")

    print(f"Average XP: {sum(xp_all) / len(xp_all)}")


if __name__ == "__main__":
    roll_stats()
