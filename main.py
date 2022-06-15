
#Importations des modules
import sys
import time
import select
import tty
import termios
import random

import background
import perso


old_settings = termios.tcgetattr(sys.stdin)

valeu_play_again = 0
play_again = 0

page_accueil = 0

monster1 = None
monster2 = None
monster3 = None
monster4 = None

vieMonster4 = 0.0

player = None

Life = None
Weapon = None

timeStep = None

Background = None

positionX1 = random.randint(10,40)
positionY1 = random.randint(3,10)
positionX2 = random.randint(10,40)
positionY2 = random.randint(3,10)
positionX3 = random.randint(10,40)
positionY3 = random.randint(3,10)

numero_zone = 0

temps = 0





def init():
	global player, timeStep, Background, positionX1, positionY1, positionX2, positionY2, positionX3, positionY3, monster1, monster2, monster3, Life, Weapon
	timeStep = 0.05
	
	player = perso.createPlayer(Pname="player",
					PpositionX=25,
					PpositionY=11,
					Pspeed=1.0,
					Pstrength=5.0,
					Plife=100.0,
					PactiveWeapon="poing",
					Plevel=1,
					PlistWeapon=["poing"],
					Pdirection="up",
					Pcolor=2)


	Background = background.create("zone.txt")
	
	monster1 = perso.createMonster(Mname="monster",
					MpositionX=positionX1,
					MpositionY=positionY1,
					Mspeed=1.0,
					Mstrength=1.0,
					Mlife=10.0,
					Mweapon="poing",
					Mcolor=0,
					Mnumero=1,
					Metat="E")
	monster2 = perso.createMonster(Mname="monster",
					MpositionX=positionX2,
					MpositionY=positionY2,
					Mspeed=1.0,
					Mstrength=1.0,
					Mlife=10.0,
					Mweapon="poing",
					Mcolor=0,
					Mnumero=2,
					Metat="E")
	monster3 = perso.createMonster(Mname="monster",
					MpositionX=positionX3,
					MpositionY=positionY3,
					Mspeed=1.0,
					Mstrength=1.0,
					Mlife=10.0,
					Mweapon="poing",
					Mcolor=0,
					Mnumero=3,
					Metat="E")

	tty.setcbreak(sys.stdin.fileno())

	Weapon = createWeaponBonus()
	Life = createLifeBonus()
	




def createWeaponBonus():
	
	
	Weapon = {'Wx': 200.0, 'Wy': 200.0, 'valeur': 20.0, 'color': 6, 'etat': " "}

	return Weapon





def showWeaponBonus(Weapon):
	
	x = str(int(Weapon['Wx']))
	y = str(int(Weapon['Wy']))
	txt="\033["+y+";"+x+"H"
	sys.stdout.write(txt)

	sys.stdout.write("\033[40m")

	c = Weapon["color"]
	txt="\033[3"+str(c%7+1)+"m"
	sys.stdout.write(txt)
	
	n = Weapon["etat"]
	sys.stdout.write(n)





def createLifeBonus():
	global monster1, monster2, monster3, player, monster4
	

	if not(monster4 == None):
		x = random.randint(10,40)
		y = random.randint(3,10)
		if not((x == monster1["positionX"] and y == monster1["positionY"]) or (x == monster2["positionX"] and y == monster2["positionY"]) or (x == monster3["positionX"] and y == monster3["positionY"]) or (x == player["positionX"] and y == player["positionY"]) or (x == monster4["positionX"] and y == monster4["positionY"]))  :
			finalX = x
			finalY = y
		else : 
			finalX = 25
			finalY = 5
		Life = {'Lx': finalX, 'Ly': finalY, 'valeur':5.0, 'color': 8, 'etat': "V"}

	else:
		x = random.randint(10,40)
		y = random.randint(3,10)
		if not((x == monster1["positionX"] and y == monster1["positionY"]) or (x == monster2["positionX"] and y == monster2["positionY"]) or (x == monster3["positionX"] and y == monster3["positionY"]) or (x == player["positionX"] and y == player["positionY"]))  :
			finalX = x
			finalY = y
		else : 
			finalX = 25
			finalY = 5
		Life = {'Lx': finalX, 'Ly': finalY, 'valeur':5.0, 'color': 8, 'etat': "V"}
	
	return Life


	


