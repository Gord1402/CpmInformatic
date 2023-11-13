n = int(input())

count = 0

for i in range(n):
    num_str = input()
    for j in range(0, len(num_str) - 1):
        if (int(num_str[j]) % 2) == (int(num_str[j + 1]) % 2):
            break
    else:
        count += 1

print(count)
