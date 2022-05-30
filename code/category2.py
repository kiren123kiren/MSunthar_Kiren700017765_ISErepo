#Module A2
#Function: Converting a number given in hours to minutes
def ModuleA2():
	input_text = input()
	if not input_text.isdigit():
		print("Please enter a valid hours")
		return
	else:
		result = input_text * 60

#main part
ModuleA2()
