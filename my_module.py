first_name = "Piotr"
numbers = [10, 20, 30, 40, 50]


def adder(a, b):
    return a + b


square = lambda x: x ** 2


# when this file gets imported into
# another module this print is executed
print('Hello world!')

# within each module we have available __name__ variable
# and we can use it to determine if this module is executed or imported
print(__name__)

if __name__ == "__main__":
    print('Executing this module')
