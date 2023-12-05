def find_index_of_minimum(lst, start_index=0):
    """ Vind de locatie van het minimum in lijst lst vanaf een gegeven start_index (int). """
    minimum = lst[start_index]
    index_of_minimum = start_index

    # Doorloop de lijst lst vanaf start_index en
    # update minimum en index_of_minimum waar nodig.
    for i in range(start_index + 1, len(lst)):
        # Huidige element
        el = lst[i]

        # Is het huidige elementje kleiner? Pas dan het minimum aan
        if minimum > el:
            minimum = el
            index_of_minimum = i

    return index_of_minimum

lst = ['E', 'D', 'C', 'B', 'A']
start_index = 0

# Index van het kleinste elementje staat op
print(find_index_of_minimum(lst))

# Na de swap krijgen we deze lijst
lst = ['A', 'D', 'C', 'B', 'E']
start_index = 1

print(find_index_of_minimum(lst, ))

# Na de tweede swap
lst = ['A', 'B', 'C', 'D', 'E']
start_index = 2

min_index = find_index_of_minimum(lst, start_index)
print(min_index)

if (min_index == start_index):
    print("Dit element staat al op de juiste plek.")