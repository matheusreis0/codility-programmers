#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def is_multiple_of_three(n: int):
    return n % 3 == 0

def is_multiple_of_five(n: int):
    return n % 5 == 0

def fizzBuzz(n: int):
    for i in range(1, n + 1):
        is_current_multiple_of_five = is_multiple_of_five(i)
        is_current_multiple_of_three = is_multiple_of_three(i)
        if is_current_multiple_of_three and is_current_multiple_of_five:
            print("FizzBuzz")
        if is_current_multiple_of_three and not is_current_multiple_of_five:
            print("Fizz")
        if is_current_multiple_of_five and not is_current_multiple_of_three:
            print("Buzz")
        if not is_current_multiple_of_three and not is_current_multiple_of_five:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