def showLifeBonus(Life):

	x = str(int(Life['Lx']))
	y = str(int(Life['Ly']))
	txt="\033["+y+";"+x+"H"
	sys.stdout.write(txt)

	sys.stdout.write("\033[40m")

	c = Life["color"]
	txt="\033[3"+str(c%7+1)+"m"
	sys.stdout.write(txt)
	
	n = Life["etat"]
	sys.stdout.write(n)





def createFileVie(player):
	i = 0
	myfile = open("vie.txt", "w")
	for i in range(59):
		myfile.write(" ")
	myfile.write("life : ")
	myfile.write( str(player["life"]) )
	myfile.close()





def lireVie(nomFichier):
	global vie
	vie = dict()
	myfile = open(nomFichier, "r")
	vie["str"]=myfile.read()
	myfile.close()
	
	a = vie["str"].split("\n")
	s , i = [] , 0
	for i in range(len(a)-1) :
		
		e = list(a[i].strip())
		s.append(e)
	vie["list"] = s
	




def showVie(vie):

	sys.stdout.write("\033[1;1H")
	
	#couleur fond 
	sys.stdout.write("\033[43m")
	
	
	#couleur fond
	sys.stdout.write("\033[40m")
	
	#couleur white
	sys.stdout.write("\033[34m")
	
	#affiche
	sys.stdout.write(str(vie["str"]))





def createFileVieMonster1(monster1):

	i = 0
	myfile = open("vieMonster1.txt", "w")
	myfile.write("\n")
	myfile.write("\n")
	myfile.write("\n")
	for i in range(55):
		myfile.write(" ")
	myfile.write("monster 1 life : ")
	myfile.write( str(monster1["life"]) )
	myfile.close()





def lireVieMonster1(nomFichier):
	global vieMonster1
	vieMonster1 = dict()
	myfile = open(nomFichier, "r")
	vieMonster1["str"]=myfile.read()
	myfile.close()
	
	a = vieMonster1["str"].split("\n")
	s , i = [] , 0
	for i in range(len(a)-1) :
		
		e = list(a[i].strip())
		s.append(e)
	vieMonster1["list"] = s
	




def showVieMonster1(vieMonster1):

	sys.stdout.write("\033[1;1H")
	
	#couleur fond 
	sys.stdout.write("\033[43m")
	
	
	#couleur fond
	sys.stdout.write("\033[40m")
	
	#couleur white
	sys.stdout.write("\033[34m")
	
	#affiche
	if monster1["life"] > 0:
		sys.stdout.write(str(vieMonster1["str"]))
	else :  sys.stdout.write("DEAD")




def createFileVieMonster2(monster2):
	
	i = 0
	myfile = open("vieMonster2.txt", "w")
	myfile.write("\n")
	myfile.write("\n")
	myfile.write("\n")
	myfile.write("\n")
	for i in range(55):
		myfile.write(" ")
	myfile.write("monster 2 life : ")
	myfile.write( str(monster2["life"]) )
	myfile.close()





def lireVieMonster2(nomFichier):
	global vieMonster2
	vieMonster2 = dict()
	myfile = open(nomFichier, "r")
	vieMonster2["str"]=myfile.read()
	myfile.close()
	
	a = vieMonster2["str"].split("\n")
	s , i = [] , 0
	for i in range(len(a)-1) :
		
		e = list(a[i].strip())
		s.append(e)
	vieMonster2["list"] = s
	




def showVieMonster2(vieMonster2):

	sys.stdout.write("\033[1;1H")
	
	#couleur fond 
	sys.stdout.write("\033[43m")
	
	
	#couleur fond
	sys.stdout.write("\033[40m")
	
	#couleur white
	sys.stdout.write("\033[34m")
	
	#affiche
	if monster2["life"] > 0:
		sys.stdout.write(str(vieMonster2["str"]))
	else :  sys.stdout.write("DEAD")





def createFileVieMonster3(monster3):
	global numero_zone

	i = 0
	myfile = open("vieMonster3.txt", "w")
	myfile.write("\n")
	myfile.write("\n")
	myfile.write("\n")
	myfile.write("\n")
	myfile.write("\n")
	for i in range(55):
		myfile.write(" ")
	if numero_zone != 3 :
		myfile.write("monster 3 life : ")
	if numero_zone == 3 :
		myfile.write("  ")
		myfile.write("BOSS life : ")
	myfile.write( str(monster3["life"]) )
	myfile.close()





