
import re

with open('sample.txt') as input_file:

	#extract all text from file
	text = input_file.read()

	#extract all email addresses from text
	emails = re.findall("\S+@\S+", text)  

	#extract all phone numbers with hypyen from text
	phone_no_hyphen = re.findall("\d{2}-\d{4}-\d{8}", text)

	#extract all phone numbers with brackers from text
	phone_no_brackets = re.findall("\(\d{2}\)\(\d{4}\)\(\d{8}\)", text)

	#extract all phone numbers with spaces from text
	phone_no_spaces = re.findall("\d{2} \d{4} \d{8}", text)
  

# print(emails) 
# print(phone_no_hyphen) 
# print(phone_no_spaces) 
# print(phone_no_brackets) 

with open('info.txt', 'w') as output_file:

	output_file.write("\n--EMAILS--\n")

	#store emails onto info.txt
	for mail in emails:
		output_file.write(mail)
		output_file.write("\n")


	#store phone numbers onto info.txt

	output_file.write("\n--PHONE NUMBERS--\n")

	for phone_no in phone_no_spaces:
		output_file.write(phone_no)
		output_file.write("\n")


	for phone_no in phone_no_hyphen:
		output_file.write(phone_no)
		output_file.write("\n")


	for phone_no in phone_no_brackets:
		output_file.write(phone_no)
		output_file.write("\n")




