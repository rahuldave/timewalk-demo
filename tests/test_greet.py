from greet import greet, shout


def test_plain():
    assert greet("Ada") == "Hello, Ada."


def test_excited():
    assert greet("Ada", excited=True) == "Hello, Ada!"


def test_empty_name():
    assert greet("") == "Hello, ."


def test_shout():
    assert shout("Ada") == "HELLO, ADA!"
