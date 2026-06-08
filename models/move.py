class Move:
    def __init__(self, name, power, type, category, target, stat_changes):
        self.name = name
        self.power = power
        self.type = type
        self.category = category
        self.target = target
        self.stat_changes = stat_changes

    def execute(self, attacker, defender):
        pass

class DamageMove(Move):
    pass


class StatusMove(Move):
    pass