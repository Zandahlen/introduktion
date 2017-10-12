import pytest
from exercises.introduction import area, bouncer, character_frequency, is_of_age, overlapping, repeat, reverse, rovarsprak, to_seconds, travel_price, vowel, is_palindrome


#@pytest.mark.skip('Completed')
def test_repeat():
    assert repeat("hej", 2) == "hejhej"
    assert repeat("då", -1) == ""
    assert repeat("abc", 8) == "abcabcabcabcabcabcabcabc"
    assert repeat("ab cd ef ", 2) == "ab cd ef ab cd ef "


#@pytest.mark.skip('Not implemented yet.')
def test_bouncer():
    assert bouncer([7, "ate", "", False, 9]) == [7, "ate", 9]
    assert bouncer(["a", "b", "c"]) == ["a", "b", "c"]
    assert bouncer([0, 0.0, 0j, {}, (), [], "hello"]) == ["hello"]


#@pytest.mark.skip('Slow but Completed')
def test_rovarsprak():
    assert rovarsprak("hej") == "hohejoj"
    assert rovarsprak("Hej") == "HOHejoj"
    assert rovarsprak("TE16 är bäst.") == "TOTE16 äror bobäsostot."


#@pytest.mark.skip('Completed')
def test_area():
    assert area(20, 20) == 400
    assert area(23.5, 24.0) == 564


#@pytest.mark.skip('Completed.')
def test_to_seconds():
    assert to_seconds(5) == 18000
    assert to_seconds(1.8) == 6480


#@pytest.mark.skip('Completed')
def test_is_of_age():
    assert is_of_age(12) == False
    assert is_of_age(20) == True
    assert is_of_age(17.5) == False


@pytest.mark.parametrize('character, expected', [
('a', True), ('e', True), ('i', True), ('o', True), ('u', True), ('y', True), ('å', True), ('ä', True), ('ö', True),
('A', True), ('E', True), ('I', True), ('O', True), ('U', True), ('Y', True), ('Å', True), ('Ä', True), ('Ö', True),
('k', False), ('h', False), ('x', False), ('R', False), ('r', False), ('j', False), ('C', False), ('p', False), ('T', False)])
def test_vowel(character, expected):
    assert vowel(character) == expected


#@pytest.mark.skip('Completed')
def test_reverse():
    assert reverse('Test string') == 'gnirts tseT'
    assert reverse('Hello') == 'olleH'
    assert reverse('a') == 'a'


#@pytest.mark.skip('Completed')
def test_overlapping():
    assert overlapping([1,2,3], [3,4,5]) == True
    assert overlapping([1.23, 'test', 5], [1.24, 'test1', 'test']) == True
    assert overlapping(['a', 6, 'c'], ['e', 'f', 'g']) == False


#@pytest.mark.skip('Probably Completed')
def test_travel_price():
    assert travel_price(20, 0.6, 12) == 14.4
    assert travel_price(105.5, 0.8, 14) == 118.16


#@pytest.mark.skip('Completed')
def test_palindrome():
    assert is_palindrome('ni talar bra latin') == True
    assert is_palindrome('A car a man a maraca') == True
    assert is_palindrome('hello there') == False


#@pytest.mark.skip('Kinda Completed')
def test_character_frequency():
    assert character_frequency('hej janne') == {'h' : 1, 'e' : 2, 'j' : 2, 'a' : 1, 'n' : 2}
    assert character_frequency('bananer') == {'b' : 1, 'a' : 2, 'n' : 2, 'e' : 1, 'r' : 1}
