#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Ice Cream Parlor

https://www.hackerrank.com/monthly/challenges/icecream-parlor


"""

from itertools import combinations

test_cases = int(raw_input())

for test_case in range(test_cases):
    dollars = int(raw_input())
    total_flavors = int(raw_input())  # unused variable
    flavors_costs = raw_input()
    # string transformed into an array of ints
    flavors_costs = [int(x) for x in flavors_costs.split(' ')]

    # generation of combinations of 2 flavors
    flavors_combinations = combinations(flavors_costs, 2)

    for flavors_tuple in flavors_combinations:
        # two distinct flavors whose cost equals `dollars`
        #if ((flavors_tuple[0] + flavors_tuple[1]) == dollars):
        if ((flavors_tuple[0] + flavors_tuple[1]) == dollars):
            # get the index in flavors_costs for the first flavor
            first_flavor = flavors_costs.index(flavors_tuple[0])
            # get the index in flavors_costs for the second flavor.
            # since both flavors might cost the same, second_flavor must be
            # searched discarding the position of first_flavor
            second_flavor = flavors_costs.index(flavors_tuple[1],
                                                first_flavor + 1)
            # indices are indexed from 1
            print("{} {}".format(first_flavor + 1, second_flavor + 1))
            # unique solution
            break
