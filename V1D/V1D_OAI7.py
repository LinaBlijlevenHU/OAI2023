import matplotlib.pyplot as plt
import random

lengtes = [1.70, 1.90, 1.81, 1.85, 1.81, 1.86, 1.70, 1.94, 1.80, 1.95, 1.96, 1.99]

def gemiddelde(lst):
    return sum(lst) / len(lst)

def variantie(lst):
    m = gemiddelde(lst)

    verschillen = []

    for e in lst:
        verschillen.append((e - m)**2)

    return sum(verschillen) / len(verschillen)

def standaardafwijking(lst):
    # x^1/2 is zelfde als wortel x
    return variantie(lst)**0.5

print(f"De gemiddelde lengte in V1D is {gemiddelde(lengtes)}")
print(f"De variantie is {variantie(lengtes)} en de standaardafwijking {standaardafwijking(lengtes)}")

plt.hist(lengtes, bins=20, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.show()

langer = 0
n = 10
grens = 1.8

for i in range(n):
    if random.choice(lengtes) > grens:
        langer += 1

print(f"In een steekproef van {n} studenten zijn er {langer} langer dan {grens}.")
