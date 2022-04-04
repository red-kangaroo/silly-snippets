# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

dice = [2, 3, 4, 5, 6, 8, 10, 12]


class Test(object):
    items = {'a': 1}

    def __getattr__(self, item):
        result = self.items.get(item, None)
        if result is not None:
            return result

        raise AttributeError


if __name__ == "__main__":
    cnt = 0
    for d in itertools.product(dice, repeat=2):
        print(f"d{d[0]}, d{d[1]}    {sum(d)}")
        # print(f"{d[0]},{d[1]},{sum(d)}")

        if sum(d) >= 6:
            cnt += 1

    print(f"\nFound {cnt} instances with value of 6+.")

    # qry = Test()
    # print(qry.a)
    # print(qry.b)
