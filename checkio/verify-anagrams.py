#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 hardentoo <hardenedgentoo@gmail.com>
#
# Distributed under terms of the MIT license.
#
# https://py.checkio.org/mission/verify-anagrams/
#


def checkio (str1, str2):

    str3 = ''

    for x in str1.lower().split():
        str3 += x

    str4 = ''

    for x in  str2.lower().split():
        str4 += x

    if (sorted(str3) == sorted(str4)):
        return True
    else:
        return False

print (checkio('AA  Affaaa', 'aaa    ffAAA'))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
