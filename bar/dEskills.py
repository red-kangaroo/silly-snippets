# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

SKILLS = ["Acrobacy", "Arcologistics", "Argue", "Architecture", "Armour Penetration", "Armour Repair", "Armour Use", "Arts/Performance", "Arts/Visual", "Assassin", "Astrogation", "Biology", "Botany", "Brawl", "Brewing", "Bureaucracy", "Business", "Camping", "Climbing", "Command", "Communications", "Cooking", "Craft/Earth", "Craft/Metal", "Craft/Wood", "Cyber Warfare", "Cybernetics", "Disguise & Camouflage", "Dodge", "Drive Burrower", "Drive Heavy Machinery", "Drive Hovercraft", "Drive Railed", "Drive Tracked", "Drive Walker", "Drive Wheeled", "Drive Winter", "Engineering/Bio", "Engineering/Electronic", "Engineering/Mechanical", "Engineering/Nano", "Engineering/Neural", "Esotericism", "Etiquette", "Explosives", "Farming", "First Aid", "Flight", "Forensics", "Geology", "Gunsmith", "History", "Hyperphysics", "Chemistry", "Immunity", "Impersonate", "Intimidate", "IT", "Jury-Rig", "Law", "Leadership", "Linguistics", "Lip Reading", "Martial Arts", "Math", "Medicine", "Meditation", "Mining", "Navigation", "Parapsychology", "Physics", "Pilot Aircraft", "Pilot Balloon", "Pilot Grav", "Pilot Mech", "Pilot Nautical", "Pilot Rotor", "Pilot Spacecraft", "Pilot Subnautical", "Psi Shielding", "Psychology", "Rad Reading", "Rad Shielding", "Resolve", "Ride Beast", "Ride Bike", "Robotics", "Running", "Sail", "Scanners & Sensors", "Seduce", "Senses", "Shield Use", "Sign Language", "Sleight of Hand", "Stealth", "Streetwise", "Surgery", "Swimming", "Swindle", "Taunt", "Teaching", "Tracking & Hunting", "Trapping & Fishing", "Warfare", "Weight Lifting", "WS Archery", "WS Artillery", "WS Axe", "WS Blade", "WS Blaster", "WS Bludgeon", "WS Flexible", "WS Handgun", "WS Launcher", "WS Paired Melee", "WS Paired Ranged", "WS Parry", "WS Polearm", "WS Rifle", "WS Staff", "WS Swordsmanship", "WS Thrown", "WS Two Handed", "WS Zen", "Xenobiology", "Xenosophontology", "Xenotechnology", "Zero G", "Zoology"]


##################################################
# Natural Abilities & Disabilities
##################################################
def get_natural():
    print(f"Strength: {0}\n"
          f"Speed   : {2}\n"
          f"Stamina : {d(6) + d(6)}\n"
          f"Smarts  : {d(6) + d(6)}\n")

    age = random.randint(11, 100)
    if age == 100:
        age = 100 + d(6) * d(100)
    sex = "male" if d(2) == 1 else "female"

    ht = d(6) * d(6) + d(6)
    ht += 165 if sex == "male" else 155
    wt = ht * (20 + d(6) + d(6) + d(6) + d(6) + d(6) + d(6)) / 100

    bmi = wt / ((ht / 100) ** 2)
    match bmi:
        case bmi if bmi < 18.5:
            bmi_class = "underweight"
        case bmi if bmi < 25:
            bmi_class = "normal"
        case bmi if bmi < 30:
            bmi_class = "overweight"
        case bmi if bmi < 35:
            bmi_class = "obese"
        case _:
            bmi_class = "morbidly obese"

    print(f"Age     : {age} years\n"
          f"Sex     : {sex}\n"
          f"Height  : {ht} cm\n"
          f"Weight  : {int(wt)} kg\n"
          f"BMI     : {bmi:.2f} ({bmi_class})\n"
          f"Rads    : {(d(6) - 1) * d(6)}\n")

    abi = []
    dis = []

    for skill in SKILLS:
        r = random.randint(1, 6) + random.randint(1, 6)
        if r == 2:
            dis.append(skill)
        elif r == 12:
            abi.append(skill)

    abi = '\n  '.join(abi)
    dis = '\n  '.join(dis)
    print(f"Natural abilities:\n  {abi}\nNatural disabilities:\n  {dis}")


def d(x: int) -> int:
    return random.randint(1, x)


if __name__ == "__main__":
    get_natural()
