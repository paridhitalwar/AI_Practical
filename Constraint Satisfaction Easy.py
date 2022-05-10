import itertools
def solve2():
    letters = ('c', 'r', 'o', 's', 'a', 'd', 'n', 'g', 'e')
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sol['c'] == 0 or sol['r'] == 0:
            continue
        cross = 10000 * sol['c'] + 1000 * sol['r'] + 100 * sol['o'] + 10 * sol['s'] + sol['s']
        roads = 10000 * sol['r'] + 1000 * sol['o'] + 100 * sol['a'] + 10 * sol['d'] + sol['s']
        danger = 100000 * sol['d'] + 10000 * sol['a'] + 1000 * sol['n'] + 100 * sol['g'] + 10 * sol['e'] + sol['r']
        if cross + roads == danger:
          print(" cross"," roads"," danger")
          return cross, roads, danger
print(solve2())
