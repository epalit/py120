class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        
    def __str__(self):
        return f"a {self.species} named {self.name}"
    
class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []
        
    def adopt(self, pet):
        self.pets.append(pet)
        
    def number_of_pets(self):
        return len(self.pets)

class Shelter:
    def __init__(self):
        self.adopters = set()
        self.animals = []
        
    def adopt(self, owner, pet):
        owner.adopt(pet)
        self.adopters.add(owner)
        if pet in self.animals:
            self.animals.remove(pet)
        
    def print_adoptions(self):
        for owner in self.adopters:
            print(f"{owner.name} has adopted the following pets:")
            for pet in owner.pets:
                print(pet)
            print()
            
    def take_in(self, pet):
        self.animals.append(pet)
        
    def number_of_animals(self):
        return len(self.animals)
    
    def print_animals(self):
        print("The Animal Shelter has the following unadopted pets:")
        for animal in self.animals:
            print(animal)
        
cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

asta = Pet("dog", "Asta")
shelter.take_in(asta)

shelter.print_adoptions()
shelter.print_animals()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
print(f"The Animal Shelter has {shelter.number_of_animals()} unadopted pets.")

