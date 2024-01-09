import matplotlib.pyplot as plt
import random

lengtes = [1.95, 1.80, 1.70, 1.82, 1.69, 1.70, 1.83, 1.83, 1.81, 1.77, 1.88, 1.90, 1.74, 1.85, 1.74]

def gemiddelde(lst):
    return sum(lst) / len(lengtes)

def variantie(lst):
    # gemiddelde
    m = gemiddelde(lst)

    kwadraten = []

    for lengte in lengtes:
        verschil = lengte - m
        kwadraten.append(verschil**2)

    # kwadraten = [(lengte - m)**2 for e in lst]

    # delen door n
    return sum(kwadraten) / len(kwadraten)

def standaarddeviatie(lst):
    return variantie(lst) ** 0.5

print(f"De gemiddelde student in deze klas is {gemiddelde(lengtes)}")
print(f"De variantie is {variantie(lengtes)} en de standaarddeviatie is {standaarddeviatie(lengtes)}")

#plt.hist(lengtes, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
#plt.show()

# Simpel scriptje om te sampelen
# We vragen 10 leerlingen en checken hoeveel er >180 zijn.
langer = 0

for i in range(10):
    lengte = random.choice(lengtes)

    if lengte > 1.80:
        langer += 1

print(f"Er zijn {langer} studenten langer dan 180 als je random leerlingen selecteert.")