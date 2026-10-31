n = int(input())
sonlar = list(map(int, input().split()))

kublar = list(map(lambda x: x ** 3, sonlar))
print(kublar)
