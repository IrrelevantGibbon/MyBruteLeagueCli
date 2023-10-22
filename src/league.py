import random
import sys

sys.path.append("../mybrutelibs/libs")
from gladiator import Gladiator
from arena import Arena
from data import Permanent


class League:
    def __init__(self, name: str, gladiators: list[Gladiator]) -> None:
        self.gladiators = gladiators
        self.name = name
        for gladiator in self.gladiators:
            gladiator.next_level()

    def add_gladiator(self, gladiator_name: str) -> None:
        gladiator = Gladiator().new(r(), gladiator_name)
        gladiator.next_level()
        self.gladiators.append(gladiator)

    def fight(self):
        gladiators = self.gladiators.copy()
        random.shuffle(gladiators)

        for i in range(0, len(gladiators), 2):
            if i + 1 < len(gladiators):
                arena = Arena(r())
                arena.add_gladiator(0, gladiators[i])
                arena.add_gladiator(1, gladiators[i + 1])
                arena.fight()

    def ranking(self):
        return sorted(
            self.gladiators,
            key=lambda gladiator: (gladiator.lvl, gladiator.xp),
            reverse=True,
        )

    def print_ranking(self):
        ranking = self.ranking()
        for i in range(len(ranking)):
            print(
                f"{i + 1}. {ranking[i].name} ({ranking[i].win}/{ranking[i].lose})  ({ranking[i].lvl})"
            )
            
    def pretty_print_stats(self, gladiator: Gladiator):
        print(f"{gladiator.name} ({gladiator.lvl})")
        print(f"    - {gladiator.win} wins")
        print(f"    - {gladiator.lose} loses")
        print(f"    - {gladiator.lifeMax_()} hp")
        print(f"    - {gladiator.force_()} force")
        print(f"    - {gladiator.agility_()} agility")
        print(f"    - {gladiator.speed_()} speed")
        
        print("    - Permanent bonuses")
        for bonus in gladiator.bonus:
            if isinstance(bonus, Permanent):
                print(bonus.id, end=",")
        print()
        print("    - Super powers")
        for super in gladiator.supers:
            print(super.id, end=",")
        print()
        print("    - Weapons")
        for weapon in gladiator.weapons:
            print(weapon.id, end=",")
        print()
        print("    - Followers")
        for follower in gladiator.followers:
            print(follower.id, end=",")
        
        
            
    def get_gladiator(self, gladiator_name: str):
        for gladiator in self.gladiators:
            if gladiator.name == gladiator_name:
                return gladiator
        return None
               
    def print_gladiator(self, gladiator_name: str):
        gladiator = self.get_gladiator(gladiator_name)
        
        if gladiator is None:
            print(f"Gladiator {gladiator_name} not found")
            return
        self.pretty_print_stats(gladiator)
        
        


def r():
    return random.randint(0, 2147483647)
