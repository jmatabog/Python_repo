
def find_min(element):
    """TODO: complete for Step 1"""
    
    for i in element:
        if type(i) != type(1):
            return -1
    if len(element) == 0: 
        return -1
    
    elif len(element) == 1:
        return element[0]
    
    else:
        if element[0] < element[-1]:
            return find_min(element[:-1])
        else:
            return find_min(element[1:])


def sum_all(element):
    """TODO: complete for Step 2"""
    
    for i in element:
        if type(i) != type(1):
            return -1
    if len(element) == 0:
        return -1

    elif len(element) == 1:
        return element[0]
    else:
        return element[0] + sum_all(element[1:])


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    
    jeff = ([])
    for i in character_set:
        if type(i) != type(""):
            return jeff
    set1 = []
    if n <= 1:
        return character_set

    for i in character_set:
        for p in find_possible_strings(character_set, n-1):
            set1.append(i+p)
    return set1