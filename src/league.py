import random
import sys

sys.path.append("../mybrutelibs/libs")
from gladiator import Gladiator
from arena import Arena


class League:
    def __init__(self, name: str, gladiators: list[Gladiator]) -> None:
        self.gladiators = gladiators
        self.name = name
        for gladiator in self.gladiators:
            gladiator.next_level()

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


def r():
    return random.randint(0, 2147483647)
