# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import itertools

dice = [2, 3, 4, 5, 6, 8, 10, 12]


class Test(object):
    items = {'a': 1}

    def __getattr__(self, item):
        result = self.items.get(item, None)
        if result is not None:
            return result

        raise AttributeError


def time_percentage() -> float:
    """Get percentage of the current time point within the hour

    :return: percentage <0, 1>
    """
    tm_now = datetime.datetime.now()
    cur_sec = tm_now.minute * 60 + tm_now.second
    tm_perc = cur_sec / 3600

    return tm_perc


if __name__ == "__main__":
    from string import ascii_uppercase

    for c in range(10):
        print(f"| {c} ||")
