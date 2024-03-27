# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
from d6_explode_implode import roll_explode

stats = [
    "Strength",
    "Perception",
    "Endurance",
    "Charisma",
    "Intellect",
    "Agility",
    "Luck"
]
max_stat_len = 10
exceptional_threshold = 16


##################################################
# Palladium Stat Roller
##################################################
def roll_stats():
    stat = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    if stat >= exceptional_threshold:
        stat = roll_explode(stat)

    return stat


if __name__ == "__main__":
    max_stat = 0

    while max_stat < 20:
        for s in stats:
            score = roll_stats()
            max_stat = max(score, max_stat)

            bonus = math.floor((score - 10) / 2)
            if bonus >= 0:
                bonus = f'+{bonus}'

            print(f"{s: <{max_stat_len}}:{score: 3} ({bonus})")
        print("")
