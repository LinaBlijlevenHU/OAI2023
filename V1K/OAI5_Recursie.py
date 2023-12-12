def faculteit(n):
    """
    Bereken recursief de faculteit van een gegeven getal.

    :param  int:    Gegeven getal
    :return int:    Resultaat
    """
    print(f"{n}")

    # Base case: 1! is gewoon gelijk aan 1.
    if n == 1:
        return 1

    return n * faculteit(n-1)

print(faculteit(8))
