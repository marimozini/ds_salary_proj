# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:52:20 2023

@author: marim
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#Salary parsing
#Company name text only
#State field 
#Age of company
#Parsing of job description (python, etc.)

#Salary parsing --------------------------------
#creating new columns hourly and 
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

#removing the -1 on the salary estiamte column
df = df[df['Salary Estimate'] != '-1']
#removing the text field on the salary estimate and K/$
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company name text only -------------------------
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)
# axis = 1: This argument specifies that the lambda function will be applied to each row (along axis 1).
# If it were axis = 0, the function would be applied to each column.

#State field 
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])


