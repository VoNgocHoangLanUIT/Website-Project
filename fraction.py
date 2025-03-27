def add_fractions(a_num, a_den, b_num, b_den):
    result_num = a_num * b_den + b_num * a_den
    result_den = a_den * b_den
    return result_num, result_den

print(add_fractions(1, 2, 1, 3))  # (5, 6)
