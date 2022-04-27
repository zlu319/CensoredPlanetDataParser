#!/usr/bin/env python3

# requires at least python 3.8 for this function
from math import comb

print("--- This Program Conducts Fisher's Exact Test with large numbers ---")

input_str = input("Please input a, b, c, d separated by commas: ")
abcd_vals = [int(x.strip()) for x in input_str.split(',')]
if len(abcd_vals) != 4:
    print("error, input four values, not", len(abcd_vals), "values")
else:
    a, b, c, d = abcd_vals
    p_value = comb(a + b, a) * comb(c + d, c) / comb(a + b + c + d, a + c)
    print("p-value is ", p_value)


