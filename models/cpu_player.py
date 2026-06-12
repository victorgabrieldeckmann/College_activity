import random
from models.trainer import Trainer

class CPUPlayer(Trainer):

    def choose_action(self):

        actions = self.pokemon.moves.copy()

        if self.pokemon.heal_potions["qnt"] > 0:
            actions.append("heal")

        return random.choice(actions)