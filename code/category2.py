#Module A2
#Function: Converting a number given in hours to minutes
def ModuleA2():
	print("Please enter hours that needed to convert to minutes: ")
	for input_text in ModuleE2():
		input_text = input_text.rstrip('\n')
		if not input_text.replace(".","",1).isdigit():
			print("Please enter valid hours")
			return
		else:
			result = float(input_text) * 60
			print("{0} hours => {1} minutes".format(input_text,result))

#Module E2
#Function: Input value with a text file
def ModuleE2():
	try:
		f = open("../document/inCategory2.txt","r")
		for line in f:
			yield line
	finally:
		f.close()

#main part
ModuleA2()
