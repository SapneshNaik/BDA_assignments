#1. Read the ‘sample.txt’ file and extract the phone numbers and email ids. 
#Extracted information need to be stored in ‘info.txt’.

import re


def main():

	with open('../question_n_source/sample.txt') as input_file:

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


if __name__ == "__main__":
	main()




