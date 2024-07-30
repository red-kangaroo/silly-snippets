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
    "Str. of Will",
    "Magic",
    "Fellowship"
]
alt_stats = {
    "Strength": ["Arm", "Leg"],
    "Magic": ["Power", "Resist"]
}
combat_stats = [
    "Strength",
    "Dexterity",
    # "Speed",
    "Wits"
]
max_stat_len = 12


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

    pwr_lvl = 1
    weapon = 5
    armour = 5
    shield = 5

    all_stats = dict()
    if pwr_lvl > 1:
        bonus_stats = dict()
        stat_bonus = (pwr_lvl - 1) * 2
        bonus_stats = break_num2(stat_bonus, len(stats3))
    else:
        bonus_stats = [0] * len(stats3)

    for ndx, stat in enumerate(stats3):
        res = roll()
        score = res[0]
        rolled = res[1]

        if stat in alt_stats.keys() and not random.randint(0, 2):
            alts = alt_stats[stat].copy()
            random.shuffle(alts)

            l_str = score // 2
            l_bonus = int((l_str + pwr_lvl) // 2)
            h_str = score + (score - l_str) + bonus_stats[ndx]
            h_bonus = int((h_str + pwr_lvl) // 2)

            all_stats[f"{stat} {alts[0]}"] = {
                "score": l_str,
                "bonus": l_bonus,
                "multi": int(math.sqrt(l_str))
            }
            all_stats[f"{stat} {alts[1]}"] = {
                "score": h_str,
                "bonus": h_bonus,
                "multi": int(math.sqrt(h_str)),
                "roll": f"{rolled} + {bonus_stats[ndx]}"
            }
        else:
            score += bonus_stats[ndx]
            bonus = int((score + pwr_lvl) // 2)
            multi = int(math.sqrt(score))

            all_stats[stat] = {
                "score": score,
                "bonus": bonus,
                "multi": multi,
                "roll": f"{rolled} + {bonus_stats[ndx]}"
            }

        # Attribute level:
        lvl += score

        if score > ms:
            ms = score

    print(f"{max_stat_len * ' '} Raw | Bn | Multi")

    sorted_stats = dict(sorted(all_stats.items(), reverse=True))
    for stat, s in sorted_stats.items():
        ln = f"{stat: <{max_stat_len}}: {s['score']: <2} | {s['bonus']: <2} | x{s['multi']}"
        if "roll" in s.keys():
            ln += f"   {s['roll']}"
        print(ln)

    print("")

    block = all_stats["Strength Arm"]["score"] if "Strength Arm" in all_stats.keys() else all_stats["Strength"]["score"]
    block += all_stats["Stamina"]["score"] + shield
    block_bonus = int((block + pwr_lvl) // 2)
    print(f"{'Block': >{max_stat_len}}: {block: <2} | {block_bonus: <2}")
    dodge = all_stats["Strength Leg"]["score"] if "Strength Leg" in all_stats.keys() else all_stats["Strength"]["score"]
    dodge += all_stats["Speed"]["score"]
    dodge_bonus = int((dodge + pwr_lvl) // 2)
    print(f"{'Dodge': >{max_stat_len}}: {dodge: <2} | {dodge_bonus: <2}")
    parry = all_stats["Strength Arm"]["score"] if "Strength Arm" in all_stats.keys() else all_stats["Strength"]["score"]
    parry += weapon
    parry_bonus = int((parry + pwr_lvl) // 2)
    print(f"{'Parry': >{max_stat_len}}: {parry: <2} | {parry_bonus: <2}")

    print("")

    arm = all_stats["Stamina"]["score"] + armour
    arm_bonus = int((arm + pwr_lvl) // 2)
    print(f"{'Armor': >{max_stat_len}}: {arm: <2} | {arm_bonus: <2}")
    m_arm = all_stats["Magic Resist"]["score"] if "Magic Resist" in all_stats.keys() else all_stats["Magic"]["score"]
    m_arm_bonus = int((m_arm + pwr_lvl) // 2)
    print(f"{'Magic Armor': >{max_stat_len}}: {m_arm: <2} | {m_arm_bonus: <2}")
    s_arm = all_stats["Fellowship"]["score"]
    s_arm_bonus = int((s_arm + pwr_lvl) // 2)
    print(f"{'Social Armor': >{max_stat_len}}: {s_arm: <2} | {s_arm_bonus: <2}")

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
