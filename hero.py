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






