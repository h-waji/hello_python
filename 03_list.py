r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))
print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'Miku Rin Len'
to_split = s.split(' ')
print(to_split)

x = '☆彡'.join(to_split)
print(x)

# print(help(list))

# ----- copy -----
x = [1, 2, 3, 4, 5]
y = x.copy()
print('x', x)
print('y', y)

print(id(x))
print(id(y))
