# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path
from statistics import median

##################################################
# PSNR/SSIM Exporter
##################################################
for path in Path('.').glob('*.txt'):
    with open(str(path)) as f:
        if 'psnr' in path.name:
            pmin = 999
            pmax = -999
            ptot = 0
            pno = 0
            pmean = list()

            for line in f:
                res = re.search(r"psnr_avg:([0-9]+\.[0-9]+)", line)
                if res is None:
                    continue

                nbr = float(res.group(1))
                pmean.append(nbr)
                pmin = min(pmin, nbr)
                pmax = max(pmax, nbr)
                ptot += nbr
                pno += 1

            print(f"{path.stem} {pmin} {pmax} {ptot/pno:.2f} {median(pmean)}")

        elif 'ssim' in path.name:
            ssmin = 999
            ssmax = -999
            sstot = 0
            ssno = 0
            ssmean = list()

            for line in f:
                res = re.search(r"All:([0-9]\.[0-9]+)", line)
                if res is None:
                    continue

                nbr = float(res.group(1))
                ssmean.append(nbr)
                ssmin = min(ssmin, nbr)
                ssmax = max(ssmax, nbr)
                sstot += nbr
                ssno += 1

            print(f"{path.stem} {ssmin:.2f} {ssmax} {sstot/ssno:.2f} {median(ssmean):.2f}")