def lireVieMonster3(nomFichier):
	global vieMonster3
	vieMonster3 = dict()
	myfile = open(nomFichier, "r")
	vieMonster3["str"]=myfile.read()
	myfile.close()
	
	a = vieMonster3["str"].split("\n")
	s , i = [] , 0
	for i in range(len(a)-1) :
		
		e = list(a[i].strip())
		s.append(e)
	vieMonster3["list"] = s
	




def showVieMonster3(vieMonster3):
	global monster3

	sys.stdout.write("\033[1;1H")
	
	#couleur fond 
	sys.stdout.write("\033[43m")
	
	
	#couleur fond
	sys.stdout.write("\033[40m")
	
	#couleur white
	sys.stdout.write("\033[34m")
	
	#affiche
	if monster3["life"] > 0:
		sys.stdout.write(str(vieMonster3["str"]))
	else :
		sys.stdout.write("monster 3 life : Dead")




def createFileVieMonster4(monster4):
	
	if not(monster4 == None):
		i = 0
		myfile = open("vieMonster4.txt", "w")
		myfile.write("\n")
		myfile.write("\n")
		myfile.write("\n")
		myfile.write("\n")
		myfile.write("\n")
		myfile.write("\n")
		for i in range(55):
			myfile.write(" ")
		myfile.write("monster 4 life : ")
		myfile.write( str(monster4["life"]) )
		myfile.close()





def lireVieMonster4(nomFichier):
	global vieMonster4
	if not(monster4 == None):
		vieMonster4 = dict()
		myfile = open(nomFichier, "r")
		vieMonster4["str"]=myfile.read()
		myfile.close()
	
		a = vieMonster4["str"].split("\n")
		s , i = [] , 0
		for i in range(len(a)-1) :
		
			e = list(a[i].strip())
			s.append(e)
		vieMonster4["list"] = s
	




def showVieMonster4(vieMonster4):

	if not(monster4 == None):

		sys.stdout.write("\033[1;1H")
	
		#couleur fond 
		sys.stdout.write("\033[43m")
	
	
		#couleur fond
		sys.stdout.write("\033[40m")
	
		#couleur white
		sys.stdout.write("\033[34m")
	
		#affiche
		if monster4["life"] > 0:
			sys.stdout.write(str(vieMonster4["str"]))
		else :  sys.stdout.write("DEAD")






def createFileForce(player):
	i = 0
	myfile = open("force.txt", "w")
	myfile.write("\n")
	for i in range(59):
		myfile.write(" ")
	myfile.write("force : ")
	myfile.write( str(player["strength"]) )
	myfile.close()






def lireForce(nomFichier):
	global force
	force = dict()
	myfile = open(nomFichier, "r")
	force["str"]=myfile.read()
	myfile.close()
	
	a = force["str"].split("\n")
	s , i = [] , 0
	for i in range(len(a)-1) :
		
		e = list(a[i].strip())
		s.append(e)
	force["list"] = s
	




def showForce(force):

	sys.stdout.write("\033[1;1H")
	
	#couleur fond 
	sys.stdout.write("\033[43m")
	
	
	#couleur fond
	sys.stdout.write("\033[40m")
	
	#couleur white
	sys.stdout.write("\033[34m")
	
	#affiche
	sys.stdout.write(str(force["str"]))





def createFileZone(Numero_zone):
	global numero_zone
	
	if numero_zone == 0 :
		i = 0
		myfile = open("numero_zone.txt", "w")
		for i in range(14):
			myfile.write("\n")
		i = 0
		for i in range(20):
			myfile.write(" ")
		myfile.write("zone : ")
		myfile.write("1")
		myfile.write("\n")
		i = 0
		for i in range(17):
			myfile.write(" ")
		myfile.write(" Difficulte : ")
		myfile.write("*")
		myfile.close()
	if numero_zone != 0 :
		i = 0
		myfile = open("numero_zone.txt", "w")
		for i in range(19):
			myfile.write("\n")
		i = 0
		for i in range(21):
			myfile.write(" ")
		myfile.write("zone : ")
		i = 0
		myfile.write(str(numero_zone+1))
		myfile.write("\n")
		for i in range(18):
			myfile.write(" ")
		myfile.write("Difficulte : ")
		i = 0
		for i in range(numero_zone+1):
			myfile.write("*")
		if numero_zone == 3 :
			myfile.write("\n")
			myfile.write("\n")
			i = 0
			for i in range(19):
				myfile.write(" ")
			myfile.write("DERNIERE VAGUE")
			myfile.write("\n")
			
			i = 0
			for i in range(20):
				myfile.write(" ")
			myfile.write("ZONE DU BOSS")
		myfile.close()





