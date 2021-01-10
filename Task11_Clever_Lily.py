years = int(input())
price = float(input())
price_per_toy = int(input())
sum = 0
toys = 0

for i in range(1, years+1):
    if i % 2 == 0:
        sum += ((i / 2 * 10) - 1)
    else:
        toys += 1

sum += (price_per_toy * toys)

if sum < price:
    print(f"No! {price - sum:.2f}")
else:
    print(f"Yes! {sum - price:.2f}")