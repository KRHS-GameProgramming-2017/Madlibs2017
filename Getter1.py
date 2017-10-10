def getMenuResponse(debug = False):
	if debug: print "--In getMenuResponse function--"
	goodInput = False
	while not goodInput:
		response = raw_input("Make a selection please: ")
		if (response == "1" or 
			response == "one" or 
			response == "story 1"):
				goodInput = True
				response = "1"
		elif (response == "q" or 
			  response == "quit" or 
			  response == "exit"):
			goodInput = True
			response = "q"
		else:
			print "Please enter a valid input!"
	return response
		
def getWord(prompt):
	if debug: print "--In getWord function--"
	goodInput = False
	while not goodInput:
		response = raw_input(prompt)
		if isSwear(response):
			goodInput = False
			print "Don't go using that type of language here"
		elif word == "":
			goodInput = False
			print "Type something"
		else:
			goodInput = True
	return response
			
			
def isSwear(word):
	swearList = ["poop",
				 "dumb",
				 "stupid"]
	if word.lower() in swearList:
		return True
	else:
		return False
	