def lireZone(nomFichier):
	global zone

	zone = dict()
	myfile = open(nomFichier, "r")
	zone["str"]=myfile.read()
	myfile.close()
	a = zone["str"].split("\n")
	s , i = [] , 0
	for i in range(len(a)-1) :
		
		e = list(a[i].strip())
		s.append(e)
	zone["list"] = s
	




def showZone(zone):

	sys.stdout.write("\033[1;1H")
	
	#couleur fond 
	sys.stdout.write("\033[43m")
	
	
	#couleur fond
	sys.stdout.write("\033[40m")
	
	#couleur white
	sys.stdout.write("\033[34m")
	
	#affiche
	sys.stdout.write(str(zone["str"]))





def moveMonster(monster) :
	global player, Background, Life, Weapon

	if monster["etat"] == "E" or monster["etat"] == "B":
		y = monster["positionY"]
		x = monster["positionX"]
		x0 = monster["positionX"]
		y0 = monster["positionY"]
		while (x<1 or y<1 or x>45 or y>20  or (x0 == x and y0 == y)) or (x == Life['Lx'] and y == Life['Ly']) or (x == Weapon['Wx'] and y == Weapon['Wy']) or Background["list"][y][x-1] != ' ' or Background["list"][y][x] != ' ' or Background["list"][y-1][x] != ' ' or Background["list"][y-2][x] != ' ' or Background["list"][y-2][x-2] != ' ' or Background["list"][y][x-2] != ' ' or Background["list"][y-1][x-2] != ' ' or Background["list"][y-2][x-1] != ' ':
			x = monster["positionX"] + random.randint(0,1)*2 - 1
			y = monster["positionY"] + random.randint(0,1)*2 - 1
		
		monster["positionX"] = x
		monster["positionY"] = y





def move():
	global monster1, monster2, monster3, monster4
	moveMonster(monster1)
	moveMonster(monster2)
	moveMonster(monster3)
	if not(monster4 == None):
		moveMonster(monster4)





def playerRegen(player):
	global Life

	if player["positionX"] == Life['Lx'] and player["positionY"] == Life['Ly'] :
		player["life"] = player["life"] + Life['valeur']
		Life['valeur'] = 0.0
		Life["etat"] = " "
		Life['Lx'] = 200.0
		Life['Ly'] = 200.0





def playerWeapon(player):
	global Weapon

	if player["positionX"] == Weapon["Wx"] and player["positionY"] == Weapon["Wy"] :
		player["strength"] = player["strength"] + Weapon["valeur"]
		Weapon['valeur'] = 0.0
		Weapon['etat'] = " "
		Weapon['Wx'] = 200.0
		Weapon['Wy'] = 200.0





def interact():

	global player, Background, monster1, monster2, monster3, page_accueil, play_again, valeur_play_again, monster4

	if isData():
		c = sys.stdin.read(1)
		if c == '\x1b':
			quitGame()
		elif c == 'w' and page_accueil == 0 :
			page_accueil = 1
		elif c == 'z':
			y = player["positionY"] - 1
			x = player["positionX"]
			if Background["list"][y-1][x-1] == " " :
				player["positionY"] = y
		elif c == 'q':
			y = player["positionY"]
			x = player["positionX"] - 1
			if Background["list"][y-1][x-1] == " " :
				player["positionX"] = x
		elif c == 's':
			y = player["positionY"] + 1
			x = player["positionX"]
			if Background["list"][y-1][x-1] == " "  :
				player["positionY"] = y
		elif c == 'd':
			y = player["positionY"]
			x = player["positionX"] + 1
			if Background["list"][y-1][x-1] == " " :
				player["positionX"] = x
		elif c == 'b' : #Donne un coup
			perso.playerHit(player,monster1)
			perso.playerHit(player,monster2)
			perso.playerHit(player,monster3)
			if not(monster4 == None):
				perso.playerHit(player,monster4)
		elif c == 'w' and valeur_play_again == 1 :
			play_again = 1






