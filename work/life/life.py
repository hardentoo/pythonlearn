#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 bsd <hardenedgentoo@gmail.com>
#
# Distributed under terms of the MIT license.


def cout (a):
    for i in range (0, len(a)-1):
        print(a[i])

n = 10
m = 10

a = [[0 for x in range(m)] for y in range(n)]
b = [[0 for x in range(m)] for y in range(n)]

a[5][5] = 1
a[5][6] = 1
a[5][7] = 1

for k in range (1):
    for i in range (2, n-1):
        for j in range (2, m-1):
            count = 0
            count += a[i-1][j-1] + a[i-1][j] + a[i-1][j+1]
            count += a[i][j-1]   + a[i][j]   + a[i][j+1]
            count += a[i+1][j-1] + a[i+1][j] + a[i+1][j+1]

            if (count == 3):
                b[i][j] = 1
            else:
                b[i][j] =0

    for i in range (1, n):
        for j in range(1, m):
            a[i][j] = b[i][j]

cout(b)
