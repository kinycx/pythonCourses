class Dog(object):
    def __init__(self,name):
        self.name = name
        print(f"YOU FUCKIN MADE A {name} EEEIIIISH!!")

    def speak(self):
        print("CIAO MI CHIAMO ", self.name, " CIOE' ehm.. BARK BARK!!")

drillo = Dog("Drillo")
drillo.speak()

#INHERITANCE

class Cat(Dog):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

ciri = Cat("Ciri", "White")
ciri.speak()