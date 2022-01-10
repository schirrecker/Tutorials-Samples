def my_gen(s):
    for l in s:
        yield l

for c in my_gen("hello"):
    print(c)

for c in my_gen((['item1'], ['item2'], ['item3'])):
    print(c)

l = [x for x in range(10)]
#that's list comprehension

g = (x**2 for x in range(10))
# that's an iterator

print(next(g))
print(next(g))
print(next(g))
