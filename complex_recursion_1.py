new_list = []
def recursive_flatten(nested_ls):
    for element in nested_ls:
        if type(element) is list:
                recursive_flatten(element)

        else:
            new_list.append(element)
    return new_list

print(recursive_flatten([[1,2,["random"],3],4, 5, ["google"], [5, 6]]))