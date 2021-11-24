import inspect

x = [1,2,3]
y = [4,5]

print(x + y)


class Person:
    '''
    Dunder Methods or Magic Methods are those methods that have double underscore,
    they are special methods defined for python data model only and have many applications.
    '''
    def __init__(self, name):
        self.name = name
    #define a function for representing name
    def __repr__(self):
        return f"Person({self.name})"
    #define what happens if use * operator with this class
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument")
        self.name = self.name * x
    #define what happens if called an instance of the class
    def __call__(self, y):
        print("Called this function", y)

    def __len__(self):
        return len(self.name)

p = Person("Niky")

p * 4
print(p)

p(4)

print("The length is:", len(p))