def isData():

	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])





def show():
	global Background, player, monster1, monster2, monster3, vieMonster1, vieMonster2, vieMonster3, Life, Weapon, numero_zone, monster4, vieMonster4

	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")

	#affichage des different element
	showVie(vie)
	showForce(force)

	showVieMonster1(vieMonster1)
	showVieMonster2(vieMonster2)
	showVieMonster3(vieMonster3)
	showVieMonster4(vieMonster4)
	showZone(zone)
	background.show(Background)
	
	showWeaponBonus(Weapon)
	showLifeBonus(Life)
	perso.showMonster(monster1)
	perso.showMonster(monster2)
	perso.showMonster(monster3)
	if not(monster4 == None):
		perso.showMonster(monster4)
	perso.showPlayer(player)
	
	
	

	#restoration couleur 
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")

	#deplacement curseur
	sys.stdout.write("\033[0;0H\n")





def changeZone():
	global monster1, monster2, monster3, Background, numero_zone, Life, Weapon, monster4

	if monster1["etat"] == "D" and monster2["etat"] == "D" and monster3["etat"] == "D" and numero_zone == 0 :
		Background = background.create("zone2.txt")
		monster1["etat"] = "E"
		monster2["etat"] = "E"
		monster3["etat"] = "E"
		monster1["life"] = 20.0
		monster2["life"] = 20.0
		monster3["life"] = 20.0
		monster1["strength"] = 2.0
		monster2["strength"] = 2.0
		monster3["strength"] = 2.0
		monster1["positionX"] = random.randint(5,35)
		monster1["positionY"] = random.randint(5,10)
		monster2["positionX"] = random.randint(5,35)
		monster2["positionY"] = random.randint(5,10)
		monster3["positionX"] = random.randint(5,35)
		monster3["positionY"] = random.randint(5,10)

		x = random.randint(10,40)
		y = random.randint(3,10)
		if not((x == monster1["positionX"] and y == monster1["positionY"]) or (x == monster2["positionX"] and y == monster2["positionY"]) or (x == monster3["positionX"] and y == monster3["positionY"]) or (x == player["positionX"] and y == player["positionY"])) :
			finalX = x
			finalY = y
		else:
			finalX = 25
			finalY = 5
		Life['Lx'] = finalX
		Life['Ly'] = finalY
		Life['etat'] = "V"
		Life['valeur'] = 10.0
	
		player["life"] = 100.0
		numero_zone += 1


	if monster1["etat"] == "D" and monster2["etat"] == "D" and monster3["etat"] == "D" and numero_zone == 1 :
		monster1["etat"] = "E"
		monster2["etat"] = "E"
		monster3["etat"] = "E"
		monster1["life"] = 30.0
		monster2["life"] = 30.0
		monster3["life"] = 50.0
		monster1["strength"] = 4.0
		monster2["strength"] = 4.0
		monster3["strength"] = 6.0
		monster1["positionX"] = random.randint(5,35)
		monster1["positionY"] = random.randint(5,10)
		monster2["positionX"] = random.randint(5,35)
		monster2["positionY"] = random.randint(5,10)
		monster3["positionX"] = random.randint(5,35)
		monster3["positionY"] = random.randint(5,10)
		monster3["color"] = 5

		x = random.randint(10,40)
		y = random.randint(3,10)
		if not((x == monster1["positionX"] and y == monster1["positionY"]) or (x == monster2["positionX"] and y == monster2["positionY"]) or (x == monster3["positionX"] and y == monster3["positionY"]) or (x == player["positionX"] and y == player["positionY"])) :
			finalX = x
			finalY = y
		else :
			finalX = 25
			finalY = 5
		Life['Lx'] = finalX
		Life['Ly'] = finalY
		Life['etat'] = "V"
		Life['valeur'] = 15.0


		numero_zone += 1

		player["life"] = 100.0

	if monster1["etat"] == "D" and monster2["etat"] == "D" and monster3["etat"] == "D" and numero_zone == 2 :
		monster1["etat"] = "E"
		monster2["etat"] = "E"
		monster3["etat"] = "B"
		monster1["life"] = 50.0
		monster2["life"] = 50.0
		monster3["life"] = 150.0
		monster1["strength"] = 10.0
		monster2["strength"] = 10.0
		monster3["strength"] = 25.0
		monster1["positionX"] = random.randint(5,35)
		monster1["positionY"] = random.randint(5,10)
		monster2["positionX"] = random.randint(5,35)
		monster2["positionY"] = random.randint(5,10)
		monster3["positionX"] = random.randint(5,35)
		monster3["positionY"] = random.randint(5,10)

		monster4 = perso.createMonster(Mname="monster",
					MpositionX=random.randint(10,40),
					MpositionY=random.randint(5,10),
					Mspeed=1.0,
					Mstrength=10.0,
					Mlife=50.0,
					Mweapon="poing",
					Mcolor=0,
					Mnumero=1,
					Metat="E")
		
		x = random.randint(10,40)
		y = random.randint(3,10)
		if not((x == monster1["positionX"] and y == monster1["positionY"]) or (x == monster2["positionX"] and y == monster2["positionY"]) or (x == monster3["positionX"] and y == monster3["positionY"]) or (x == player["positionX"] and y == player["positionY"]) or (x == monster4["positionX"] and y == monster4["positionY"])) :
			finalX = x
			finalY = y
		else :
			finalX = 25
			finalY = 5
		Life['Lx'] = finalX
		Life['Ly'] = finalY
		Life['etat'] = "V"
		Life['valeur'] = 25.0

		numero_zone += 1

		player["life"] = 200.0
		player["strength"] = 20.0

		x = random.randint(10,40)
		y = random.randint(3,10)
		if not((x == monster1["positionX"] and y == monster1["positionY"]) or (x == monster2["positionX"] and y == monster2["positionY"]) or (x == monster3["positionX"] and y == monster3["positionY"]) or (x == player["positionX"] and y == player["positionY"]) or (x == Life['Lx'] and y == Life['Ly']) or (x == monster4["positionX"] and y == monster4["positionY"])) :
			finalX = x
			finalY = y
		else : 
			finalX = 20
			finalY = 5
		Weapon['Wx'] = finalX
		Weapon['Wy'] = finalY

		Weapon['etat'] = "|"
		
		

		
		
	



