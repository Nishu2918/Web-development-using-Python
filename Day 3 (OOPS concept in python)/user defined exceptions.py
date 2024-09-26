# Define a custom exception class

class CustoError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

#Example function tghat raises the custom exception

def check_value(x):
    if x < 0:
        raise CustoError("Number should be non-negative")
    elif x >100:
        raise CustoError("Number is too large")
    return x

#Example usgae of the function that raises the custom exception

try:
    num = int(input("Enter a number (0-100):"))
    result = check_value(num)
    print("valid number entered:",result)
except CustoError as ce:
    print("CustomError occurred:",ce.message)
except ValueError:
    print("Invalid input. Please enter a valid")