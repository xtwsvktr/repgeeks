class SuperHero:
    people = "people"

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def nameforsuperhero(self):
        print(f"имя супергероя {self.name}")

    def health_point(self):
        print(f"здоровье героя {self.health_points * 2}")

    def __str__(self):
        return f"{self.nickname} {self.superpower} {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("барри", "флэш", "скорость", 750, "Все разбитые сердца до сих пор бьются")
print(hero)
SuperHero.nameforsuperhero(hero)
SuperHero.health_point(hero)
print(len(hero))


class Sups(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=0, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        print(f'Здоровье Железного Человека x2: {self.health_points * self.health_points}')
        self.fly = True

    def crit_hero(self):
        print(f'Урон Железного Человека x2: {self.damage * self.damage}')

    def fly_phrase(self):
        if self.fly_phrase:
            print('fly in the True_phrase')

    def hp(self):
        print(f'Здоровье Человека Паука x2: {self.health_points * self.damage}')
        self.fly = True

    def critt(self):
        print(f'Урон Человека Паука x2: {self.damage * self.damage}')

    def fly_phras(self):
        if self.fly_phrase:
            print('fly in the True_phrase')

    def double_hp(self):
        print(f'Здоровье Бумa x2: {self.health_points * self.health_points}')
        self.fly = True

    def crit(self):
        print(f'Урон Бума x2: {self.damage * self.damage}')

    def gen_x(self):
        pass

    class First_hero(SuperHero):
        people = 'people'

    class Second_hero(SuperHero):
        people = 'people'

    class Villian(SuperHero):
        people = 'monster'



first_hero = Sups('Tony Stark', 'Iron Man', 'intelligence', 300, 'I"m an Tony Stark!', 650 )
second_hero = Sups('Piter Parker', 'Spider Man' 'web', 400, 'spider neighbor!', 920)
villian = Sups('Cosmo', 'Boom', 'Bombs', 150, 'uhaha!', 300)

print(first_hero.double_health())
print(first_hero.crit_hero())
print(first_hero.fly_phrase())

print(second_hero.hp())
print(second_hero.critt())
print(second_hero.fly_phras())

print(villian.double_hp())
print(villian.crit())