# lst = [::stap]
# lst = [start:eind]
# lst = [start:eind:stap]

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Hele lijst, equivalent van print(lst)
print(lst[0:len(lst):1])

# Vanaf tweede element, equivalent van lst[1:len(lst)]
print(lst[1:])

# T/m index 5 (start=0, eind=5, stap=1)
print(lst[:5])

# Print alles behalve het laatste element
# T/m index -1 (start=0, eind=-1, stap=1)
print(lst[:-1])

# Omgekeerde lijst (stappen van -1, van start tot eind)
print(lst[::-1])