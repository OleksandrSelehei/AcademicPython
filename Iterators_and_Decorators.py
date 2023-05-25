import logging
import time


# Define a class to iterate through a given sequence of numbers
class GeometricIteration:
    def __init__(self, args):
        self.args = args
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.args):
            i = self._index
            self._index += 1
            return self.args[i]
        else:
            raise StopIteration


# Define a class to generate a geometric progression of n terms
class GeometricProgression:
    def __init__(self, start, factor, n):
        self.start = start
        self.factor = factor
        self.n = n
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self.n:
            number = self.start
            self.start *= self.factor
            self._index += 1
            return number
        else:
            raise StopIteration


# Define a decorator function to log the execution time of a given function to a file
logging.basicConfig(filename='example.log', level=logging.INFO)


def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f'{func.__name__} executed in {execution_time:.21f} seconds')
        return result

    return wrapper


# Define a function to sum the elements of an iterator
@log_time
def sum_(args):
    result = 0
    for element in args:
        result += element
    return result


# Create and sum a geometric progression of 10 terms, 100 terms, and 1000 terms, respectively
print(sum_(GeometricIteration([i for i in GeometricProgression(2, 3, 10)])))
print(sum_(GeometricIteration([i for i in GeometricProgression(2, 3, 100)])))
print(sum_(GeometricIteration([i for i in GeometricProgression(2, 3, 1000)])))

