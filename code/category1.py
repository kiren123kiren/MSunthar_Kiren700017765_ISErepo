
#Module A1
#Function: Converting a string to upper case or lower case
def ModuleA1(module_output):
	print("1: Convert a string to upper case")
	print("2: Convert a string to lower case")
	selection_input = input()
	if(not selection_input.isdigit()):
		print("Please enter a valid digit number!")
		return
	
	if module_output == "":
		input_text = input_option()
				
	else:
		input_text = module_output
	
	if input_text != "":
		if int(selection_input) == 1:
			output_text = input_text.upper()
			print("Upper case: {0}".format(output_text))
		elif int(selection_input) == 2:
			output_text = input_text.lower()
			print("Lower case: {0}".format(output_text)) 
		else:
			print("Please select available selection!")
			output_text = ""	
		ModuleF1(output_text)

#Module B1
#Function: Identify whether numeric values are in a given string
def ModuleB1():
	input_text = input_option()
	if input_text != "":
		result = any(map(str.isdigit,input_text))
		if result == True:
			output_text = "The given string contain numeric values"
			print(output_text)
		else:
			output_text = "The given string DOES NOT contain numeric values"
			print(output_text)
		ModuleF1(output_text)

#Module C1
#Function: Identify whether a given string is a valid number or not
def ModuleC1():
	input_text = input_option()
	if input_text != "":
		result = input_text.isdigit()
		if result == True:
			output_text = "The given string is a valid number"
			print(output_text)
		else:
			output_text = "The given string is NOT a valid number"
			print(output_text)
		ModuleF1(output_text)

#Module D1
#Function: Remove any numeric values in a given string and then convert the string to upper case or lower case
def ModuleD1():
	input_text = input_option()
	if input_text != "":
		output_text = ""
		for c in input_text:
			if c.isdigit():
				continue
			else:
				output_text += c
		return output_text

#Module E1
#Function: Input value with a text file
def ModuleE1():
	try:
		f=open("../document/inCategory1.txt","r")
		input_text = f.read()
		return input_text.rstrip('\n')
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

#Module Input Option
#Function: Allow user to select specific input method
def input_option():
	print("1: Input with keyboard")
	print("2: Input with text file")
	input_method = input()
	if not input_method.isdigit():
		print("Please enter a valid digit number")
		return
	input_text = ""
	if int(input_method) == 1:
		print("Please enter a string:")
		input_text = input()
	elif int(input_method) == 2:
		input_text = ModuleE1()
	else:
		print("Please enter a valid selection")
	return input_text
	
#main_part
print("Please select function that wanted to perform:")
print("1: Converting a string to upper case or lower case")
print("2: Identify whether numeric values are in a given string")
print("3: Identify whether a given string is a valid number or not")
print("4: Remove any numeric values in a given string and then convert the string to upper case or lower case")

print("Select?:")
select_func = input()
if not select_func.isdigit():
	print("Please enter a valid digit number!")
else:
	if int(select_func) == 1:
		ModuleA1("")
	elif int(select_func) == 2:
		ModuleB1()
	elif int(select_func) == 3:
		ModuleC1()
	elif int(select_func) == 4:
		module_output = ModuleD1()
		ModuleA1(module_output)
	else:
		print("Please select a valid Number!")

