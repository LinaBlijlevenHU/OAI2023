# Sets in Python
# Een set aanmaken
kleuren = {"groen", "blauw", "rood"}

# Een lijst met dubbele elementen
dubbele_kleuren = ["groen", "groen", "rood", "groen", "rood", "blauw", "groen"]

print(kleuren)
print(dubbele_kleuren)

# Casten naar een set
kleurenset = set(dubbele_kleuren)
print(f"Lijst met dubbele waarden naar set: {kleurenset}")

print(set(["groen", "blauw", "rood"]) == set(["groen", "groen", "rood", "groen", "rood", "blauw", "groen"]))