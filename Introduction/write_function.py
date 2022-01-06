def is_leap(y):
    leap = False

    # Write your logic here

    if y % 400 == 0:
        leap = True
    elif y % 100 == 0:
        leap = False
    elif y % 4 == 0:
        leap = True
    else:
        leap = False

    return leap

year = int(input())
check_leap_year(year)
