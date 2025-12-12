import json
import os

DATA_FILE = "animals_data.json"

def load_animals():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_animals(animals):
    with open(DATA_FILE, 'w') as f:
        json.dump(animals, f, indent=2)
    print(f"Data saved to {DATA_FILE}\n")

animals = load_animals()

def add_animal():
    name = input("Enter animal name: ").lower()
    
    diet = input("Is it a carnivore or herbivore? (c/h): ").lower()
    diet_type = "carnivore" if diet == 'c' else "herbivore"
    
    prey = []
    print("Enter prey/what this animal eats (press Enter with no input when done):")
    while True:
        prey_item = input("prey:").strip().lower()
        if not prey_item:
            break
        prey.append(prey_item)
    
    predators = []
    print("Enter predators (press enter with no input when done):")
    while True:
        predator = input("predator: ").strip().lower()
        if not predator:
            break
        predators.append(predator)
    
    animals[name] = {
        "diet": diet_type,
        "prey": prey,
        "predators": predators
    }
    save_animals(animals)
    print(f"Added {name}\n")

def display_all():
    if not animals:
        print("no animals")
        return
    
    for name in sorted(animals.keys()):
        animal = animals[name]
        prey_str = ', '.join(animal.get('prey', [])) if animal.get('prey') else 'None'
        pred_str = ', '.join(animal['predators']) if animal['predators'] else 'None'
        print(f"{name.title()}: {animal['diet']}")
        print(f"  Eats: {prey_str}")
        print(f"  Eaten by: {pred_str}")

def main():
    while True:
        print("1. Add animal")
        print("2. View all animals")
        print("3. Stop")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_animal()
        elif choice == "2":
            display_all()
        elif choice == "3":
            break
        else:
            print("Not an option bruh.\n")

if __name__ == "__main__":
    main()
