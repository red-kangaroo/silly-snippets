# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

stats = [
    "Strength",
    "Dexterity",
    # "Speed",
    "Endurance",  # Hit points. Physical save, based on current value. Regain by rolling current value on rest, or by medicine.
    "Charisma",
    "Spirit",  # Mental save, based on current value. Warrior spends for extra attack/defence dice. Rogue for rerolls and spells. Mage for spells.
    "Wits"
]
combat_stats = [
    "Strength",
    "Dexterity",
    # "Speed",
    "Wits"
]
max_stat_len = 10


##################################################
# 2d6 Stats Roller
##################################################
def roll():
    total = 0
    nums = list()

    while True:
        n1 = random.randint(1, 6)
        n2 = random.randint(1, 6)

        total += (n1 + n2)
        nums.extend([n1, n2])

        if n1 == n2: #or n2 == n3 or n3 == n1:  # DARO
            pass
        else:
            break

    return total, nums

# Differentiate current (effective) attribute score and permanent (maximum) attribute score.
# Pool of d6s? Any 6 is a success.
# Can split large pool for multiple actions.
# You can go into debt during character creation no higher than your Charisma * 10.
# When you run out of Endurance, roll d6 for injury location, destroy armour if present, then destroy limb.

# Successes:
#  1: success on EASY
#     flawed success, success at a cost, or can try again on NORMAL
#  2: success on NORMAL

# Combat Pool resets at the start of each round. Then players wager any number of dice as initiative dice. They take
# one action in order of number of initiative dice wagered; in case of a tie, they roll and higher success number goes
# first, if there is still a tie, higher Dexterity goes first. Once everyone who had initiative dice had their action,
# wager initiative again for another action. Players who have no more dice in their Combat Pool can take no further
# actions until next round.
# Warriors may add dice to their Combat Pool by spending points of Spirit, 1 for 1.
# For attack/defense, get dice from your weapon/armour, plus may add any number from Combat Pool (even 0).


if __name__ == "__main__":
    gold = 100  # len(stats) * 10
    adds = 0

    for stat in stats:
        res = roll()
        score = res[0]
        rolled = res[1]

        if stat in combat_stats:
            # if score < 6:
            #     adds += score - 6
            # elif score > 9:
            #     adds += score - 9
            adds += score
        gold -= score

        print(f"{stat: <{max_stat_len}}: {score: <2}   {rolled}")

    # if adds > 0:
    #     adds = '+'+str(adds)
    # elif adds == 0:
    #     adds = ''
    # print(f"\nCombat{' ' * (max_stat_len-6)}: weapon/armour {adds}")
    print(f"\nCombatPool: {adds}")

    print(f"Gold{' ' * (max_stat_len-4)}:{' '+str(gold*10) if gold >= 0 else gold*10}")
