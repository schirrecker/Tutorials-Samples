def gen():
    yield 1
    yield 2
    yield 3

g = gen()

next(g)
