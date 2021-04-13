# Sargon Odicho
# 04/08/2021
# CSV-Combiner PMG coding challenge

import sys
import os
import unittest
import pandas as pd
    
def get_name(path):
    # find the last forward slash and return the rest of the string (filename)
    name_index = path.rfind('/')
    filename = path[name_index+1:]

    return filename

def combine(df, csv_files):
    # looping through the the rest of the csv files
    for i in range(1, len(csv_files)):
        # creating new dataframe
        df1 = pd.read_csv(csv_files[i])
        # adding in filename and correctly naming it using get_name
        df1['filename'] = get_name(csv_files[i])
        # concatenate the new df to the original and the same for the rest of files
        df = pd.concat([df,df1])
    return df

def main():
    csv_files = []
    # looping through files that were given as arguments on command line 
    for i in range(1,len(sys.argv)):
        # if path valid, append
        if os.path.isfile(sys.argv[i]):
            if sys.argv[i][-4:] == '.csv':
                csv_files.append(sys.argv[i])

    # this will be the base of the csv and the rest will combine to this
    # using pandas library to read csv and convert to dataframe
    df = pd.read_csv(csv_files[0])

    # adding in the filename column for the it was retrieved from
    df['filename'] = get_name(csv_files[0])

    # if more files, call combine
    if len(csv_files) > 1:
        # assign to original df
        df = combine(df, csv_files)

    # setting index to first column e.g. email_hash
    df = df.set_index(df.columns[0])


    # new_csv will convert dataframe to csv and save new file as 'combined.csv'
    # into same directory as script
    new_csv = df.to_csv()
    print(new_csv)

if __name__ == "__main__":
    main()