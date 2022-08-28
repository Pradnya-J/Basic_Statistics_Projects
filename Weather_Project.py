import pandas as pd
import numpy as np
data = pd.read_csv(r"C:\Users\Pramod\Downloads\1. Weather Data.csv") #r written to remove the unicode error
# data.head() shows the th first N no. of rows in the data (by default 5, we can choose our own rows)
# print(data)
# a python shell. Always print() function will be required.
# print(data.shape)
# 8784*8 (rows, columns)
# print(data.index)
# RangeIndex(start=0, stop=8784, step=1)
# print(data.columns)  shows names of all columns
# Index(['Date/Time', 'Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h',
# 'Visibility_km', 'Press_kPa', 'Weather'],   dtype='object')
#print(data.dtypes)
# print(data['Weather'].unique)

 # Question 1 : Find all unique wind speeds in data
print(data.head(2)) # just df.head() function does not work in pycharm becoz it is not
print("names of all columns : ",data.columns)
print(data['Wind Speed_km/h'].nunique())
print("All unique wind speeds in data : ", data['Wind Speed_km/h'].unique())

# Q2 find the exact no of times weather is exactly clear
#M1
print(data.Weather.value_counts())
#M2
print(data[data.Weather == 'Clear'])
#M3
print(data.groupby('Weather').get_group('Clear'))

# Q3 Find the no. of times when the wind speed is exactly 4km/hr
print(data[data['Wind Speed_km/h'] == 4])

#4 Find out the null values in data
print(data.isnull().sum())
print(data.notnull().sum())

# Q5 Rename weather to weather conditions
print(data.rename( columns = { 'Weather' : "Weather Conditions"}, inplace = True)) #inplace= True changes the name permanently
print(data.head(1))

# Q6 What is mean visibility?
print("mean of visibility : " , data.Visibility_km.mean())

# q7 What is the stndard deviation of pressure column
print("standard deviatiob of pressure : ", data.Press_kPa.std())

# Q8 variance of relative humidity
print("variance of relative humidity : ", data['Rel Hum_%'].var())

# Q9 All instances when snow was recorded
print(data['Weather Conditions'].value_counts()) #M1
print(data[data['Weather Conditions'] == 'Snow']) #M2
print(data[data['Weather Conditions'].str.contains('Snow')]) #gives all rows that contain snow word

# Q10 all instances when wind speed is above 24 and visibility is 25
print(data[((data['Wind Speed_km/h'] > 24)) & ((data['Visibility_km'] == 25))])

# Q11 mean value of each column against each weather condition
print(data.groupby('Weather Conditions').mean())

# Q12  Minimum & Max value of each column against each ' weather conditions'
print(data.groupby('Weather Conditions').min())
print(data.groupby('Weather Conditions').max())

# Q13 Show all the records where weather conditions is fog
print(data[data['Weather Conditions'] == 'Fog'])

# Q14 weather is clear OR  visibility is above 40
print("")
print(data[((data['Weather Conditions'] == 'Clear')) | (data['Visibility_km'] > 40)])

# Q15 (A) Weather is clear and relative humidity is greater than 50
# (B) Visibility is above 40
print(data[((data['Weather Conditions'] == 'Clear')) & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40) ])