def playerWin(player):
	global Background, monster1, monster2, monster3, numero_zone, vie, force, valeur_play_again, monster4

	if player["life"] > 0 and monster1["etat"] == "D" and monster2["etat"] == "D" and monster3["etat"] == "D" and monster4["etat"] == "D" and numero_zone == 3 :
		Background = background.create("victory.txt")
		monster1["positionX"]=200.0
		monster1["positionY"]=200.0
		monster1["etat"]=" "
		monster2["positionX"]=200.0
		monster2["positionY"]=200.0
		monster2["etat"]=" "
		monster3["positionX"]=200.0
		monster3["positionY"]=200.0
		monster3["etat"]=" "
		player["life"] = " "
		player["strength"] = " "
		monster1["life"] = " "
		monster2["life"] = " "
		monster3["life"] = " "

		Life['Lx'] = 200.0
		Life['Ly'] = 200.0
		Life['etat'] = " "
		Life['valeur'] = 0.0

		Weapon['Wx'] = 200.0
		Weapon['Wy'] = 200.0
		Weapon['etat'] = " "
		Weapon['valeur'] = 0.0

		valeur_play_again = 1
		
		monster4 = None





def deathPlayer(player):
	global Background, monster1, monster2, monster3, valeur_play_again, monster4
	
	if player["life"] <= 0.0 :
		monster1["etat"]=" "
		monster2["etat"]=" "
		monster3["etat"]=" "
		Background = background.create("defeat.txt")
		
		monster1["positionX"]=200.0
		monster1["positionY"]=200.0
		
		monster2["positionX"]=200.0
		monster2["positionY"]=200.0
		
		monster3["positionX"]=200.0
		monster3["positionY"]=200.0
		
		player["life"] = " "
		player["strength"] = " "
		monster1["life"] = " "
		monster2["life"] = " "
		monster3["life"] = " "

		Life['Lx'] = 200.0
		Life['Ly'] = 200.0
		Life['etat'] = " "
		Life['valeur'] = 0.0

		Weapon['Wx'] = 200.0
		Weapon['Wy'] = 200.0
		Weapon['etat'] = " "
		Weapon['valeur'] = 0.0
		
		valeur_play_again = 1

		monster4 = None
		




