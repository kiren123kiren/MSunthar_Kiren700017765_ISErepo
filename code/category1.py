#Module A1
#Function: Converting a string to upper case or lower case
def ModuleA1(text):
	new_text = text.upper()
	return new_text

#main_part
print("Please enter a string\n")
input_text = input()

output_text = ModuleA1(input_text)
print("Upper case text:{0}".format(output_text))

