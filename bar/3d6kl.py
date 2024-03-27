# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

stats = [
    "Strength",
    "Dexterity",
    "Endurance",
    "Charisma",
    "Spirit",
    "Wits"
]
max_stat_len = 9


##################################################
# Stat Roller
##################################################
def roll_stats():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)

    kl = min([d1, d2, d3])
    gp = sum([d1, d2, d3]) - kl

    return kl, gp


if __name__ == "__main__":
    total_gold = 0

    for s in stats:
        score, gold = roll_stats()
        total_gold += gold
        print(f"{s: <{max_stat_len}}: +{score}")

    print(f"\nGold: {total_gold}")
