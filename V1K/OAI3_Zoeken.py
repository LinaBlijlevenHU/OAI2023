# gegeven getallen A en B
def euclides(a, b):
    # zolang (A ≠ B)
    while (a != b):
        #  als A > B
        if (a > b):
            #  verminder A met B
            a -= b
        #  anders
        else:
            #  verminder B met A
            b -= a
    # retourneer A
    return a

# Extra materiaal: recursieve versie van Euclides
def euclides_recursive(a, b):
    # Base case (we stoppen als de getallen gelijk zijn)
    # In dit geval is a gelijk geworden aan onze grootste gemene deler.
    if (a == b):
        return a

    # De rest van het algoritme:
    # Als a groter is verminderen we a met b
    if (a > b):
        euclides_recursive(a - b, b)
    # Als b groter is verminderen we b met a
    return euclides_recursive(a, b - a)

print(f"Grootste gemene deler van a = 70 en b = 7 is {euclides(70, 7)}")
print(f"Grootste gemene deler van a = 7 en b = 70 is {euclides_recursive(7, 70)}")

def faculteit(n):
    product = 1

    while (n > 1):
        product *= n
        n -= 1

    return product


a = [2**n for n in range(0, 50, 10)]
f = [faculteit(n) for n in range(0, 50, 10)]
print(a)
print(f)



