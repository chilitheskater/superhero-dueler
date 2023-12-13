import random

from ability import Ability
from armor import Armor

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
    '''
    # self.abilities = list()
    # self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def fight(self, opponent):
    outcome = ['wins','loses','draw']
    result = random.choice(outcome)
    print(f"{self.name} {result} against {opponent.name}")

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
#   ability = Ability("Great Debugging", 50)

  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")

  hero1.fight(hero2)
    #my_hero = Hero ("Grace Hopper", 200)

def create_ability():
    abilities = [
        "Telekenisis",
        "Science",
        "Extra Strenght",
        "Immortality",
        "Lasso of Truth",
        "Invisibility",
        "Team Spirit",
        "Seeing in the Dark"
        "Truthfulness"
        "Sword of Truth"
        "Empathy"
        "Passion"]
    name = abilities[random.randint(0, len(abilities) - 1)]
    power = random.randint(45, 700000)
    return Ability(name, power)
