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
    "Skill",
    "Speed",
    "Stamina",
    "Str. of Will",
    "Senses",
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


"""
Roll:
    d6*d6 + stat + skill
DC
easy   15
normal 20
hard   25
"""


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


def get_console_stats():
    ms = 0
    lvl = 0

    pwr_lvl = 10
    weapon = pwr_lvl
    catalyst = pwr_lvl
    armour = pwr_lvl  # First, determine Effective Armour as average armour of head, arms, torso and legs. If your Invulnerability is higher than Effective Armour, use Invulnerability instead.
    shield = pwr_lvl

    all_stats = dict()
    if pwr_lvl > 1:
        # stat_bonus = (pwr_lvl - 1) * 2
        # bonus_stats = break_num2(stat_bonus, len(stats3))

        stat_bonus = (pwr_lvl - 1)
        bonus_stats = [stat_bonus, stat_bonus] + [0] * (len(stats3) - 2)
        random.shuffle(bonus_stats)
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

    print(f"{max_stat_len * ' '}  Raw | Bn | Multi")

    sorted_stats = dict(sorted(all_stats.items(), reverse=True))
    for stat, s in sorted_stats.items():
        ln = f"{stat: <{max_stat_len}}: {s['score']: >3} | {s['bonus']: <2} | x{s['multi']}"
        if "roll" in s.keys():
            ln += f"   {s['roll']}"
        print(ln)

    print("")

    melee = all_stats["Strength Arm"]["score"] if "Strength Arm" in all_stats.keys() else all_stats["Strength"]["score"]
    melee += all_stats["Skill"]["score"] + weapon
    melee_bonus = int((melee + pwr_lvl) // 3)
    print(f"{'Melee': >{max_stat_len}}: {melee: >3} | {melee_bonus: <2}")
    melee = all_stats["Strength Leg"]["score"] if "Strength Leg" in all_stats.keys() else all_stats["Strength"]["score"]
    melee += all_stats["Speed"]["score"] + all_stats["Stamina"]["score"]
    melee_bonus = int((melee + pwr_lvl) // 3)
    print(f"{'Kick': >{max_stat_len}}: {melee: >3} | {melee_bonus: <2}")
    ranged = all_stats["Senses"]["score"] + all_stats["Skill"]["score"] + weapon
    ranged_bonus = int((ranged + pwr_lvl) // 3)
    print(f"{'Ranged': >{max_stat_len}}: {ranged: >3} | {ranged_bonus: <2}")
    # ranged = all_stats["Speed"]["score"]
    # ranged += all_stats["Senses"]["score"] + weapon
    # ranged_bonus = int((ranged + pwr_lvl) // 2)
    # print(f"{'Firearm': >{max_stat_len}}: {ranged: >3} | {ranged_bonus: <2}")
    spell = all_stats["Magic Power"]["score"] if "Magic Power" in all_stats.keys() else all_stats["Magic"]["score"]
    spell += all_stats["Str. of Will"]["score"] + catalyst
    spell_bonus = int((spell + pwr_lvl) // 3)
    print(f"{'Spell': >{max_stat_len}}: {spell: >3} | {spell_bonus: <2}")
    bluff = all_stats["Fellowship"]["score"]
    bluff_bonus = int((bluff + pwr_lvl) // 2)
    print(f"{'Bluff': >{max_stat_len}}: {bluff: >3} | {bluff_bonus: <2}")

    print("")

    block = all_stats["Strength Arm"]["score"] if "Strength Arm" in all_stats.keys() else all_stats["Strength"]["score"]
    block += all_stats["Stamina"]["score"] + shield
    block_bonus = int((block + pwr_lvl) // 3)
    print(f"{'Block': >{max_stat_len}}: {block: >3} | {block_bonus: <2}")
    dodge = all_stats["Strength Leg"]["score"] if "Strength Leg" in all_stats.keys() else all_stats["Strength"]["score"]
    dodge += all_stats["Speed"]["score"] + all_stats["Senses"]["score"]
    dodge_bonus = int((dodge + pwr_lvl) // 3)
    print(f"{'Dodge': >{max_stat_len}}: {dodge: >3} | {dodge_bonus: <2}")
    parry = all_stats["Skill"]["score"] + all_stats["Speed"]["score"] + weapon
    parry_bonus = int((parry + pwr_lvl) // 3)
    print(f"{'Parry': >{max_stat_len}}: {parry: >3} | {parry_bonus: <2}")
    spell = all_stats["Magic Power"]["score"] if "Magic Power" in all_stats.keys() else all_stats["Magic"]["score"]
    spell += all_stats["Senses"]["score"] + catalyst
    spell_bonus = int((spell + pwr_lvl) // 3)
    print(f"{'Counterspell': >{max_stat_len}}: {spell: >3} | {spell_bonus: <2}")
    stlth = all_stats["Skill"]["score"] + all_stats["Speed"]["score"] + all_stats["Senses"]["score"]
    stlth_bonus = int((stlth + pwr_lvl) // 3)
    print(f"{'Stealth': >{max_stat_len}}: {stlth: >3} | {stlth_bonus: <2}")

    print("")

    arm = all_stats["Stamina"]["score"]
    res_bonus = int((arm + pwr_lvl) // 2)
    print(f"{'Resiliency': >{max_stat_len}}: {arm: >3} | {res_bonus: <2}")
    arm += armour
    arm_bonus = int((arm + pwr_lvl) // 2)
    print(f"{'Armor': >{max_stat_len}}: {arm: >3} | {arm_bonus: <2}")
    m_arm = all_stats["Magic Resist"]["score"] if "Magic Resist" in all_stats.keys() else all_stats["Magic"]["score"]
    m_arm += all_stats["Str. of Will"]["score"]
    m_arm_bonus = int((m_arm + pwr_lvl) // 2)
    print(f"{'Magic Armor': >{max_stat_len}}: {m_arm: >3} | {m_arm_bonus: <2}")
    s_arm = all_stats["Fellowship"]["score"]
    s_arm += all_stats["Str. of Will"]["score"]
    s_arm_bonus = int((s_arm + pwr_lvl) // 2)
    print(f"{'Social Armor': >{max_stat_len}}: {s_arm: >3} | {s_arm_bonus: <2}")

    print(f"\nPL: {pwr_lvl}")
    print(f"AL: {lvl}")
    return ms <= 20


"""Console
DIFFERENCE       %
-30 or less		  1
-25 to -29		  2
-20 to -24		  5
-15 to -19		 10
-10 to -14		 15
 -5 to -9		 20
 -4 to +4		 25
 +5 to +9		 30
+10 to +14		 40
+15 ot +19		 50
+20 to +24		 60
+25 to +29		 75
+30 to +39		 90
+40 to +49		 99
+50 to +59		125
+60 to +69		150
+70 to +79		175
+80 or more		+25
"""

if __name__ == "__main__":
    # get_pool_stats()

    # for i in range(2):
    #     print("\n==========\n")
    #     get_console_stats()

    while get_console_stats():
        print("\n==========\n")
