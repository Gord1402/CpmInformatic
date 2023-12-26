inp = input()

arr = []

while inp != "":
    try:
        arr.append(int(inp))
    except ValueError:
        print("Необходимо ввести целое число")
    inp = input()

changed = True
while changed:
    changed = False
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            arr[i + 1], arr[i] = arr[i], arr[i + 1]
            changed = True

print(arr)
