import pytest

def fizz_buzz(numero):
    result = ""
    if numero % 3 == 0:
         result += "Fizz"
    if numero % 5 == 0:
        result += "Buzz"
    if result:
        return result
    return numero

def test_should_return_number_for_number():
    assert 1 == fizz_buzz(1)
    assert 2 == fizz_buzz(2)

def test_should_return_fizz_for_multiple_of_3():
    assert "Fizz" == fizz_buzz(3)
    assert "Fizz" == fizz_buzz(6)

def test_should_return_buzz_for_multiple_of_5():
    assert "Buzz" == fizz_buzz(5)
    assert "Buzz" == fizz_buzz(10)

def test_should_return_fizzbuzz_for_multiples_of_3_and_5():
    assert "FizzBuzz" == fizz_buzz(15)
    assert "FizzBuzz" == fizz_buzz(30)


for number in range(1,101):
    print(fizz_buzz(number))
