import pytest

def fizz_buzz(i):
    if i % 3 == 0:
        return "Fizz"
    if i == 5:
        return "Buzz"
    return i

def test_should_return_number_for_number():
    assert 1 == fizz_buzz(1)
    assert 2 == fizz_buzz(2)

def test_should_return_fizz_for_multiple_of_3():
    assert "Fizz" == fizz_buzz(3)
    assert "Fizz" == fizz_buzz(6)

def test_should_return_buzz_for_5():
    assert "Buzz" == fizz_buzz(5)
