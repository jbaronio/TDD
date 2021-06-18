import pytest

def test_should_return_1_for_1():
    assert 1 == fizz_buzz(1)

def fizz_buzz(i):
    return i

def test_should_return_2_for_2():
    assert 2 == fizz_buzz(2)
