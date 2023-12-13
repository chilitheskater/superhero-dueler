from hero import Hero
import random
#team class will manage all of our superheros
class Team:
    def __init__(self, name):
        '''init team with team name and empty list of heroes'''
        self.name = name
        self.heroes = list()
    def remove_hero(self, name):
        '''if hero isn't found return zero'''
        #if hero in list, remove hero from list by name
        for hero in self.heroes:
            #make sure it is correct hero
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        #if looping through list and didn't find hero, indicator would not change so return 0
        if not foundHero:
            #if not = if not True
            return 0
    def view_all_heroes(self):
        '''print heroes to console'''
        print(self.heroes)
    def add_hero(self,hero):
        '''Add hero object to self.heroes'''
        #add hero object that is passed into list of heroes in self.heroes
        self.heroes.append(hero)
    def stats(self):
        #print hero statistics
      for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")
    def revive_heroes(self, health):
    #reset all heroes health to starting_health
        for hero in self.heroes:
            hero.current_health = health
            print(f"{hero.name} has been revived!")
    def attack(self, other_team):
        #battle teams 
        living_heroes = list(self.heroes)
        living_opponents = list(self.opponent)
        for hero in self.heroes:
            living_heroes.append(hero)
        for hero in other_team.heroes:
            living_opponents.append(hero)
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            #1) randomly select living hero from ea. team
            hero1 = random.choice(living_heroes)
            hero2 = random.choice(living_opponents)
            #fight ea. other
            hero1.fight(hero2)
        #update list/fight to the death
        if hero1.is_alive():
            living_heroes.remove(hero1)
        else:
            living_opponents.remove(hero2) #hero2 lost the battle 
        
        if hero2.is_alive():
            living_heroes.remove(hero2)
        else:
            living_opponents.remove(hero1) #