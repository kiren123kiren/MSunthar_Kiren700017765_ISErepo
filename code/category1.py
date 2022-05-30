#Module A1
#Function: Converting a string to upper case or lower case
def ModuleA1():
	print("Convert a string to upper case, Press 1")
	print("Convert a string to lower case, Press 2")
	selection_input = input()

	print("Input with keyboard, Press 1")
	print("Input with text file, Press 2")
	input_method = input()

	if int(input_method) == 1:
		print("Please enter a string:")
		input_text = input()
	elif int(input_method) == 2:
		input_text = ModuleE1()
	else:
		print("Please enter a valid selection")		

	if int(selection_input) == 1:
		output_text = input_text.upper()
		print("The Upper-case of {0} is {1}".format(input_text,output_text))
	elif int(selection_input) == 2:
		output_text = input_text.lower()
		print("The Lower-case of {0} is {1}".format(input_text,output_text)) 
	else:
		print("Please select available selection!")
		output_text = ""
		
	ModuleF1(output_text)

#Module E1
#Function: Input value with a text file
def ModuleE1():
	try:
		f=open("../document/inCategory1.txt","r")
		input_text = f.read()
		return input_text
	finally:
		f.close()

#Module F1
#Function: Output value to a text file
def ModuleF1(output_text):
	try:
		f=open("../document/outCategory1.txt","w")
		f.write(output_text)		
	finally:
		f.close()

#main_part
ModuleA1()

