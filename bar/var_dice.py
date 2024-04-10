# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

stats = [
    "Strength",
    "Dexterity",
    "Endurance",
    "Wits",
    "Sanity",
    "Charisma",
]
dice = [
    'd2',
    'd4',
    'd6',
    'd8',
    'd10',
    'd12',
    '2d8',
    '2d10',
    '3d8',
    '3d10',
    '4d8',
    '3d12',
    '4d10',
    '4d12',
    '5d10'
]
max_stat_len = 9


##################################################
# Stat Roller
##################################################
def roll_stats() -> int:
    stat = random.randint(1, 6) + random.randint(1, 6)

    if stat == 12:
        d = random.randint(1, 6)
        stat += d
        while d == 6:
            d = random.randint(1, 6)
            stat += d

    return stat // 2


if __name__ == "__main__":
    hp = 0
    mp = 0

    for s in stats:
        tier = roll_stats()
        stat_die = dice[tier]
        if stat_die.startswith('d'):
            stat_die = ' ' + stat_die

        print(f"{s: <{max_stat_len}}: {stat_die} ({tier})")

        if s in ["Dexterity", "Endurance"]:
            d_num, d_val = stat_die.split('d')
            hp += int(d_num.replace(' ', '1')) * int(d_val)
        if s in ["Wits", "Sanity"]:
            d_num, d_val = stat_die.split('d')
            mp += int(d_num.replace(' ', '1')) * int(d_val)

    print(f"\nHP: {hp}"
          f"\nMP: {mp}")

# Strength :  d8
# Dexterity: 2d10
# Endurance:  d8
# Wits     : 2d8
# Sanity   :  d10
# Charisma :  d6
#
# HP: 28
# MP: 26
