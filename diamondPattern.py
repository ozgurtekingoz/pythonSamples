# coding=utf-8
from __future__ import print_function


def drawDaimond():
    sayi = input("sayı giriniz")
    n = 1
    for x in range(0, sayi):
        for y in range(0, sayi - x):
            print(end=" ")

        for z in range(0, 2 * n - 1):
            print(end="*")

        n += 1
        print()

    n = 1
    for x in range(0, sayi):
        for y in range(0, n + 1):
            print(end=" ")

        for z in range(0, 2 * (sayi - n - 1) + 1):
            print(end="*")

        n += 1
        print()


drawDaimond()
