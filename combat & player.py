##### Player Stats #####
class player:
	def __init__(self): ##### initial stats #####
		 self.name = ''
		 self.level = 1
		 self.hp = 100
		 self.mp = 100
		 self.job = 'mage'
		 self.status = ({False:"burn",False:"curse",True:"poison" })
		 self.atk = 100
		 self.deef = 100
		 self.crit = 0
		 self.invent = {"key":0, "apple":0, "potion":0}
		 self.room = 'catroom'
Myplayer = player()

##### Rooms ######

combatrooms = ["catroom","dogroom","dragonroom"]
itemrooms = ["catroom"]

##### Enemy 1 #####
class Enemy1:
	def __init__(self):
		 self.name = "big fat cat"
		 self.hp = 100
		 self.mp = 100
		 self.job = 'mage'
		 self.status = ({False:"burn",False:"curse",False:"poison" })
		 self.atk = 100
		 self.deef = 100
		 self.crit = 0
Enemy1 = Enemy1()

##### Enemy 2 #####
class Enemy2:
	def __init__(self):
		 self.name = "small scary dog"
		 self.hp = 100
		 self.mp = 100
		 self.job = 'mage'
		 self.status = ({False:"burn",False:"curse",False:"poison" })
		 self.atk = 100
		 self.deef = 100
		 self.crit = 0
Enemy2 = Enemy2()

##### Enemy 3 #####
class Enemy3:
	def __init__(self):
		 self.name = "boring generic dragon"
		 self.hp = 100
		 self.mp = 100
		 self.job = 'mage'
		 self.status = ({False:"burn",False:"curse",False:"poison" })
		 self.atk = 100
		 self.deef = 100
		 self.crit = 0
Enemy3 = Enemy3()



##### Command #####
command = input("> ")
while command:
	##### COMBAT ######
	if command.lower() == "fight" and Myplayer.room in combatrooms:
		print("##################")
		print("#     Attack     #")
		print("#      Magic     #")
		print("#       Bag      #")
		print("##################")
		move = input("What will you do? ")
		if move.lower() == "attack":
			dmg = Myplayer.atk + Myplayer.level - Enemy1.deef
			print("You did " + str(dmg) + " to " + Enemy1.name)

		elif move.lower() == "magic":
			dmg = Myplayer.mp + Myplayer.level
			print("You did " + str(dmg) + " to " + Enemy1.name)

		elif move.lower() == "bag":
			print(Myplayer.invent)
			item = input("What will you use? ")
			if item.lower() in Myplayer.invent:
				Myplayer.invent[item] -= 1
				print(Myplayer.invent)
	##### Take #####			
	elif command.lower() == "take" and Myplayer.room in itemrooms:
		item = input("what will you take? ")
		print("You took the " + item + ".")
		if item.lower() in Myplayer.invent:
			Myplayer.invent[item] += 1
			print(Myplayer.invent)
	##### Use #####
	elif command.lower() == "use":
		print(Myplayer.invent)
		item = input("what will you use? ")
		if item.lower() in Myplayer.invent:
			Myplayer.invent[item] -= 1
			print(Myplayer.invent)
	

	




	command = input("> ")
  