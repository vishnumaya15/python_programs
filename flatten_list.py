def flatten_list(nested_list):
    flat = []
    for i in nested_list:
        if isinstance(i, list):
            flat.extend(flatten_list(i))
        else:
            flat.append(i)
    return flat

# Example
print(flatten_list([1, [2, [3, 4], 5], 6])) 


def flatten(list):
    flatted=[]
    for i in list:
        if isinstance(i,list):
            flatted.extend(flatten(list(i)))
        else:
            flatted.append(i)
    return flatted
print(flatten_list([1, [2, [3, 4], 5], 6])) 