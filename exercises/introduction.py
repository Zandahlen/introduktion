"""Övningar på introduction."""


def repeat(string, num):
    """Repeterar en sträng (arg 1) num (arg 2) gånger.

    Returnerar en ny sträng eller en tom sträng om num är negativt.
    """
    if num > 0:
        return(string * num)
    else:
        return(string * 0)


def bouncer(items):
    """Tar bort alla värden i items (arg 1) som evalueras till False."""
    result = []
    for item in items:
        if item:
            result.append(item)
    return result


def rovarsprak(string):
    """Returnerar strängen på rövarspråk.

    * Versaler och gemener ska vara kvar enligt instoppad sträng.
    * Övriga tecken (.,*! etc.) ska vara kvar på samma position.

    `Wikipedia<https://sv.wikipedia.org/wiki/R%C3%B6varspr%C3%A5ket>`
    """
    import re
    string2 = re.sub(r"([bcdfghjklmnpqrstvwxz])", r"\1o\1", string)
    return re.sub(r"([BCDFGHJKLMNPQRSTVWXZ])", r"\1O\1", string2)


def area(width, height):
    """Returnerar arean av en figur med bredden 'width' och höjden 'height'."""
    return(width * height)


def to_seconds(time):
    """Returnerar en float `time` (timmar) till sekunder."""
    return(time * 60 * 60)


def is_of_age(age):
    """Returnerar true om 'age' är större eller lika med 18, annars false."""
    if age >= 18:
        return(True)
    else:
        return(False)


def vowel(character):
    """Returnerar true om 'character' är en vokal, annart false."""
    vowels = 'auoåeiyäöAUOÅEIYÄÖ'
    return character in vowels


def reverse(words):
    """Byter ordning på alla tecken i strängen `words`, returnerar resultatet.

    words = "Hej på dig!" ska till exempel returnera
    strängen "!gid åp jeH".
    """
    return words[::-1]


def overlapping(list1, list2):
    """Returnerar True om listorna har åtminstone ett gemensamt objekt."""
    return any(x in list1 for x in list2)


def is_palindrome(words):
    """Returnerar sant om orden är en palindrom.

    Det vill säga en följd tecken som blir likadan oavsett om den läses
    framlänges eller baklänges, annars false. Ett exempel på palindrom är orden
    'ni talar bra latin' som kan läsas likadant åt båda hållen.
    """
    words = words.lower()
    words = words.replace(" ", "")
    if words[::-1] == words:
        return True
    else:
        return False


def travel_price(distance, consumtion, price):
    """Beräknar och returnerar priset för en resa.

    Resan är `distance` km lång, och görs med en bil som drar `consumption`
    liter bensin per mil då bensinen kostar `price` kr per liter.
    """
    x = (distance * consumtion * price) / 10
    return round(x, 2)


def character_frequency(words):
    """Returnerar ett histogram (dictionary).

    Returnerar en dictionary med varje bokstav i strängen `words` som nyckel
    till ett värde av antalet gånger bokstaven uppkommer i stängen.
    """
#    from string import whitespace
#    for char in words.replace(whitespace, ''):
    chars = {}
    for char in words.replace(' ', ''):
        chars[char] = chars.get(char, 0) + 1
    return chars
