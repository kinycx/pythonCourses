def func(f):
    """[Decorator like functions take a function as argument which is wrapped in a subfunction that
        takes the argument:
            *args (any positional argument)
            **kwargs (any keyword argument)]

    Args:
        f ([function]): [description]
    """
    def wrapper(*args, **kwargs):
        print("started")
        rv = f(*args, **kwargs)
        print("ended")
        return rv

    return wrapper


#decorators are function implemented with wrapper function that are called just before another function with the operator @
#func2() is wrapped inside the func(f) and takes the place of f
@func
def func2(x):
    print(x)
    return x

@func
def func3():
    print("I am func3")

x = func2(5)
print("returned value", x)
func3()

###########################################
import time

def exeTime(func):
    """[Decorator that return the execution time of a function]

    Args:
        func ([type]): [description]
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print("Execution Time:", total)
        return rv

    return wrapper

@exeTime
def test():
    for _ in range(10000000):
        pass

test()