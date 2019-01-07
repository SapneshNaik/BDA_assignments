#4. Design a HTML parser in python which is capable of extracting ‘data’ by ignoring the tags and their attributes. 
# The “data” should be written ‘data.txt’. 
# Input to the script is html file.

import re

def main():
	with open('../question_n_source/sample.html') as html_file:
		parser = lambda text: re.sub(r'<.+?>', '', text)

		with open('data.txt', 'w') as output:
			output.write(parser(html_file.read()))


if __name__ == "__main__":
	main()