import sys






def create(filename):
	#creation du fond
	bg=dict()

	#ouverture fichier
	myfile = open(filename, "r")
	bg["str"]=myfile.read()
	myfile.close()
	
	a = bg["str"].split("\n")
	s , i = [] , 0
	for i in range(len(a)-1) :
		
		e = list(a[i].strip())
		s.append(e)
	bg["list"] = s
	
	return bg





def show(bg) : 

	
	#goto
	sys.stdout.write("\033[1;1H")
	
	
	
	
	#couleur fond
	sys.stdout.write("\033[40m")
	
	#couleur white
	sys.stdout.write("\033[34m")
	
	#affiche
	sys.stdout.write(bg["str"])



