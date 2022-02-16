# Creating dataframe:
import pandas as pd
df = pd.read_csv("weather_data.csv")   #read weather.csv data
print(df)

 
  
#list of tuples
weather_data = [('1/1/2017', 32, 6, 'Rain'),
                ('1/2/2017', 35, 7, 'Sunny'),
                ('1/3/2017', 28, 2, 'Snow'),
                ('1/4/2017', 24, 7, 'Snow'),
                ('1/5/2017', 32, 4, 'Rain'),
                ('1/6/2017', 31, 2, 'Sunny')
               ]
df = pd.DataFrame(weather_data, columns=['day', 'temperature', 'windspeed', 'event'])
print(df)
 
  
  
#get dimentions of the table
df.shape   #total number of rows and columns			#(6,4)



#if you want to see initial some rows then use head command (default 5 rows)
print(df.head())
 
  
  
#if you want to see last few rows then use tail command (default last 5 rows will print)
print(df.tail())
 
  
  
#slicing
print(df[2:5])
 
  
  
print(df.columns)   #print columns in a table



#get 2 or more columns
print(df[['day', 'event']])
 
  
#print max,min.describe temperature
print(df['temperature'].max())
print(df['temperature'].min())
print(df['temperature'].describe())


# Read and write CSV files 

import pandas as pd
df = pd.read_csv('weather_data.csv')
print(df)

# GROUP-BY
import pandas as pd
df = pd.read_csv('weather_data_cities.csv')
print(df)  #weather by cities



# concatenate Data Frames
import pandas as pd
india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
print(india_weather)
 
  
  
df = pd.concat([india_weather, us_weather],axis=1)
print(df)
 

# Merge DataFrames 
temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore", 'hyderabad'],
    "temperature": [32,45,30,40]})
print(temperature_df)
 

# Numerical Indexing (.loc vs iloc)

import pandas as pd
import numpy as np
df = pd.DataFrame([1,2,3,4,5,6,7,8,9,19], index=[49,48,47,46,45, 1, 2, 3, 4, 5])
print(s.iloc[:2])
 

