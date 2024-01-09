"""
fibonacci.py

Dit bestand demonstreert het verschil tussen implementaties van de
Fibonacci-reeks.
"""

# 0, 1, 1, 2, 3, 5, 8

# Met recursie
def fibonacci_recursief(n):
    print(f"Bereken {n}de getal in de reeks van Fibonacci")

    # Base case(s)
    if n == 1: return 0
    elif n == 2: return 1

    # Recurrente betrekking
    else:
        return fibonacci_recursief(n - 1) + fibonacci_recursief(n - 2)

# Zonder recursie
def fibonacci(n):
    # De fibonaccireeks begint met 0 en 1
    vorige = [0, 1]

    if (n == 1):
        return 0
    elif (n == 2):
        return 1
    else:
        for i in range(3, n+1):
            print(f"We berekenen nu fibonacci getal {i} met de vorige twee getallen {vorige}: {sum(vorige)}")
            # Bereken het huidige fibonacci getal
            som = sum(vorige)

            # Kopieer een van de vorige getallen
            vorige[0] = vorige[1]

            # Zet onze nieuwe som erin als laatste getal
            vorige[1] = som

    return vorige[1]

#print(fibonacci(15))
print(fibonacci_recursief(15))