# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
from daro import prob_from_bonus

stats = [
    "Strength",
    "Dexterity",
    # "Speed",
    "Endurance",  # Hit points. Physical save, based on current value. Regain by rolling current value on rest, or by medicine.
    "Charisma",
    "Spirit",  # Mental save, based on current value. Warrior spends for extra attack/defence dice. Rogue for rerolls and spells. Mage for spells.
    "Wits"
]
stats2 = [
    "Strength",
    # "Stamina",
    "Dexterity",
    "Speed",  # "Agility",
    "Endurance",
    # "Perception",
    "Intellect",  # "Cunning",
    "Wits",  # "Willpower",
    "Charisma",
    "Essence"
]
stats3 = [
    "Strength",
    "Speed",
    "Stamina",
    "Str-o-Will",
    "Magic",
    "Fellowship"
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


def break_num2(num, count):
    ingreds = [num // count for _ in range(count)]

    while count:
        i1 = random.randrange(len(ingreds))
        i2 = (i1 + 1) % len(ingreds)
        n = random.randint(0, ingreds[i1])
        ingreds[i1] -= n
        ingreds[i2] += n
        count -= 1
    if sum(ingreds) < num:
        ingreds.append(num - sum(ingreds))
    return ingreds


def get_pool_stats():
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

    print(f"Gold{' ' * (max_stat_len - 4)}:{' ' + str(gold * 10) if gold >= 0 else gold * 10}")


def get_gonzo_stats():
    ms = 0

    hp = 0
    mp = 0
    mp_stat = 0
    mp_skill = 5
    lvl = 0
    hd = 6

    for stat in stats2:
        res = roll()
        score = res[0]
        rolled = res[1]
        bonus = int(math.sqrt(score))
        print(f"{stat: <{max_stat_len}}: {score: <2} / +{bonus} ({prob_from_bonus[bonus]}%)   {rolled}")

        # Attribute level:
        lvl += score

        if score > ms:
            ms = score
        if stat == "Endurance":
            hp = (score**2) * random.randint(1, hd)
        if stat == "Essence":
            mp = score  # random.randint(1, score)
        if stat in ["Cunning", "Willpower", "Charisma"] and score > mp_stat:
            mp_stat = score

    print(f"\nHP: {hp}")
    print(f"EP: {mp * (mp_stat + mp_skill)}")
    print(f"AL: {lvl}")
    return ms <= 20


def get_console_stats():
    ms = 0
    lvl = 0

    print(f"{max_stat_len * ' '} Raw | Bn | Multi")

    pwr_lvl = 10

    bonus_stats = dict()
    if pwr_lvl > 1:
        stat_bonus = (pwr_lvl - 1) * 2
        bonus_stats = break_num2(stat_bonus, len(stats3))

    for ndx, stat in enumerate(stats3):
        res = roll()
        score = res[0] + bonus_stats[ndx]
        rolled = res[1]
        bonus = int((score + pwr_lvl) // 2)
        multi = int(math.sqrt(score))
        print(f"{stat: <{max_stat_len}}: {score: <2} | {bonus: <2} | x{multi}   {rolled} + {bonus_stats[ndx]}")

        if stat == "Strength":
            l_str = score // 2
            l_bonus = int((l_str + pwr_lvl) // 2)
            a_str = score + (score - l_str)
            a_bonus = int((a_str + pwr_lvl) // 2)

            print(f"{'Arm': >{max_stat_len}}: {a_str: <2} | {a_bonus: <2} | x{int(math.sqrt(a_str))}")
            print(f"{'Leg': >{max_stat_len}}: {l_str: <2} | {l_bonus: <2} | x{int(math.sqrt(l_str))}")

        if stat == "Magic":
            l_str = score // 2
            l_bonus = int((l_str + pwr_lvl) // 2)
            a_str = score + (score - l_str)
            a_bonus = int((a_str + pwr_lvl) // 2)

            print(f"{'Power': >{max_stat_len}}: {a_str: <2} | {a_bonus: <2} | x{int(math.sqrt(a_str))}")
            print(f"{'Resistance': >{max_stat_len}}: {l_str: <2} | {l_bonus: <2} | x{int(math.sqrt(l_str))}")

        # Attribute level:
        lvl += score

        if score > ms:
            ms = score

    print(f"\nPL: {pwr_lvl}")
    print(f"AL: {lvl}")
    return ms <= 20


"""
Roll:
    d6*d6 + stat + skill
DC
easy   15
normal 20
hard   25
"""

"""
Differentiate current (effective) attribute score and permanent (maximum) attribute score.
Pool of d6s? Any 6 is a success.
Can split large pool for multiple actions.
You can go into debt during character creation no higher than your Charisma * 10.
When you run out of Endurance, roll d6 for injury location, destroy armour if present, then destroy limb.

Successes:
 1: success on EASY
    flawed success, success at a cost, or can try again on NORMAL
 2: success on NORMAL

Combat Pool resets at the start of each round. Then players wager any number of dice as initiative dice. They take
one action in order of number of initiative dice wagered; in case of a tie, they roll and higher success number goes
first, if there is still a tie, higher Dexterity goes first. Once everyone who had initiative dice had their action,
wager initiative again for another action. Players who have no more dice in their Combat Pool can take no further
actions until next round.
Warriors may add dice to their Combat Pool by spending points of Spirit, 1 for 1.
For attack/defense, get dice from your weapon/armour, plus may add any number from Combat Pool (even 0).
"""

if __name__ == "__main__":
    # get_pool_stats()

    # for i in range(4):
    #     print("\n==========\n")
    #     get_gonzo_stats()

    while get_console_stats():
        print("\n==========\n")
