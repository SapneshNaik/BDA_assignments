# 3. Reading from and writing to csv files using lists and dictionaries. 
# You are provided with sample.csv file and implement the following.
# Read_fieldnames() : It should return the field names (column names) for the given csv file
# Read_csv_as_list_dict():  Returns a list of dictionaries where each item in the list  corresponds to a row in the CSV file.  
#                         The dictionaries in the list map the field names to the field values for that row.
# Write_csv_as_list_dict(): to this method pass the field names we get from first method, list of dictionaries which we get from second method and new file name as the third parameter. 
#                         Code should create new csv file with given file name, field names and write the data supplied.

from collections import OrderedDict
import csv


def read_fieldnames(csv_reader):
    return list(csv_reader)[0]


def read_csv_as_list_dict(csv_reader, fieldnames):
    row_list = list()
    
    #skip row 1 (fieldname) and loop
    for row in list(csv_reader)[1:]:
        temp_dict = OrderedDict()
        for value, fieldname in zip(row, fieldnames):
            temp_dict.update({fieldname : value})
        
        # row_list.append(temp_dict)
        print(temp_dict)

    return row_list


def write_csv_as_list_dict(fieldnames, row_list):
    with open("new.csv", "w") as new_csvfile:
        dw = csv.DictWriter(new_csvfile, delimiter=',', fieldnames=fieldnames)
        dw.writeheader()

        print(row_list)
        # for row in row_list:
        #     print(row)
            # dw.writerows(row)

        print("\n New csv file created")


def main():
    with open("../question_n_source/sample.csv") as csv_file:
        csv_reader = csv.reader(csv_file)

        fieldnames = read_fieldnames(csv_reader)

        #move cursor to the begining
        csv_file.seek(0)

        row_list = read_csv_as_list_dict(csv_reader, fieldnames)

        # print(fieldnames)
        # print("\n\n")
        # print(row_list)

        write_csv_as_list_dict(fieldnames, row_list)





if __name__ == "__main__":
    main()