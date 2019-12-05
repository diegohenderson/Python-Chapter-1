class Enemy:
    def __init__(self,hp,mp):
        self.max_hp=hp
        self.hp=hp
        self.max_mp=mp
        self.mp=mp
    def het_hp(self):
        return self.hp