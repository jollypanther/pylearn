# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# https://projecteuler.net/problem=5
from math import lcm


def f(start, end):
    return lcm(tuple(range(start, end + 1)))
