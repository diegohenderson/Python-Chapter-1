import random

class Enemy:
    hp= 200
    def __init__(self,atkl,atkh):
        self.atkl= atkl
        self.atkh=atkh
    def getatk(self):
        print("atk is",self.atkl)
    def gethp(self):
        print("hp is",self.hp)
enemy1= Enemy(40,49)
enemy1.getatk()
enemy1.gethp()
enemy2= Enemy(75,90)
enemy2.getatk()
enemy2.gethp()

playerhp=260
enemyatkl= 60
enemyatkh=80
while playerhp > 0:
    dmg = random.randrange(enemyatkl,enemyatkh)
    playerhp= playerhp -dmg
    if playerhp <=30:
        playerhp=30
    print("enemy strikes for", dmg,"points of damage. current hp is", playerhp)
    if playerhp>30:
        continue
    print("you have low health, you have")
    break

