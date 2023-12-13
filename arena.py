from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        ''' Instantiate properties
            team_one: None 
            team_two: Noone
        '''
        self.team_one = Team("team_one")
        self.team_two = Team("team_two")

    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")
        return Ability(name, max_damage)

    def create_weapon(self):
        '''
        Prompt user for weapon information and return a new Weapon instance
        with values from user input.
        '''
        name = input("Enter the name of your weapon: ")
        max_damage = int(input("Enter the max damage you want: "))
        return Weapon(name, max_damage)

    def create_armor(self):
        ''' Prompt user for Armor info
            return Armor with values from user input.
        '''
        name = input("Enter name the of your sacred Armor: ")
        max_block = int(input("Enter the max block value you want to use for this: "))
        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)

        add_item = ""
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())

        return hero

    def build_team_one(self):
        num_of_team_members = int(input("How many members would you like on Team One?\n"))
        self.team_one.add_heroes([self.create_hero() for _ in range(num_of_team_members)])

    def team_battle(self):
        ''' Battle team_one and team_two together'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        ''' Prints team statistics to the terminal.'''
        print("\n")
        
        for team in [self.team_one, self.team_two]:
            print(f"{team.name} statistics:")
            team.stats()
            print("\n")

        team_kills = sum(hero.kills for hero in self.team_one.heroes)
        team_deaths = sum(hero.deaths for hero in self.team_one.heroes) or 1
        print(f"{self.team_one.name} average K/D was: {team_kills/team_deaths}")

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print(f"Survived from {self.team_one.name}: {hero.name}")

if __name__ == "__main__":
    while True:
        arena = Arena()

        arena.build_team_one()
        arena.build_team_two()

        arena.team_battle()
        arena.show_stats()

        play_again = input("Play Again? Y or N: ")
        if play_again.lower() == "n":
            break

        arena.team_one.revive_heroes()
        arena.team_two.remove_heroes()

