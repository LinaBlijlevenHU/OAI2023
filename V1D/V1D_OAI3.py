# 1. ontvang twee positieve getallen
def euclides(g1, g2):
    # 2. noem het grootste getal a en het kleinste getal b
    a, b = max(g1, g2), min(g1, g2)

    # 3. herhaal stap 4 zolang a groter of gelijk is aan b
    while (a >= b):
        # 4. trek b af van a
        a -= b

    # 5. als a gelijk is aan 0, geef dan b terug
    if (a == 0):
        return b

    # 6. als a ongelijk is aan 0, ga naar stap 1 met b en (het restant van) a
    return euclides(b, a)

print(euclides(42, 7))










