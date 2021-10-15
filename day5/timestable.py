def timestable():
    i = 9
    j = 1
    while i >= 1:
        while j <= 9:
            result = i * j
            print(j, "*", i, "=", '%-3d' % result, end="    ")
            j = j + 1
            if j - 1 == 9:
                print()
        i = i - 1
        j = 1
    print("\nend.")

timestable()