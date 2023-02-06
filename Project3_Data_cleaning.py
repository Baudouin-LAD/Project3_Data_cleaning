#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 09:49:43 2023

@author: Baudouin
"""

"""Project 3 Data cleaning """


import pandas as pd
import numpy as np
import re
from sqlalchemy import create_engine 
import pymysql.cursors
import os
import getpass
data = pd.read_excel('/Users/Baudouin/Ironhack/Project3_Data_cleaning/data.xlsx')
data = data.reset_index(level=0)
#linking to SQL database
pw = os.getenv('IronHack')
pw = getpass.getpass()
connection_string = 'mysql+pymysql://root:' + pw + '@localhost:3306/'
engine = create_engine(connection_string)
with engine.connect() as conn:
    conn.execute(f"CREATE DATABASE IF NOT EXISTS data_cleaning")
data.to_sql('entrepreneurial_fit',engine, 'data_cleaning', if_exists='replace', index=False)

# formatting columns naming
data.columns = (data.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.lower()
                .str.replace(' ', '_', regex=True)
                .str.replace('-', '_', regex=True))

#identifying rows with too many empty values
data_slice = data.loc[:,'perseverance':'good_physical_health']
data_slice_t_f = data_slice.isnull()
nan_rows = [i for i in range(len(data_slice_t_f.index)) if data_slice_t_f.iloc[i].sum() >1]
data = data.drop(index=nan_rows)
  
#replacing empty cells in reasons for lack
data['reasons_for_lack'].fillna('No Reason', inplace = True)  
    
#replacing missing ages with mean age
data['age'].fillna(round(data['age'].mean()),inplace=True)

#replacing nan cell in mentaldissorder columns as 'No' benefit of the doubt
data['mental_disorder'].fillna('No',inplace=True)

reasons=", ".join(data['reasons_for_lack'])
reasons_list = list(set([s[1:] if s[0] == ' ' else s for s in reasons.split(',')]))

"""
def encodereason(i):
    isreason= lambda i,j : 1 if str(i) in str(j) else 0
    data[str(i)]=data['reasons_for_lack'].apply(lambda x: isreason(i, x))
    return
for i in reasons_list:
    encodereason(i)"""

#get a list of unique values per column
values = []
def standard(d) :
    for c in range(len(d.columns)):
     if (d.dtypes[c] == np.float64 or d.dtypes[c] == np.int64):
         pass
     else:
         list1 = list(set([s[1:] if s[0] == ' ' else s for s in (", ".join(d.iloc[:, c].values)).split(',')]))
         values.append(list1)
standard(data)
#get columns index for the non numeric columns
cols= [i for i in range(len(data.columns)) if not (data.dtypes[i] == np.float64 or data.dtypes[i] == np.int64)]
 #create a list of tuples (col index, list of unique values in said column)           
array_to_change = list(zip(cols,values))      
            
#standardisation of the columns content
data['gender'] = data['gender'].str.lower()
data['influenced']= data['influenced'].replace('unkown','No', regex=True)
data['key_traits'] = data['key_traits'].replace('Rrresilience','Resilience', regex=True)
data['key_traits'] = data['key_traits'].str.lower()

data = data.replace({'target_individual_project_' : {'Yes' : 'True', 'No' : 'False'},
                     'city' : { 'Yes' : 'True', 'No' : 'False'},
                     'influenced' : { 'Yes' : 'True', 'No' : 'False'},
                     'mental_disorder' : { 'Yes' : 'True', 'No' : 'False'},
                     'gender' : {'male' : 'False', 'female' : 'True'}})  
   
#renaming stupid columns
"""data.columns.values[23] = 'wants_to_relocate'
data.columns.values[25] = 'just_not_interested'"""
sql = """
Select *
from data_cleaning.entrepreneurial_fit;"""
new_df = pd.read_sql_query(sql, engine)





















