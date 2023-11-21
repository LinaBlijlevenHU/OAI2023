# Het totaal van de getallen 1-100 (per getal)
# Maak een tellertje aan
c = 0

for i in range(1, 101):
    c += i

print(c)

# Som van getallen 1-100 berekenen (per paar)
# Zet alle getallen van een range in een lijst
getallen = [x for x in range(1, 101)]

# Tel hoeveel getallen er in de lijst staan
n = len(getallen)

som = (1/2) * n * (getallen[0] + getallen[n-1])
print(int(som))