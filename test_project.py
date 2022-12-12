import pytest
def inc(x):
    return x + 1

# @pytest.mark.Increment
def test_Increment_function():
    assert inc(3) == 4

# @pytest.mark.Average
def test_Average_function():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = 0
    for i in x:
        sum = sum + i

    average = sum / len(x)
    assert average == 5.5


def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)

# @pytest.mark.factorial
def test_factorial_function():
    assert fact(5) == 120

# @pytest.mark.maximum
def test_maximum_function():
    x = [12, 21, 43, 5, 67, 90, 11, 7, 21, 3]
    maximum = x[0]
    for i in x:
        if maximum < i:
            maximum = i
    assert maximum == 90

# @pytest.mark.minimum
def test_minimum_function():
    x = [12, 21, 43, 5, 67, 90, 11, 7, 21, 3]
    minimum = x[0]
    for i in x:
        if i < minimum:
            minimum = i
    assert minimum == 3

def Basket_function():
    basket = ["apples", "bananas", "Grapes", "Pineapple", "Oranges", "kiwi", "melons"]
    return basket

def test_find_fruit_function():
    assert "apples" in Basket_function()

