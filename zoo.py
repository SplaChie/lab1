# lab-1/zoo.py

class Animal:
    def __init__(self, species, name, age, diet):
        self.species = species
        self.name = name
        self.age = age
        self.diet = diet

    def __str__(self):
        return f"{self.name} the {self.species}, Age: {self.age}, Diet: {self.diet}"

class Enclosure:
    def __init__(self, enclosure_id, size, type):
        self.enclosure_id = enclosure_id
        self.size = size
        self.type = type
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def __str__(self):
        animal_list = ', '.join([animal.name for animal in self.animals])
        return f"Enclosure {self.enclosure_id} ({self.type}, {self.size} sq ft): {animal_list}"

class Food:
    def __init__(self, food_type, quantity):
        self.food_type = food_type
        self.quantity = quantity

    def __str__(self):
        return f"{self.food_type} - {self.quantity} units"

class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name}, {self.role}"

class ZooInventory:
    def __init__(self):
        self.animals = []
        self.enclosures = []
        self.food_inventory = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def add_food(self, food):
        self.food_inventory.append(food)

    def add_staff(self, staff):
        self.staff.append(staff)

    def inventory_summary(self):
        print("Animals in Zoo:")
        for animal in self.animals:
            print(animal)
        print("\nEnclosures:")
        for enclosure in self.enclosures:
            print(enclosure)
        print("\nFood Inventory:")
        for food in self.food_inventory:
            print(food)
        print("\nStaff:")
        for staff in self.staff:
            print(staff)
