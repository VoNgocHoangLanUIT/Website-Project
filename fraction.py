from math import gcd

def add_fractions(a_num, a_den, b_num, b_den):
    result_num = a_num * b_den + b_num * a_den
    result_den = a_den * b_den
    return simplify(result_num, result_den)

def simplify(num, den):
    greatest = gcd(num, den)
    return num // greatest, den // greatest

print(add_fractions(1, 2, 1, 3))  # (5, 6)
print(add_fractions(2, 4, 2, 4))  # (1, 1)
