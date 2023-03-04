
def test_int():
    assert 1 == 1

def test_string():
    test_string = "Hi"
    assert "Hi" in test_string

def test_list():
    test_list = [1,2,3]
    assert len(test_list) == 3

def test_bool():
    truthy = True
    assert truthy == True

def test_even():
    n = 4
    assert n % 2 == 0

def test_odd():
    n = 5
    assert n % 2 == 1

def test_palindrome():
    word = "bob"
    assert word[::-1] == word
