import time

class Hero:
    # Public class variables
    jumlah = 0
    move = 0
    
    # Private & Protected class variables
    __habit = "Makan"
    _speed = 15
    
    def __init__(self, name, attack, defense, hp, gender):
        # Public instance variables
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        Hero.jumlah += 1
        
        # Private instance variable (cannot be accessed directly outside the class)
        self.__gender = gender
        
        # Protected instance variable
        self._size = 30

    # Getter and Setter for the private variable __gender
    def get_gender(self):
        return self.__gender
        
    def set_gender(self, new_gender):
        self.__gender = new_gender

    # Battle Method
    def serang(self, target):
        Hero.move += 1
        print(f"\n[Turn {Hero.move}]")
        print(f"{self.name} attacks {target.name}!")
        
        # Simple damage calculation
        damage = self.attack / target.defense
        target.hp -= damage
        
        time.sleep(0.5) # Adds a slight delay for dramatic effect in the console
        print(f"{target.name} takes {damage:.2f} damage! {target.name}'s remaining HP: {target.hp:.2f}")

# Inheritance: HeroTanker inherits from Hero
class HeroTanker(Hero):
    def __init__(self, name, gender):
        # Using super() to call the parent class's __init__ method
        # Tankers have lower attack, but higher defense and HP
        super().__init__(name, attack=5, defense=15, hp=150, gender=gender)

# --- Main Execution ---

print("=== BATTLE START ===")

# Instantiating objects (Creating the heroes)
luffy = Hero(name="Luffy", attack=15, defense=7, hp=95, gender="Male")
usop = Hero(name="Usop", attack=8, defense=5, hp=80, gender="Male")

# You can also test your Tanker class like this:
# franky = HeroTanker(name="Franky", gender="Cyborg")

# The Battle Loop
while True:
    luffy.serang(usop)
    if usop.hp <= 0:
        break
        
    usop.serang(luffy)
    if luffy.hp <= 0:
        break

# Declaring the winner
print("\n=== BATTLE OVER ===")
if luffy.hp <= 0:
    print(f"Luffy fainted! The winner is {usop.name}!")
else:
    print(f"Usop fainted! The winner is {luffy.name}!")