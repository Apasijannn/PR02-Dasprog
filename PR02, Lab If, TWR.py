
print('1 2 3 4 5 6 7')
a = [1, 2, 3, 4, 5, 6, 7]
b = int(input())
c = int(input())
d, e, f = map(int, input().split())

for i in range(c):
    a = a[-b:] + a[:-b]

print(a[d], a[e], a[f])





