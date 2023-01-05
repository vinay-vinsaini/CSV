# Sample code to convert CSV files to
#import the below packages

import pandas as pd
import os
import shutils

# reading the csv file
cvsDataframe = pd.read_csv('/Users/vinsaini/Downloads/vinsaini_P.csv')
print(cvsDataframe )
# creating an output excel file and setting up its location
resultExcelFile = pd.ExcelWriter('/Users/vinsaini/Downloads/vinsaini_P.xlsx')
print(' Your XLS file will be stored here : ', os.getcwd())
# converting the csv file to an excel file
cvsDataframe.to_excel(resultExcelFile, index=False)
# saving the excel file
resultExcelFile.save()
