def nummer_palindroom(n):
    """
    Bepaal of een getal een palindroom is (spiegelgetal).
    We doen dit recursief.

    Bijv:
                True                    -> base case
    1           True (omgekeerd 1)      -> base case
    10          False (omgekeerd 01)
    2002        True (omgekeerd 2002)   -> n[0] == n[-1] AND nummer_palindroom(n[1:-1])

    :param n:       Gegeven getal
    :return bool:   Is het een palindroom?
    """

    # Comment dit uit om te zien welk deel van het nummer over is bij de aanroep.
    # print(n)

    # Base case: string is leeg (bijv. omdat alle paren gematcht zijn)
    if n == "" or len(n) == 1:
        return True

    # Zijn het eerste element en het laatste element gelijk?
    # Als dat niet het geval is weten we meteen dat het geen palindroom is.
    if n[0] != n[-1]:
        return False

    # Haal het eerste en laatste elementje eraf en check de rest
    return nummer_palindroom(n[1:-1])


# False
assert not nummer_palindroom(str(10))

# True
assert nummer_palindroom(str(99))

# True
assert nummer_palindroom(str(2002))

# True
assert nummer_palindroom(str(123456787654321))