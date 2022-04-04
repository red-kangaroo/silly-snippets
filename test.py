import itertools

dice = [2, 3, 4, 5, 6, 8, 10, 12]

if __name__ == "__main__":
    cnt = 0
    for d in itertools.product(dice, repeat=2):
        print(f"d{d[0]}, d{d[1]}    {sum(d)}")
        # print(f"{d[0]},{d[1]},{sum(d)}")

        if sum(d) >= 6:
            cnt += 1

    print(f"\nFound {cnt} instances with value of 6+.")
