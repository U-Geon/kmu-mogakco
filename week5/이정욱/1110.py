n = int(input())
first = n

cycle = 0

while True:
    cycle += 1
    if n < 10:
        n = int(str(n) + str(n))
    else:
        n = int(str(n)[1] + str((n//10 + n%10)%10))
    if n == first: break

print(cycle)

