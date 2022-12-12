def inc(x):
    return x + 1


def Increment_function():
    print("The incremented Value is:", inc(3))
    assert inc(3) == 4


def Average_function():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = 0
    for i in x:
        sum = sum + i

    average = sum / len(x)
    print("The Average is: ", average)
    assert average == 5.5


def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)


def factorial_function():
    print("The Factorial of the No is:", fact(5))
    assert fact(5) == 120


def maximum_function():
    x = [12, 21, 43, 5, 67, 90, 11, 7, 21, 3]
    maximum = x[0]
    for i in x:
        if maximum < i:
            maximum = i
    print("The Maximum no is: ", maximum)
    assert maximum == 90


def minimum_function():
    x = [12, 21, 43, 5, 67, 90, 11, 7, 21, 3]
    minimum = x[0]
    for i in x:
        if i < minimum:
            minimum = i
    print("The Minimum no is: ", minimum)
    assert minimum == 3


def Basket_function():
    basket = ["apples", "bananas", "Grapes", "Pineapple", "Oranges", "kiwi", "melons"]
    return basket


def find_fruit_function():
    assert "apples" in Basket_function()


# main
if __name__ == "__main__":
    Increment_function()
    Average_function()
    maximum_function()
    minimum_function()
    factorial_function()
    find_fruit_function()
