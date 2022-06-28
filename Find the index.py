def find_target(array, target: int) -> int:
    """
    return the index of the target.
    -1 if the target is not in array
    """
    for index, rev_index in enumerate(range(len(array) - 1, -1, -1)):
        if sorted(array)[index] == target:
            return index
        elif sorted(array)[rev_index] == target:
            return rev_index
    return -1

lista = [4, 3, 6, 1, 8, 11, 8]

print(find_target(lista, 201))
print(sorted(lista))