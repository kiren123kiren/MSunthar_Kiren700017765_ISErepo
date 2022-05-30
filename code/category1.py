#Module A1
#Function: Converting a string to upper case or lower case
def ModuleA1():
	print("Convert a string to upper case, Press 1")
	print("Convert a string to lower case, Press 2")
	selection_input = input()
	print("Please enter a string:")
	input_text = input()

	if int(selection_input) == 1:
		output_text = input_text.upper()
		print("The Upper-case of {0} is {1}".format(input_text,output_text))
	elif int(selection_input) == 2:
		output_text = input_text.lower()
		print("The Lower-case of {0} is {1}".format(input_text,output_text)) 
	else:
		print("Please select available selection!")
#main_part
ModuleA1()

