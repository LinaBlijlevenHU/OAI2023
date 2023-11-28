hex_map = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

def hex_to_dec(char):
    '''
    :param char: Character to convert from hexadecimal to a decimal based system
    :return: integer between 1-15
    '''
    if (char >= '0' and char <= '9'):
        return int(char)
    return hex_map[char]

def hex_to_rgb(hex):
    '''
    Convert a hexadecimal value to integer value.
    The first character is a hashtag, which we ignore.
    The second and third character represent red (0-255), 
    fourth and fifth represent green etc.
    :param
    '''
    if (len(hex) != 7 and hex[0] != '#'):
        raise Exception("Da's geen geldige hexcode :(")

    r = hex_to_dec(hex[1]) * 16 + hex_to_dec(hex[2])
    g = hex_to_dec(hex[3]) * 16 + hex_to_dec(hex[4])
    b = hex_to_dec(hex[5]) * 16 + hex_to_dec(hex[6])
    return (r, g, b)

hexes = ['#FF0000', '#00FF00', '#0000FF', '40986784957']
print([hex_to_rgb(x) for x in hexes])