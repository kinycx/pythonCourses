class File:
    
    def __init__(self, filename, method):
       self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback):
        print(f"{type}, {value}, {traceback}")
        print("Exit")
        self.file.close()
        return True

with File("file.txt", "w") as f:
    print("middle")
    f.write("Hello")

##################################
print("\n\nPART 2, the same result\n\n")

from contextlib import contextmanager 

@contextmanager
def file(filename, method):
    print("enter")
    file = open(filename, method)
    yield file
    file.close()
    print("exit")

with file("text.txt", "w") as f:
    print("middle")
    f.write("hello")