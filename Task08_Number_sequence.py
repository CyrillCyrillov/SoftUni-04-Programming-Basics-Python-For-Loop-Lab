import sys
number = int(input())
max = -sys.maxsize
min = sys.maxsize

for i in range(1, number+1):
    next = float(input())
    if next >= max:
        max = next
    if next <= min:
        min = next
print(f"Max number: {max:.0f}")
print(f"Min number: {min:.0f}")

