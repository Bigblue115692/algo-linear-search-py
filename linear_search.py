def linear_search(value_to_find, array_to_search_through):
    # your code here
    for x, y in enumerate(array_to_search_through):
        if y == value_to_find:
            return x
    pass

def linear_search_global(value_to_find, array_to_search_through):
    result = []
    for x, y in enumerate(array_to_search_through):
        if y == value_to_find:
            result.append(x)
    
    return result
    # your code here
    pass