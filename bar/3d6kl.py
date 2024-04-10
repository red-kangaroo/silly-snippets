# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

stats = [
    "Strength",
    "Dexterity",
    # "Endurance",
    # "Charisma",
    # "Spirit",
    "Wits"
]
skills = [
    "Athletics",
    "Alchemy",
    "Beastcraft",
    "Education",
    "Medicine",
    "Occult",
    "Seamanship",
    "Stealth",
    "Tinker",
    "Wildcraft",
]
max_stat_len = 10


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
    total_stat = 0

    for s in stats:
        score, gold = roll_stats()
        total_stat += score
        total_gold += gold

        print(f"{s: <{max_stat_len}}: +{score}")

    print("")
    skillz = dict()
    for i in range(20 - total_stat):
        skill = random.choice(skills)
        if skill in skillz.keys():
            skillz[skill] += 1
        else:
            skillz[skill] = 1
    skillz = dict(sorted(skillz.items()))
    for skill, bonus in skillz.items():
        print(f"{skill: <{max_stat_len}}: +{bonus}")

    print(f"\nGold: {total_gold}")
