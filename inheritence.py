class Hero :

	def __init__(self,name,power):
		self.name = name
		self.power = power

class Hero_Ability(Hero):
	pass

class hero_Speed(Hero):
	pass

hero1 = Hero('Klee',340)
hero2 = Hero_Ability('amber',300)
hero3 = hero_Speed('Lisa',220)

print(hero1.__dict__)
print("\n")
print(help(hero2))
print("\n")
print(hero2.__dict__)
print("\n")
print(help(hero3))
print(hero3.__dict__)