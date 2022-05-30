#Module A2
#Function: Converting a number given in hours to minutes
def ModuleA2():
	output_file = open("../document/outCategory2.txt","w")
	for input_text in ModuleE2():
		input_text = input_text.rstrip('\n')
		if not input_text.replace(".","",1).isdigit():
			print("Please enter valid hours")
			return
		else:
			result = float(input_text) * 60
			result = round(result,4)
			output_file.write(str(result)+"\n")
			print("{0} hours => {1} minutes".format(input_text,result))
	output_file.close()

#Module B2
#Function: Converting a number given in minutes to hours
def ModuleB2():
	output_file = open("../document/outCategory2.txt","w")
	for input_text in ModuleE2():
		input_text = input_text.rstrip('\n')
		if not input_text.replace(".","",1).isdigit():
			print("Please enter valid minutes")
			return
		else:
			result = float(input_text) / 60
			result = round(result,4)
			output_file.write(str(result)+"\n")
			print("{0} minutes => {1} hours".format(input_text,result))
	output_file.close()

#Module C2
#Function: Converting a number given in minutes to seconds
def ModuleC2():
	output_file = open("../document/outCategory2.txt","w")
	for input_text in ModuleE2():
		input_text = input_text.rstrip('\n')
		if not input_text.replace(".","",1).isdigit():
			print("Please enter valid minutes")
			return	
		else:
			result = float(input_text) * 60
			result = round(result,4)
			output_file.write(str(result) + "\n")
			print("{0} minutes => {1} seconds".format(input_text,result))
	output_file.close()

#Module D2
#Function: Converting a number given in seconds to minutes
def ModuleD2():
	output_file = open("../document/outCategory2.txt","w")
	for input_text in ModuleE2():
		input_text = input_text.rstrip('\n')
		if not input_text.replace(".","",1).isdigit():
			print("Please enter valid seconds")
			return
		else:
			result = float(input_text) / 60
			result = round(result,4)
			output_file.write(str(result) + "\n")
			print("{0} seconds => {1} minutes".format(input_text,result))
	output_file.close()

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
print("Please select conversion that needed:")
print("1: Converting a number given in hours to minutes")
print("2: Converting a number given in minutes to hours")
print("3: Converting a number given in minutes to seconds")
print("4: Converting a number given in seconds to minutes")
select_func = input()
if not select_func.isdigit():
	print("Please enter a valid digit number!")
else:
	if int(select_func) == 1:
		ModuleA2()
	elif int(select_func) == 2:
		ModuleB2()
	elif int(select_func) == 3:
		ModuleC2()
	elif int(select_func) == 4:
		ModuleD2()
	else:
		print("Please select a valid option")
