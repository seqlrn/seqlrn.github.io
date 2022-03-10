#!/usr/bin/env python3

import fileinput
from jiwer import wer

lookup = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

refs = list()
hyps = list()

ignored = 0

for line in fileinput.input():
    if 'null' in line:
        ignored = ignored + 1
        continue
    try:
        f, hyp = line.rstrip().split(maxsplit=1)
        d, _ = f.split('_', 1)
        refs.append(lookup[int(d)])
        hyps.append(hyp)
    except:
        pass

print(wer(refs, hyps))

if ignored:
    print("ignored {} null-lines".format(ignored))
