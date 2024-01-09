def faculteit(n):
    """
    Bereken (recursief) de faculteit van een gegeven getal

    :param  n:  Getal
    :return:    Getal!
    """
    # Base case: probleem is klein genoeg om op te lossen
    if n == 1:
        return 1

    # Recursie/recursion/recurrente betrekking
    return n * faculteit(n - 1)

print(faculteit(10))


def rekenkundig_recursief(n):
    """
    Bereken recursief de formule y = 3n + 5

    :return
    """
    # Base case: 0de getal is 5
    if n == 0:
        resultaat = 5
        print(f"Het {n}de getal in de reeks is {resultaat}")
        return resultaat

    # Recurrente betrekking (vorige getal + 3)
    resultaat = rekenkundig_recursief(n-1) + 3

    # Print voor de overzichtelijkheid
    print(f"Het {n}de getal in de reeks is {resultaat}")

    return resultaat


print(rekenkundig_recursief(5))
