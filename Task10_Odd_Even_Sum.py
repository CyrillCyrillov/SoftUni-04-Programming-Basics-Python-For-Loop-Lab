n = int(input())
odd_sum = 0
even_sum = 0

for i in range(1, n+1):
    next = float(input())
    if i % 2 == 0:
        even_sum += next
    else:
        odd_sum += next
if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum:.0f}")
else:
    print("No")
    print(f"Diff = {abs(odd_sum - even_sum):.0f}")

