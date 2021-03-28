#!/usr/bin/env python3

# %%
def equals(x, y):
    return x == y

def hamming(x, y):
    assert len(x) == len(y) 
    nmm = 0
    for i in range(0, len(x)):
        if x[i] != y[i]:
            nmm += 1
    return nmm

a = [1, 0, 0, 0, 1, 1, 0]
b = [1, 1, 0, 0, 1, 0, 0]

print(equals(a, a))
print(equals(a, b))

print(hamming(a, b))

# %% [markdown]
"""
# Some heading
## Some sub-heading

This is some sweet descriptive text!
"""
# %%
import datetime as d

def ed1(x, y):
    if len(x) == 0: return len(y)
    if len(y) == 0: return len(x)
    delt = 1 if x[-1] != y[-1] else 0
    diag = ed1(x[:-1], y[:-1]) + delt
    vert = ed1(x[:-1], y) + 1
    horz = ed1(x, y[:-1]) + 1
    return min(diag, vert, horz)

st = d.datetime.now()
ed1("Shakespeare", "shake spear")
print((d.datetime.now() - st).total_seconds())

# %%

import numpy as np

def edit(x, y, cost={'m': 0, 's': 1, 'i': 1, 'd': 1}):
    D = np.zeros((len(x) + 1, len(y) + 1), dtype=int)

    # for the empty word, costs match the length of the other string
    D[0, 1:] = range(1, len(y) + 1)
    D[1:, 0] = range(1, len(x) + 1)
    
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            delta = cost['m'] if x[i-1] == y[j-1] else cost['s']
            D[i, j] = min(
                D[i-1, j] + cost['d'],
                D[i, j-1] + cost['i'],
                D[i-1, j-1] + delta
            )
    
    print(D)

    return D[len(x), len(y)]

def nw(x, y, d, sim):
    D = np.zeros((len(x) + 1, len(y) + 1), dtype=int)

    # for the empty word, costs match the length of the other string
    D[0, 1:] = range(1, len(y) + 1); D[0, 1:] *= d
    D[1:, 0] = range(1, len(x) + 1); D[1:, 0] *= d

    for i in range(1, len(x)):
        for j in range(1, len(y)):
            cs = D[i-1, j-1] + sim(x[i], y[j])
            cd = D[i-1, j] + d
            ci = D[i, j-1] + d
            D[i,j] = max(cs, cd, ci)

    print(D)
    return D[len(x)][len(y)]

def sim(a: str, b: str):
    if a.casefold() == b.casefold():
        return 1
    else:
        return -1

print(edit("Shakespeare", "shake spear"))
print(nw("ATTACA", "ATGCT", -1, sim))
# %%

def dtw(x: list, y: list, d) -> float:
    D = np.full((len(x) + 1, len(y) + 1), np.inf, dtype=float)
    D[0, 0] = 0
    
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            cost = d(x[i], y[j])
            D[i, j] = cost + min(D[i-1, j], 
                                 D[i, j-1],
                                 D[i-1, j-1])
    
    return D[len(x)][len(y)]
