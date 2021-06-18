import pytest

def test_should_return_1_for_1():
    assert 1 == fizz_buzz(1)

def fizz_buzz(i):
    if i == 3:
        return "Fizz"
    if i == 5:
        return "Buzz"
    return i

def test_should_return_2_for_2():
    assert 2 == fizz_buzz(2)

def test_should_return_fizz_for_3():
    assert "Fizz" == fizz_buzz(3)

def test_should_return_buzz_for_5():
    assert "Buzz" == fizz_buzz(5)
