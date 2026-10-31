def katta_son(a, b):
    if a >= b:
        return a
    return b


a, b = map(int, input().split())
print(katta_son(a, b))
