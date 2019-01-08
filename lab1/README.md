1. Read the ‘sample.txt’ file and extract the phone numbers and email ids. Extracted information need to be stored in ‘info.txt’. 
2. Read the file ‘state-place.txt’ which is copy pasted from wiki pages. It starts with state name with constant word [edit] followed by place name with or without college/ university name. Parse the text file and create a csv file with two columns. First will be state name and second is the place name. Entries in the csv file will be data extracted from text file.
3. Reading from and writing to csv files using lists and dictionaries. You are provided with sample.csv file and implement the following.
Read_fieldnames() : It should return the field names (column names) for the given csv file
Read_csv_as_list_dict():  Returns a list of dictionaries where each item in the list  corresponds to a row in the CSV file.  The dictionaries in the list map the field names to the field values for that row.
Write_csv_as_list_dict(): to this method pass the field names we get from first method, list of dictionaries which we get from second method and new file name as the third parameter. Code should create new csv file with given file name, field names and write the data supplied.
4. Design a HTML parser in python which is capable of extracting ‘data’ by ignoring the tags and their attributes. The “data” should be written ‘data.txt’. Input to the script is html file.
5. Assume that we have a folder with name ‘mix-files’, which contains many sub folders. Each sub folders may contain ‘n’ number of different types of files (.java, .py, .c, .txt, .html … etc). Write python script which identifies different types of files under all sub folders of ‘mix-files’ folder. After identifying different types of file, create sub folders for each type of files and move the corresponding type of files that folders ie.  ‘.c’ files to ‘c-folder’, .java files to ‘java-folder’ etc.



https://en.wikipedia.org/wiki/List_of_college_towns#College_towns_in_the_United_States
