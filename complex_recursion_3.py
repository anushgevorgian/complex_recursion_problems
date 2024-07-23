def recursive_isascending(ls):
    if not ls:
        return False
    elif len(ls) == 1 or (ls[0] <= ls[1]):
        return True
    recursive_isascending(ls[1:])
    return ls[0] <= ls[1]

print(recursive_isascending([0,2,3,6]))