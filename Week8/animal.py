class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name, 'says', self.sound)
        
class Dog(Animal):
    sound = 'woof!'

class Cat(Animal):
    sound = 'meow'

dog = Dog('Fido')
cat = Cat('Fluffy')

dog.speak()
cat.speak()
