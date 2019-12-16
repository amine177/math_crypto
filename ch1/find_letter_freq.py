#!/bin/env python3


from collections import defaultdict


def print_freq(s):
    freqs = defaultdict(lambda  : 0)
    for i in s:
        if not i.isspace():
            freqs[i] += 1

    for i in freqs.keys():
        print("{} : {}%".format(i, freqs[i] * 100 / len(s)))

if __name__ == "__main__":
    print('input:')
    stopword = ''
    print_freq('\n'.join(iter(input, stopword)).replace(' ', '').replace('\n', ''))
