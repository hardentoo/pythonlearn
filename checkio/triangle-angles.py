#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://py.checkio.org/mission/triangle-angles/

import math


def checkio(a, b, c):

    if(a >= b + c or  b >= a + c or c >= a + b):
        return [0, 0, 0]

    return sorted ( [ round(math.degrees(math.acos((x[0]**2 + x[1]**2 - x[2]**2)/(2*x[0]*x[1])))) for x in [[a, b, c] ,[b, c, a], [c, a, b]] ] )

    #la = round (math.degrees (math.acos ((c*c + b*b - a*a)/(2*c*b) )))
    #lb = round (math.degrees (math.acos ((a*a + c*c - b*b)/(2*a*c) )))
    #lc = round (math.degrees (math.acos ((a*a + b*b - c*c)/(2*a*b) )))

    #return sorted([la, lb, lc])

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
