########
# SETS #
########
# We maken twee lijsten aan met groen, blauw en rood erin.
# De tweede lijst bevat ook dubbele waarden.
enkel = ['rood', 'groen', 'blauw']
dubbele = ['blauw', 'blauw', 'blauw', 'blauw', 'rood', 'groen', 'groen']

# Zet de lijsten om naar sets van kleuren. Sets herkennen we aan de krulhaken/accolades { }
# De volgorde wordt niet behouden, dubbele waarden worden verwijderd.
kleurenset1 = set(enkel)
kleurenset2 = set(dubbele)
print(kleurenset1)
print(kleurenset2)

# Op het moment dat we een set maken van de lijsten, resulteren ze in dezelfde set.
# Sets kunnen immers geen dubbele waarden hebben.
print(kleurenset1 == kleurenset2)

# Sets kun je ook gebruiken om dubbele waarden te verwijderen uit lijst. De volgorde wordt dan niet behouden.
lijst_zonder_dubbele = list(set(['blauw', 'blauw', 'blauw', 'blauw', 'rood', 'groen', 'groen']))
print(lijst_zonder_dubbele)

# We gebruiken de epsilon ∈ om aan te geven dat iets in een set zit,
# of ∉ om te aan te geven dat iets niet in een set zit.
print('blauw' in kleurenset1)                   # ∈ -> in
print('groen' not in kleurenset2)               # ∉ -> not in

##############
# Werken met #
##############