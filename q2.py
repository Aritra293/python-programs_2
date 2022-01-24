def fac(i):
    if i == 0:
        return 1
    return i * fac(i - 1)

i=int(input())
print("factorial is:-")
print(fac(i))


    