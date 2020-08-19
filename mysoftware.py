import os

while True:
	print("Please tell me what you want me to do? - ", end='')
	x = input()
	y = x.upper()

	if ((("OPEN" in y) or ("RUN" in y) or ("EXECUTE" in y) or ("TURN ON" in y) or ("START" in y) or ("BEGIN" in y) or ("COMMENCE" in y) or ("INITIATE" in y) or ("SWITCH" in y) or ("ENTER" in y)) and (("GOOGLE CHROME" in y) or ("GOOGLE" in y) or ("CHROME" in y) or ("BROWSER" in y) or ("DEFAULT BROWSER" in y) or ("INTERNET" in y))):
		os.system("chrome")

	elif((("OPEN" in y) or ("RUN" in y) or ("EXECUTE" in y) or ("TURN ON" in y) or ("START" in y) or ("BEGIN" in y) or ("COMMENCE" in y) or ("INITIATE" in y) or ("SWITCH" in y) or ("ENTER" in y)) and (("FIREFOX" in y) or ("MOZILLA FIREFOX" in y))):
		os.system("firefox")

	elif((("OPEN" in y) or ("RUN" in y) or ("EXECUTE" in y) or ("TURN ON" in y) or ("START" in y) or ("BEGIN" in y) or ("COMMENCE" in y) or ("INITIATE" in y) or ("SWITCH" in y) or ("ENTER" in y)) and (("NOTEPAD" in y) or ("TEXT EDITOR" in y) or ("TEXT FILE" in  y))):
		os.system("notepad") 

	elif ("CLOSE" in y) or ("SHUT" in y) or ("END" in y) or ("TURN OFF" in y) or ("BREAK OFF" in y) or ("TERMINATE" in y) or ("FINISH" in y) or ("ADJOURN" in y) or ("HALT" in y) or ("DISCONTINUE" in y) or ("QUIT" in y) or ("BREAK" in y) or ("DISCARD" in y) or ("OVER" in  y):
		break
	else:
		print("Please re-enter your request. Maybe try using open or run with your command!")