# Hoe ziet het opsommen van getallen eruit in Python?
# Bereken de som van getallen 1-100 (in wiskunde met sigma-notatie)
# We beginnen met tellen vanaf 0.
c = 0

# Tel elk losse getal bij elkaar op
for i in range(1, 101):
    # Zelfde als c = c + i
    c += i

# Print het resultaat
print(c)

# We kunnen ook de som berekenen aan de hand van een formule.
# Maak een lijstje met getallen van 1-500. We slaan min en max
# even op om later te printen.
min = 1
max = 500
r = [x for x in range(min, max+1)]

# Bereken de lengte van de lijst
n = len(r)

# We hebben 1/2 * n paren, die allemaal dezelfde som hebben (hoogste + laagste getal).
som = (1/2) * n * (r[0] + r[n-1])

print(f"De som van alle getallen tussen {min} en {max} is {som}")