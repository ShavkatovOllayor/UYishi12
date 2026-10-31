n = int(input())
narxlar = list(map(int, input().split()))

selected = list(filter(lambda x: x >= 15000, narxlar))
final_prices = list(map(lambda x: x - 3000, selected))
print(final_prices)
