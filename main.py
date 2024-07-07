# lab-1/main.py

from zoo import Animal, Enclosure, Food, Staff, ZooInventory

def main():
    zoo = ZooInventory()

    # Додаємо тварин
    tiger = Animal("Tiger", "Sheru", 5, "Carnivore")
    elephant = Animal("Elephant", "Dumbo", 10, "Herbivore")
    zoo.add_animal(tiger)
    zoo.add_animal(elephant)

    # Додаємо вольєри
    enclosure1 = Enclosure(1, 500, "Outdoor")
    enclosure2 = Enclosure(2, 1000, "Indoor")
    enclosure1.add_animal(tiger)
    enclosure2.add_animal(elephant)
    zoo.add_enclosure(enclosure1)
    zoo.add_enclosure(enclosure2)

    # Додаємо корм
    meat = Food("Meat", 50)
    hay = Food("Hay", 100)
    zoo.add_food(meat)
    zoo.add_food(hay)

    # Додаємо працівників
    keeper = Staff("Alice", "Keeper")
    vet = Staff("Bob", "Veterinarian")
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Виводимо інвентаризацію
    zoo.inventory_summary()

if __name__ == "__main__":
    main()
