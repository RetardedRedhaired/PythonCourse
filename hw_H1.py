import random
import time

class Human:
    def __init__(self, hp = None, ap = None):
        self.hp = hp
        self.ap = ap
        
        
class Survior(Human):
    def __init__(self, name, hp, ap):
        super().__init__(hp, ap)
        self.name = name
        
    def _check(self):
        print(f'{self.name} HP is {self.hp}, attack power is {self.ap}')


class Zombie(Human):
    def __init__(self, hp, class_z, ap):
        super().__init__(hp, ap)
        self.class_z = class_z
    
    def _check(self):
        print(f"Zombie's class is {self.class_z}, HP is {self.hp}, attack power is {self.ap}")
    
def Classify():
    a = ("Just zombie", 'Fireman', 'Policeman', 'Hunter', 'FUCKING_ZOMBIE_SHREK')
    t = random.randint(0, 100)
    if t <= 50:
        ty = a[0]
        hp = random.randint(1, 15)
        ap = random.randint(0, 5)
    elif 50 < t <= 75:
        ty = a[1]
        hp = random.randint(15, 30)
        ap = random.randint(5, 10)
    elif 75 < t <= 90:
        ty = a[2]
        hp = random.randint(5, 10)
        ap = random.randint(25, 35)
    elif 90 < t <= 98:
        ty = a[3]
        hp = random.randint(25, 50)
        ap = random.randint(25, 35)
    else:
        ty = a[4]
        hp = random.randint(50, 150)
        ap = random.randint(40, 100)
    return (hp, ty, ap)


def attack(attacker, defender):
    t = random.randint(0, 100)
    if t > 90:
        defender.hp -= attacker.ap * 3
        print(f'Хера себе, крит выпал. Минус {attacker.ap * 3}. Ай, больно. За шо молодого так')
    else:
        defender.hp -= attacker.ap
        print(f'НЫЫЫЫЫЫЫЫЫААААААААААА. Минус {attacker.ap}')


def battle(zomb, surv):
    print(f'Пред вами предстал могучий {zomb.class_z}, у него {zomb.hp} HP, а сносит он {zomb.ap} HP. За оружие!')
    while (zomb.hp > 0 and surv.hp > 0):
        t = random.randint(0,1)
        if t == 0:
            print(f'Вы атаковали вонючую рожу, зомби потерял ебучку!')
            attack(surv, zomb)            
        else:
            print(f'Зомби пизданул тебя своим обрубком по лицу. Жалко, куда деньги на лечение скидывать?')
            attack(zomb, surv)            
        time.sleep(2)
        if (zomb.hp <= 0):
            print('Умер мужык')
        if (surv.hp <=0):
            print('PRESS F TO PAY RESPECTS')

ramzan = Survior('Ramzan', 25, 30)

n = int(input('Сколько зомби хошь побить, силач: '))
for _ in range(n):
    b = Classify()
    maxim = Zombie(b[0], b[1], b[2])
    battle(maxim, ramzan)
    if ramzan.hp <= 0:
        break
print('ЛЯ КАКОЙ ПАЖИЛОЙ УБИЦА ЗОМБИ')
