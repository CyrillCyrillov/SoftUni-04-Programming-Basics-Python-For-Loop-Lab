n = int(input())
left_sum = 0
right_sum = 0
for i in range(1, n+1):
    left_sum += float(input())
for i in range(1, n+1):
    right_sum += float(input())
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum:.0f}")
else:
    print(f"No, diff = {abs((left_sum - right_sum)):.0f}")
