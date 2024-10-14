
def compute_values(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    return i, j, k

# Test cases
test_cases = [
    (3, 5, 7),
    (3, 7, 5),
    (5, 3, 7),
    (5, 7, 3),
    (7, 3, 5),
    (7, 5, 3)
]
results = [compute_values(i, j, k) for i, j, k in test_cases]
print(results)
