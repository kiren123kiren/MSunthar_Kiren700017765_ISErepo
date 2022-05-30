#Module A2
#Function: Converting a number given in hours to minutes
def ModuleA2():
	print("Please enter hours that needed to convert to minutes: ")
	input_text = input()
	if not input_text.replace(".","",1).isdigit():
		print("Please enter a valid hours")
		return
	else:
		result = float(input_text) * 60
		print("{0} hours => {1} minutes".format(input_text,result))

#main part
ModuleA2()
