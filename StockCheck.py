#! Python 3
'''
The purpouse of this program is to read from a daily CSV report of avaiable stock
and return randomly selected parts for counting.
'''
# Fieldnames = "[0]Store","[1]Part","[2]Description","[3]Lot Ref","[4]Lot Line","[5]Lot Qty","[6]UOM","[7]Bin Qty","[8]Part Cost"

import csv
import random
import pandas as pd

# Import and read from the .CSV parts file to extract data
csvfile = pd.read_csv(r'C:\Users\PC\Desktop\DELTA\PARTS.csv')
print(csvfile.sample())

# Pass in the list of parts and return randomly selected one's


def chosen_at_random():

    answer = int(input('How many parts to be counted\n'))
    list_of_random_item = random.choice(line)
    return list_of_random_item


print(chosen_at_random())
