import string

base = string.digits + string.ascii_lowercase


def from_base(number):
    power = 0
    result = 0
    for c in number[::-1]:
        result += base.index(c) * (37 ** power)
        power += 1
    return result


print(from_base(input()) + from_base(input()))
