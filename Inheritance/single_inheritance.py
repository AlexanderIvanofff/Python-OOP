class Animal:
    def eat(self):
        return f'eating...'


class Dog(Animal):
    def bark(self):
        return f'barking...'


d = Dog()

print(d.eat())
print(d.bark())