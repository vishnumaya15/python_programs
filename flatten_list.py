def flatten_list(nested_list):
    flat = []
    for i in nested_list:
        print('i',i)
        if isinstance(i, list):
            print("in if")
            flat.extend(flatten_list(i))
            print(flat,"flat")
            print("out if")
        else:
            print("in else")
            print(i,"else i")
            flat.append(i)
            print(flat,"flat else")
            print("out else")
    return flat

# Example
print(flatten_list([1, [2, [3, 4], 5], 6])) 