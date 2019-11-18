class Mammal:
    def walk(self):
        print("walking")


class Dog(Mammal):
      pass

class Cat(Mammal):
    def meow(self):
        print("meow")


dog1 = Dog()
dog1.walk()

cat1 = Mammal()
cat1.walk()
