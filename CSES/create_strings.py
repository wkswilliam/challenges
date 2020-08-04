from itertools import permutations 
r = set()
for s in permutations(input()):
    r.add(''.join(s))
print(len(r))
for s in sorted(r):
    print(s)