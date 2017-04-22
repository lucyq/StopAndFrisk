import pandas as pd
import numpy as npy
import os

from field_conversions import *

# outputs a csv file (one per year) with the following columns:
#   date                    (FIOS_DATE_CORRECTED)
#   sex                     (SEX)
#   race                    (RACE_DESC)
#   age                     (AGE_AT_FIO_CORRECTED)
#   city                    (CITY)
#   suspicion               (BASIS)
#   action                  (FIOFS_TYPE)


# set up inputs
out_dir = '//Users//Jenn//Documents//Hack4Democracy//'
in_file_1 = '//Users//Jenn//Documents//Hack4Democracy//Boston_Police_Department_FIO.csv'

# read data
df1 = pd.read_csv(in_file_1, usecols=['FIO_DATE_CORRECTED', 'SEX', 'RACE_DESC', 'AGE_AT_FIO_CORRECTED', 'CITY', \
                                      'BASIS', 'FIOFS_TYPE'])

df1['datestamp'] = pd.to_datetime(df1['FIO_DATE_CORRECTED'])  # create a datetime field

# map the fields read in to the desired output fields
df1['date'] = df1['datestamp'].apply(lambda x: str(x).split(' ')[0])  # put date in format YYYY-MM-DD

df1['sex'] = df1['SEX'].apply(lambda x: x.lower())  # make lower case
df1 = df1[df1['SEX'] != 'UNKOWN'] # drop all rows with sex = unknown

df1['race'] = df1['RACE_DESC'].apply(convert_race_function)
#df1 = df1[df1['race'] != 'NO DATA ENTERED'] # drop all rows with 'NO DATA ENTERED', 'UNKNOWN'
#df1 = df1[df1['race'] != 'UNKOWN']
df1 = df1[df1['race'] != 'delete']

df1['age'] = df1['AGE_AT_FIO_CORRECTED']
df1 = df1[df1['age'] > 0] # drop all rows with < 1 or > 100
df1 = df1[df1['age'] < 100]

df1['city'] = df1['CITY']
df1 = df1[df1['CITY'] != 'NO DATA ENTERED'] # drop all rows with 'NO DATA ENTERED', 'OTHER'
df1 = df1[df1['CITY'] != 'OTHER']

df1['suspicion'] = df1['BASIS'].apply(convert_basis_function)
df1 = df1[df1['suspicion'] != 'delete']

df1['action'] = df1['FIOFS_TYPE'] .apply(convert_fiofs_type_function)
df1 = df1[df1['action'] != 'delete']
# drop all rows with 'PI', 'PIO', 'PIOS', 'PO', 'PIOFS', 'PIF', 'PIOF', 'P', 'PIS', 'PF', 'POF'

 # create the mapping of the FIOFS_TYPE field (stopped or observed)
 # create the mapping of the basis field (Reasonable suspicion, probable cause, consented to search)

df1['YEAR'] = df1.apply(lambda x: x['FIO_DATE_CORRECTED'].split(' ')[0].split('/')[2], axis=1)
for yr in df1['YEAR'].unique():
    out_df = df1.loc[df1['YEAR'] == yr]  # get only the rows for that year

    # sort date (increasing)
    out_df = out_df.sort(columns='datestamp', ascending=True)

    # drop any rows with nans for any of the columns (shouldnt be possible - ignore this)

    # write output file
    out_file = 'data' + yr + '.csv'
    out_df.to_csv(os.path.join(out_dir, out_file), columns=['date', 'sex', 'race', 'age', 'city', 'suspicion', 'action'], index=False)
