# Set: met accolades/krulhaken { }
# 1. Geen dubbele waarden (worden genegeerd)
# 2. Geen vaste volgorde
# 3. Kan aangepast worden
s = {"groen", "rood", "blauw", "groen"}
s.add("paars")
print(s)

# Lijst: met blokhaken [ ]
# 1. Wel dubbele waarden (blijven behouden)
# 2. Wél een vaste volgorde
# 3. Kan aangepast worden (is mutable)
l = ["groen", "groen", "blauw", "blauw", "rood"]
l.append("geel")                                        # Voeg toe aan het einde
l.insert(0, "oranje")
print(l)

# Tuple: met ronde haken ( )
# 1. Wél dubbele waarden (blijven behouden)
# 2. Wél een vaste volgorde
# 3. Kan niet aangepast worden (is immutable)
t = ("blauw", "geel", "groen")
print(t)

# Een tuple kan niet aangepast worden. Dit kan dus NIET.
# t[0] = "rood"         x
# t.add("rood")         x
# t.append("rood")      x

# Dictionary: met krulhaken/accolades { }
# 1. Key-value paren (gelabelde data)
# 2. Dubbele values mogen voorkomen, dubbele keys niet
# 3. Wél een vaste volgorde
# 4. Kan aangepast worden
# Het woord dictionary betekent woordenboek; net als in een woordenboek zou het
# vreemd zijn als we een woord twee keer toe zouden voegen, terwijl woorden wel
# (ongeveer) dezelfde betekenis kunnen hebben.

d = {
    "rood": 1,
    "blauw": 2,
    "groen": 3
}

# Voeg een nieuwe waarde toe
d["geel"] = 4
# Pas de waarde van blauw aan naar 5
# (let op: het resultaat hangt er vanaf of het huidige element bestaat)
d["blauw"] = 5