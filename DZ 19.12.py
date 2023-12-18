N = int(input())

maximum = ""

for _ in range(N):
    number = bin(int(input()))[2:]
    if len(maximum) < len(number):
        maximum = number

print(int(maximum, 2))
