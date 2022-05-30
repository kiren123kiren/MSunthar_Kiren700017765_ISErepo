
#Module A1
#Function: Converting a string to upper case or lower case
def ModuleA1():
	print("1: Convert a string to upper case")
	print("2: Convert a string to lower case")
	selection_input = input()

	print("1: Input with keyboard")
	print("2: Input with text file")
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

#Module B1
#Function: Identify whether numeric values are in a given string
def ModuleB1():
	print("1: Input with keyboard")
	print("2: Input with text file")	
	input_method = input()
	
	if int(input_method) == 1:
		print("Please enter a string:")
		input_text = input()
	elif int(input_method) == 2:
		input_text = ModuleE1()
	else:
		print("Please enter a valid selection")
	
	
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
	print("1: Input with keyboard")
	print("2: Input with text file")
	input_method = input()

	if int(input_method) == 1:
		print("Please enter a string:")
		input_text = input()
	elif int(input_method) == 2:
		input_text = ModuleE1()
	else:
		print("Please enter a valid selection")
	
	result = input_text.isdigit()
	if result == True:
		output_text = "The given string is a valid number"
		print(output_text)
	else:
		output_text = "The given string is NOT a valid number"
		print(output_text)
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
print("Please select function that wanted to perform:")
print("1: Converting a string to upper case or lower case")
print("2: Identify whether numeric values are in a given string")
print("3: Identify whether a given string is a valid number or not")

print("Select?:")
select_func = input()

if int(select_func) == 1:
	ModuleA1()
elif int(select_func) ==2:
	ModuleB1()
elif int(select_func) ==3:
	ModuleC1()
else:
	print("Please select a valid Number!")

