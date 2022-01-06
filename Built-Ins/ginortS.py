L, U, O, E = [], [], [], []

for i in sorted(input()):
    if i.isalpha():
        x = U if i.isupper() else L
    else:
        x = O if int(i) % 2 else E
    x.append(i)

print("".join(L + U + O + E))