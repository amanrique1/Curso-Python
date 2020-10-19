def product(*numbers, initial=1):
    total = initial
    for n in numbers:
        total *= n
    return total

print(product(4, 4))
print(product(4, 4, initial=1))
print(product(4, 5, 2, initial=3))

#Check generadores to understand better the yield functionality
def join(*iterables, joiner):
    if not iterables:
        return
    yield from iterables[0]
    for iterable in iterables[1:]:
        yield joiner
        yield from iterable

print(list(join([1, 2, 3], [4, 5], [6, 7], joiner='-')))