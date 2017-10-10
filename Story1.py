from Getter1 import *

def story1(debug= False):
	if debug: print "--In story1 function--"
	
	friend1 = getWord("A Name: ")
	
	out = ""
	out += "One day me and my friend, " + friend1
	
	return out
