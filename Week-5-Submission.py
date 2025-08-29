#  Solution 1. Design Your Own Class! 🏗️

# Define a Character class with attributes for name and age,
# and a method to introduce the character using those attributes.
class Character:
    # initialize the name and age attributes.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # The introduce method returns a formatted string
    # introducing the character using the stored attributes.
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


# Define the Superhero class that inherits from Character and initializes additional attributes:
# hero_name, superpowers, and a protected _weakness.
class Superhero(Character):
    def __init__(self, name, age, hero_name, superpowers, weakness):
        super().__init__(name, age)
        self.hero_name = hero_name
        self.superpowers = superpowers
        self._weakness = weakness # Protected attribute

    # Method to reveal the superhero's identity

    # Method to reveal the superhero's identity
    def reveal_identity(self):
        """Return a string revealing the superhero's real name and hero name."""
        return f"My real name is {self.name}, but I am {self.hero_name}!"

      # Method to use a superpower
    def use_superpower(self, power):
        if power in self.superpowers:
            return f"{self.hero_name} uses {power}!"
        else:
            return f"{self.hero_name} doesn't have the power: {power}."
    # Method to get the superhero's weakness
    def get_weakness(self):
        return f"{self.hero_name}'s weakness is {self._weakness}."



# Solution 2: Polymorphism Challenge! 🎭

# Define a base class Vehicle with a method move.
class Vehicle:
    def move(self):
        pass

# Define subclasses for different vehicle types

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")  
                        
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")  

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵") 
              
class Bike(Vehicle):
    def move(self):
        print("Biking 🚴‍♂️")  

class Train(Vehicle):
    def move(self):
        print("Choo Choo 🚆")