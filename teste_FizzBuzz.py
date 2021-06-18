import pytest

def fizz_buzz(i):
    if i == 15:
        return "FizzBuzz"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return i

def test_should_return_number_for_number():
    assert 1 == fizz_buzz(1)
    assert 2 == fizz_buzz(2)

def test_should_return_fizz_for_multiple_of_3():
    assert "Fizz" == fizz_buzz(3)
    assert "Fizz" == fizz_buzz(6)

def test_should_return_buzz_for_multiple_of_5():
    assert "Buzz" == fizz_buzz(5)
    assert "Buzz" == fizz_buzz(10)

def test_should_return_fizzbuzz_for_15():
    assert "FizzBuzz" == fizz_buzz(15)
