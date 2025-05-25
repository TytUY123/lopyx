class Animal:
    def __init__(self, name, age, wtsay):
        self.name = name
        self. age = age
        self.wtsay = wtsay
        
    def speak(self):
        print(f"{self.name} says: {self.wtsay}")
    def describe(self, typee, age):
        self.typee = typee
        self.age = age
        print(f"Hello! I am {self.typee} and i am {self.age} years old")

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self, wtsay):
        self.wtsay = wtsay
        print(f"Cat {self.name} says: {self.wtsay}")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self, wtsay):
        self.wtsay = wtsay
        print(f"Dog {self.name} says: {self.wtsay}")

class Parrot(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self, wtsay):
        self.wtsay = wtsay
        print(f"Parrot {self.name} says: {self.wtsay}")

c1 = Cat("Myrzik")
c1.speak("Meow")

c2 = Dog("sharik")
c2.speak("Gav")

c3 = Parrot("mihail")
c3.speak("Grrrr")
