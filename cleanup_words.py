#!/usr/bin/env python
# -*- coding:utf-8 -*-

from itertools import islice
from re import sub
import sys
import csv

LETTERS = dict({(v, k) for (k, v) in map(lambda x: (x, chr(x)), range(ord('A'), ord('ž')))})


def read_sbsj(path='./data/sbsj.html', skip=16):
    with open(path, 'r', encoding="utf-8", newline="\r\n") as f:
        for line in islice(f, skip, None):
            yield line.strip()


def word(line: str) -> str:
    br_pos = line.find('<br>')
    return sub(r'[^a-žA-Ž ]+', '', line[0:br_pos].split(' ')[0]) if \
        line is not '' and len(line) > 1 and br_pos != 0 else ''


def optimised_word(word: str = '') -> str: return ''.join(sorted(set(word.upper())))


def as_pg_array(word: str = '') -> str: return "{%s}" % ','.join(set(word))


def as_pg_numbers_array(word: str = ''): return "{%s}" % ','.join(
    sorted(set(map(lambda x: str(LETTERS.get(x, -1)), list(word)))))


if __name__ == '__main__':
    w = csv.writer(sys.stdout, quoting=csv.QUOTE_MINIMAL)

    for word, letters in [(word(line), optimised_word(word(line))) for line in read_sbsj() if len(word(line)) > 1]:
        w.writerow([word, as_pg_numbers_array(letters)])
