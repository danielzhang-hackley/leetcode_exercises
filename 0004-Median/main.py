def rec_med(a, b, a_l, b_l, a_r, b_r, med_idx):
    """
    a and b are arrays, recursively obtained; subsequences of num1 and num2, respectively
    a_l is the index at which the leftmost element of a would be in num1
    likewise for b_l, a_r (rightmost), b_r
    """
    if len(a) + len(b) == 2:
        return (sum(a) + sum(b)) / 2

    elif len(a) + len(b) == 1:
        return sum(a) + sum(b)

    a_med_idx = len(a) // 2 + a_l
    b_med_idx = len(b) // 2 + b_l

    if a_med_idx == med_idx:
        return a[len(a) // 2]

    if b_med_idx == med_idx

    # 898 127 -531

    return rec_med()