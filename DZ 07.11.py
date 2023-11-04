from math import sqrt

a, b = int(input()), int(input())

for number in range(a, b + 1):
    divisors = []
    for divider in range(2, int(sqrt(number)) + 1):
        if number % divider == 0:
            if len(divisors) >= 4:
                break
            divisors.append(divider)
            if number // divider != divider:
                divisors.append(number // divider)
    else:
        if len(divisors) != 4:
            continue
        print(number, "|", " ".join(map(str, sorted(divisors, reverse=True))))
