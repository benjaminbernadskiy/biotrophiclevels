import json
import os

DATA_FILE = "animals_data.json"

def load_animals():
    if not os.path.exists(DATA_FILE):
        print(f"Please run bio.py first to add animals.")
        return None
    
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def calculate_trophic_level(animal_name, animals, visited=None):
    if visited is None:
        visited = set()
    
    if animal_name in visited:
        return 0
    
    if animal_name not in animals:
        return 0  
    
    animal = animals[animal_name]
    
    if animal["diet"] == "herbivore" or not animal.get("prey"):
        return 2
    
    visited.add(animal_name)
    max_prey_level = 0
    
    for prey_name in animal.get("prey", []):
        prey_level = calculate_trophic_level(prey_name, animals, visited.copy())
        max_prey_level = max(max_prey_level, prey_level)
    
    if max_prey_level == 0:
        return 2  
    
    return max_prey_level + 1

def display_animal(name, animals):
    if name not in animals:
        print(f"{name} not found in database.\n")
        return
    
    animal = animals[name]
    trophic_level = calculate_trophic_level(name, animals)
    level_names = ["", "Producer", "Primary Consumer", "Secondary Consumer", 
                   "Tertiary Consumer", "Quaternary Consumer", "Apex Predator"]
    
    print(f"\n--- {name.title()} ---")
    print(f"Diet: {animal['diet'].title()}")
    print(f"Prey: {', '.join(animal.get('prey', [])) if animal.get('prey') else 'None'}")
    print(f"Predators: {', '.join(animal['predators']) if animal['predators'] else 'None (Apex)'}")
    print(f"Trophic Level: {trophic_level} ({level_names[trophic_level] if trophic_level < len(level_names) else 'High-level Consumer'})")
    print()

def display_all_with_levels(animals):
    animal_levels = []
    for name in animals:
        level = calculate_trophic_level(name, animals)
        animal_levels.append((name, level))
    
    animal_levels.sort(key=lambda x: (x[1], x[0]))
    
    current_level = 0
    level_names = ["", "Producer", "Primary Consumer", "Secondary Consumer", 
                   "Tertiary Consumer", "Quaternary Consumer", "Apex Predator"]
    
    for name, level in animal_levels:
        if level != current_level:
            current_level = level
            level_name = level_names[level] if level < len(level_names) else f"Level {level} Consumer"
            print(f"\n[trophic Level: {level_name}]")
        
        animal = animals[name]
        prey_str = ', '.join(animal.get('prey', [])) if animal.get('prey') else 'None'
        predators_str = ', '.join(animal['predators']) if animal['predators'] else 'None'
        print(f"  • {name.title()} ({animal['diet']})")
        print(f"prey: {prey_str}")
        print(f"predators: {predators_str}")
    
    print()

def main():
    animals = load_animals()
    if animals is None:
        return
    
    while True:
        print("=== Trophic Level Calculator ===")
        print("1. View specific animal")
        print("2. View all animals with trophic levels")
        print("3. Stop")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("animal name: ").lower()
            display_animal(name, animals)
        elif choice == "2":
            display_all_with_levels(animals)
        elif choice == "3":
            break
        else:
            print("u aint real bruh ._. PICK SOMETHING REAL")

if __name__ == "__main__":
    main()
