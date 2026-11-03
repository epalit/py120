class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

class Cat(Pet):
    def __init__(self, name, age, fur):
        super().__init__(name, age)
        self._fur = fur
        
    @property
    def fur(self):
        return self._fur
    @property  
    def info(self):
        return f"My cat {self.name} is {self.age} years old and has {self.fur} fur."

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)

