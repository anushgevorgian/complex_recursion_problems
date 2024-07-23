def recursive_sum(ls):
    if not ls:
        return 0
    if len(ls) == 1:
        return ls[0]
    return recursive_sum(ls[1:]) + ls[0]

print(recursive_sum([1,2,3,4,5,6]))

