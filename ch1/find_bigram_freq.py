#!/bin/env python3


from collections import defaultdict


def print_bigram_freq(s):
    freqs = defaultdict(lambda: 0)
    for i in range(0, len(s) - 1):
        freqs[s[i: i + 2]]  += 1

    freqs1 = {k: v for k, v in sorted(freqs.items(), key=lambda item: item[1], reverse=True)}
    for k in freqs1.keys():
        print("{} : {}%".format(k, freqs1[k] * 100 / (len(s) - 1)))


if __name__ == "__main__":
    print("input:")
    stopword = ''
    print_bigram_freq('\n'.join(iter(input, stopword)).replace('\n', '').replace(' ', ''))
