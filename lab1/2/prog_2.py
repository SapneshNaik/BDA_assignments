# 2. Read the file ‘state-place.txt’ which is copy pasted from wiki pages. 
# It starts with state name with constant word [edit] followed by place name with or without college/ university name. 
# Parse the text file and create a csv file with two columns. First will be state name and second is the place name. 
# Entries in the csv file will be data extracted from text file.

import re
import csv
from collections import OrderedDict
from itertools import islice, cycle

#shift dict values left by 1 position
def shift_dict(dct, shift):
    shift %= len(dct)
    return OrderedDict(
        (k, v)
        for k, v in zip(dct.keys(), islice(cycle(dct.values()), shift, None))
    )

#get an ordered states dict ( ending with constant [edit] or [Edit])
def get_states(input_file):
    pattern1 = re.compile(".+ \[[eE]dit\]")
    #maintain dictinary order
    states = OrderedDict()

    #Build a dictionary of states and their respective line number occurances
    for num, line in enumerate(input_file, 1):
        if pattern1.match(line):
            # print(line)
            states.update({line.strip('\n'): (num)})
    return states


def main():

    with open('../question_n_source/state-place.txt', encoding="utf8", errors='ignore') as input_file:

        states = get_states(input_file)

        #shift states dict values by 1 position so that each
        states_e = shift_dict(states,1)

        input_file.seek(0)
        with open('prog2_output.csv', mode='w') as csv_file:

            lines = [line.rstrip("\n") for line in input_file]
            fieldnames = ['state_name', 'place_name']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for state, end in zip(states.items(), states_e.values()):
                    if (end-1) != 0: 
                        places = lines[state[1]:(end-1)]
                    else:
                        places = lines[state[1]:len(lines)]
                    for place in places:
                        writer.writerow({'state_name': re.sub(r' \[[eE]dit\]', '', state[0]) , 'place_name': re.sub(r'(\[\d+\])?( \(.+)*', '', place)})


    print("Done. Please check prog2_output.csv for result")

if __name__=="__main__":
    main()