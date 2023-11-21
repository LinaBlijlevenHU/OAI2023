# Bereken de som van getallen 1-100 (in wiskunde met sigma-notatie)
c = 0

for i in range(1, 101):
    c += i

print(c)

# Bereken met de formule
# Maak een lijstje met getallen van 1-500
min = 1
max = 500
r = [x for x in range(min, max+1)]

# Bereken de lengte van de lijst
n = len(r)

# Bereken het sommetje
som = (1/2) * n * (r[0] + r[n-1])

print(f"De som van alle getallen tussen {min} en {max} is {som}")