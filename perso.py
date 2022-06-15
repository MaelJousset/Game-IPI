import random
import background
import sys


def createMonster(Mname="noname",MpositionX=0,MpositionY=0,Mspeed=0.0,Mstrength=0.0,Mlife=0.0,Mweapon="noweapon", Mcolor="nocolor",Mnumero=0,Metat="E"):
	monster = {"name":Mname, "positionX":MpositionX,"positionY":MpositionY, "speed":Mspeed, "strength":Mstrength, "life":Mlife, "weapon":Mweapon, "color":Mcolor, "numero":Mnumero,"etat":Metat}
	return monster





def createPlayer(Pname="noname",PpositionX=0,PpositionY=0,Pspeed=0.0,Pstrength=0.0,Plife=0.0,
PactiveWeapon="noactiveweapon",Plevel=1,PlistWeapon=[],Pdirection = "nodirection",Pcolor="nocolor"):
	global player
	player = {"name":Pname, "positionX":PpositionX, "positionY":PpositionY, "speed":Pspeed, "strength":Pstrength, "life":Plife, "activeWeapon":PactiveWeapon, "level":Plevel, "listWeapon":PlistWeapon, "direction":Pdirection, "color":Pcolor}
	return player



	

Background = background.create("zone.txt")






#Accesseurs de monster
def getMonsterName(monster):
	return monster["name"]
def getMonsterPositionX(monster):
	return monster["positionX"]
def getMonsterPositionY(monster):
	return monster["positionY"]
def getMonsterSpeed(monster):
	return monster["speed"]
def getMonsterStrength(monster):
	return monster["strength"]
def getMonsterLife(monster):
	return monster["life"]
def getMonsterWeapon(monster):
	return monster["weapon"]





#Accesseurs de player
def getPlayerName(player):
	return player["name"]
def getPlayerPositionX(player):
	return player["positionX"]
def getPlayerPositionY(player):
	return player["positionY"]
def getPlayerSpeed(player):
	return player["speed"]
def getPlayerStrength(player):
	return player["strength"]
def getPlayerLife(player):
	return player["life"]
def getPlayerActiveWeapon(player):
	return player["activeWeapon"]
def getPlayerLevel(player):
	return player["level"]
def getPlayerListWeapon(player):
	return player["listWeapon"]
def getPlayerDicrection(player):
	return player["direction"]





#Mutateurs de monster
def setMonsterName(monster,Mname):
	monster["name"]=Mname
def setMonsterPositionX(monster,MpositionX):
	monster["positionX"]=MpositionX
def setMonsterPositionY(monster,MpositionY):
	monster["positionY"]=MpositionY
def setMonsterSpeed(monster,Mspeed):
	monster["speed"]=Mspeed
def setMonsterStrength(monster,Mstrength):
	monster["strength"]=Mstrength
def setMonsterLife(monster,Mlife):
	monster["life"]=Mlife
def setMonsterWeapon(monster,Mweapon):
	monster["weapon"]=Mweapon





#Mutateurs de player
def setPlayerName(player,Pname):
	player["name"] = Pname 
def setPlayerPositionX(player,PpositionX):
	player["positionX"] = PpositionX
def setPlayerPositionY(player,PpositionY):
	player["positionY"] = PpositionY
def setPlayerSpeed(player,Pspeed):
	player["speed"] = Pspeed
def setPlayerStrength(player,Pstrength):
	player["strength"] = Pstrength
def setPlayerLife(player,Plife):
	player["life"] = Plife
def setPlayerActiveWeapon(player,PactiveWeapon):
	player["activeWeapon"] = PactiveWeapon
def setPlayerLevel(player,Plevel):
	player["level"] = Plevel
def setPlayerListWeapon(player,PlistWeapon):
	player["listWeapon"] = PlistWeapon
def setPlayerDirection(player,Pdirection):
	player["direction"] = Pdirection






#operateurs de player
def playerHit(player,monster):
	x1 = player["positionX"]
	y1 = player["positionY"]
	x2 = monster["positionX"]
	y2 = monster["positionY"]
	if ((x2-1)<=x1<=(x2+1)) and ((y2-1)<=y1<=(y2+1)):
		monster["life"] = monster["life"] - player["strength"]





def monsterHit(player,monster):
	x1 = player["positionX"]
	y1 = player["positionY"]
	x2 = monster["positionX"]
	y2 = monster["positionY"]
	if ((x1-1)<=x2<=(x1+1)) and ((y1-1)<=y2<=(y1+1)):
		player["life"] = player["life"] - monster["strength"]





def showPlayer(player):

	x = str(int(player["positionX"]))
	y = str(int(player["positionY"]))
	txt="\033["+y+";"+x+"H"
	sys.stdout.write(txt)

	sys.stdout.write("\033[40m")

	c = player["color"]
	txt="\033[3"+str(c%7+1)+"m"
	sys.stdout.write(txt)

	sys.stdout.write("O\n")





def showMonster(monster):

	g = monster["etat"]

	x = str(int(monster["positionX"]))
	y = str(int(monster["positionY"]))
	txt="\033["+y+";"+x+"H"
	sys.stdout.write(txt)

	sys.stdout.write("\033[40m")

	c = monster["color"]
	txt="\033[3"+str(c%7+1)+"m"
	sys.stdout.write(txt)

	sys.stdout.write(g)





def deathMonster(monster):
	
	if monster["life"] <= 0 :
		monster["etat"] = "D"
		monster["strength"] = 0.0
		




