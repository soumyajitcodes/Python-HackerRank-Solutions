n = int(input())
country = []
country = set(country)
while n:
    i = input()
    country.add(i)
    n -= 1
print(len(country))