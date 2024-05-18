n=0
while True:
    n = n + 1
    if(n%2 != 0):
        continue
    print(f"O ultimo valor de n é: {n}")
    if n > 100:
        break