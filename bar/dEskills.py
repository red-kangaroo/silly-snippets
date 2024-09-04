# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random

SKILLS = ["Acrobacy","Arcologistics","Argue","Architecture","Armour Penetration","Armour Repair","Armour Use","Arts/Performance","Arts/Visual","Assassin","Astrogation","Biology","Botany","Brawl","Brewing","Bureaucracy","Business","Camping","Climbing","Command","Communications","Cooking","Craft/Earth","Craft/Metal","Craft/Wood","Cyber Warfare","Cybernetics","Disguise & Camouflage","Dodge","Drive Burrower","Drive Heavy Machinery","Drive Hovercraft","Drive Railed","Drive Tracked","Drive Walker","Drive Wheeled","Drive Winter","Engineering/Bio","Engineering/Electronic","Engineering/Mechanical","Engineering/Nano","Engineering/Neural","Esotericism","Etiquette","Explosives","Farming","First Aid","Flight","Forensics","Geology","Gunsmith","History","Hyperphysics","Chemistry","Immunity","Impersonate","Intimidate","IT","Jury-Rig","Law","Leadership","Linguistics","Lip Reading","Martial Arts","Math","Medicine","Meditation","Mining","Navigation","Parapsychology","Physics","Pilot Aircraft","Pilot Balloon","Pilot Grav","Pilot Mech","Pilot Nautical","Pilot Rotor","Pilot Spacecraft","Pilot Subnautical","Psi Block","Psychology","Resolve","Ride Beast","Ride Bike","Robotics","Running","Sail","Scanners & Sensors","Seduce","Senses","Shield Use","Sign Language","Sleight of Hand","Stealth","Streetwise","Surgery","Swimming","Swindle","Taunt","Teaching","Tracking & Hunting","Trapping & Fishing","Warfare","Weight Lifting","WS Archery","WS Artillery","WS Axe","WS Blade","WS Blaster","WS Bludgeon","WS Flexible","WS Handgun","WS Launcher","WS Paired Melee","WS Paired Ranged","WS Parry","WS Polearm","WS Rifle","WS Staff","WS Swordsmanship","WS Thrown","WS Two Handed","WS Zen","Xenobiology","Xenosophontology","Xenotechnology","Zero G","Zoology","Psi Shield"]


##################################################
# Natural Abilities & Disabilities
##################################################
def get_natural():
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


if __name__ == "__main__":
    get_natural()
