# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random

# Differentiate current (effective) attribute score and permanent (maximum) attribute score.
# Thresholds for bonus are taken from effective attribute score. There are only a few, so put them on character sheet.
# Skills increase effective attribute score for specific tasks. Each class has several starting skills that they get at
# score d6, all the rest can be gained from guilds.
# All classes can spend Spirit: Warrior spends for extra attack/defence dice. Rogue for rerolls and spells.
# Mage for spells.

# At the end of each session, increase attribute of your choice by +1 OR split +2 between any skills.
# Levels are taken in guilds, by paying a fee depending on level plus finishing a quest. Levels increase skills (by +L,
# which can be split between all skills the guild offers), plus sometimes give special abilities. Quests are like EC.

# You can go into debt during character creation no higher than your Charisma * 10.
# All equipment has stat requirements, usually Str + Dex, but can be any.
# Weapons use the stat with highest requirement for to-hit roll.
#   spirit sabre - req Str, Dex, very high Spirit; so to-hit rolled with spirit
#   wizard staff - req Wits
#   some magic items and jewelry also have reqs
# Damage is taken to random attribute (???), or primarily to ablative armour pool.

stats = [
    "Strength",   # Carry slots
    "Dexterity",  # Initiative
    "Endurance",  # Physical save, based on current value. Regain by rolling current value on rest, or by medicine.
    "Charisma",
    "Spirit",     # Mental save, based on current value.
    "Wits"
]
max_stat_len = 10

prob_from_bonus = {
    1: '28',
    2: '42',
    3: '58',
    4: '72',
    5: '83',
    6: '92',
    7: '97',
    8: '100',
}

"""
function: daro ROLL:s {
  if 1@ROLL = 2@ROLL {
    result: ROLL + 2d6
  } else {
    result: ROLL
  }
}
output [daro 2d6] named "DARO: explode doubles"
"""


##################################################
# 2d6 Scale-able System
##################################################
def roll():
    total = 0
    nums = list()

    while True:
        n1 = random.randint(1, 6)
        n2 = random.randint(1, 6)
        # n3 = random.randint(1, 6)

        total += (n1 + n2)
        nums.extend([n1, n2])

        # if n1 == n2 == n3:  # TARO
        #     pass
        if n1 == n2:  # DARO
            pass
        else:
            break

    return total, nums


def print_stats():
    gold = 1000

    for stat in stats:
        res = roll()
        score = res[0]
        rolled = res[1]
        gold -= score * score

        bonus = int(math.sqrt(score))
        print(f"{stat: <{max_stat_len}}: {score: <2} / +{bonus} ({prob_from_bonus[bonus]}%)   {rolled}")

    print(f"Gold{' ' * (max_stat_len - 4)}:{' ' + str(gold) if gold >= 0 else gold}")
    return gold > 0


if __name__ == "__main__":
    # for i in range(4):
    #     print_stats()
    #     print("\n==========\n")

    while print_stats():
        print("\n==========\n")