def lireAccueil(nomFichier) :
	global accueil
	accueil = dict()
	myfile = open(nomFichier, "r")
	accueil["str"]=myfile.read()
	myfile.close()
	
	a = accueil["str"].split("\n")
	s , i = [] , 0
	for i in range(len(a)-1) :
		
		e = list(a[i].strip())
		s.append(e)
	accueil["list"] = s
	




def showAccueil(accueil):

	sys.stdout.write("\033[1;1H")
	
	#couleur fond 
	sys.stdout.write("\033[43m")
	
	
	#couleur fond
	sys.stdout.write("\033[40m")
	
	#couleur white
	sys.stdout.write("\033[36m")
	
	#affiche
	sys.stdout.write(str(accueil["str"]))





def playAgain():
	global play_again, monster1, monster2, monster3, Background, valeur_play_again, numero_zone, Weapon, monster4
	
	if play_again == 1 :
		
		player["positionX"] = 25
		player["positionY"] = 11
		player["strength"] = 5.0
		player["life"] = 100.0
		player["color"] = 2

		Background = background.create("zone.txt")
		
		monster1["positionX"] = positionX1
		monster1["positionY"] = positionY1
		monster1["strength"] = 1.0
		monster1["life"] = 10.0
		monster1["color"] = 0
		monster1["etat"] = "E"	
		
		monster2["positionX"] = positionX2
		monster2["positionY"] = positionY2
		monster2["strength"] = 1.0
		monster2["life"] = 10.0
		monster2["color"] = 0
		monster2["etat"] = "E"

		monster3["positionX"] = positionX3
		monster3["positionY"] = positionY3
		monster3["strength"] = 1.0
		monster3["life"] = 10.0
		monster3["color"] = 0
		monster3["etat"] = "E"
		
		x = random.randint(10,40)
		y = random.randint(3,10)

		monster4 = None		

		if not((x == monster1["positionX"] and y == monster1["positionY"]) or (x == monster2["positionX"] and y == monster2["positionY"]) or (x == monster3["positionX"] and y == monster3["positionY"]) or (x == player["positionX"] and y == player["positionY"])) :
			finalX = x
			finalY = y
		else :
			finalX = 25
			finalY = 5
		Life['Lx'] = finalX
		Life['Ly'] = finalY
		Life['etat'] = "V"
		Life['valeur'] = 5.0

		Weapon['Wx'] = 200.0
		Weapon['Wy'] = 200.0
		Weapon['etat'] = " "
		Weapon['valeur'] = 0.0

		play_again = 0
		numero_zone = 0
		valeur_play_again = 0

	





def run():
	global timeStep, monster1, monster2, monster3, temps, page_accueil, numero_zone, Weapon, Life

	while 1:
		if page_accueil == 0:
			interact()
			lireAccueil("accueil.txt")
			showAccueil(accueil)
		if page_accueil == 1:
			interact()
			perso.deathMonster(monster1)
			perso.deathMonster(monster2)
			perso.deathMonster(monster3)
			if not(monster4 == None):
				perso.deathMonster(monster4)
			playerRegen(player)
			playerWeapon(player)
			deathPlayer(player)
			changeZone()
			createFileVie(player)
			lireVie("vie.txt")
			createFileVieMonster1(monster1)
			lireVieMonster1("vieMonster1.txt")
			createFileVieMonster2(monster2)
			lireVieMonster2("vieMonster2.txt")
			createFileVieMonster3(monster3)
			lireVieMonster3("vieMonster3.txt")
			createFileVieMonster4(monster4)
			lireVieMonster4("vieMonster4.txt")
			createFileForce(player)
			lireForce("force.txt")
			createFileZone(numero_zone)
			lireZone("numero_zone.txt")
			show()
			playAgain()
			playerWin(player)
			time.sleep(timeStep)
			temps += 1
			if temps == 4 :
				perso.monsterHit(player,monster1)
				perso.monsterHit(player,monster2)
				perso.monsterHit(player,monster3)
				if not(monster4 == None):
					perso.monsterHit(player,monster4)
				move()
				if numero_zone == 3 and monster3["etat"] == "B":
					monster3["color"] = monster3["color"] + 1
				elif numero_zone == 2 and monster3["etat"] == "E" :
					monster3["color"] = 5
				else : monster3["color"] = 0
					
				temps = 0





def quitGame():

	global old_settings
	
	#couleur white
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")
	
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
	sys.exit()







init()
run()
quitGame()


