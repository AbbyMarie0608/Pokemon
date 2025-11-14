class Pokemon:
    def __init__(self, id, name, height, weight, hp, attack, defence, speed, type, evo_set, info):
        self.id = int(id)
        self.name = name
        self.height = int(height)
        self.weight = int(weight)
        self.hp = int(hp)
        self.attack = int(attack)
        self.defence = int(defence)
        self.speed = int(speed)
        self.type = type
        self.evo_set = int(evo_set)
        self.info = info