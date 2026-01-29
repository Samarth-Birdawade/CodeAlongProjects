import pandas as pd
import numpy as np
from numpy import *
import random
from time import sleep

# Using this function allows output to be displayed slowly making it readable rather than scrolling to the top to start reading
def slow_execution():
    return sleep(1)     # Change the sleep value to 0 to instantly execute everything

# Using NumPy functions (linspace, zeros, ones)
print("Linspace (0 to 50):")
print(np.linspace(0, 50, 5)) 

print("\nZeros (Shape 2x2):")
print(np.zeros((2, 2)))

print("\nOnes (Shape 2x2):")
print(np.ones((2, 2)))

slow_execution()

# Reading data using Pandas
df_employees = pd.read_csv('employees.csv')

print("--- Employees Table ---")
print(df_employees)

slow_execution()

# Adding custom index
df_employees.index = [1, 2, 3, 4]

print("\n1st Row of the Employees Table:")
print(df_employees.iloc[0])

slow_execution()

# Change the first Name from the df
df_employees.iloc[0, 0] = "Alex"

print("\n1st Row & Col of the Employees Table:")
print(df_employees.iloc[0,0])

slow_execution()

# Adding a salary column
df_employees['salary'] = np.arange(100000, 500000, 100000)

# Calculating Min, Max, and Mean Salary
min_salary = df_employees['salary'].min()
max_salary = df_employees['salary'].max()
avg_salary = df_employees['salary'].mean()

print(f"\nSalary Stats:\n\tMin: {min_salary}\n\tMax: {max_salary}\n\tMean: {avg_salary}")

slow_execution()

# Printing Boolean using basic numpy ops
all_sal_under_5 = all(df_employees['salary'] < 500000)
print(f"\nIs everyones salary under 5 lakhs: {all_sal_under_5}")

# Using Lambda to convert boolean to "Yes" or "No"
any_sal_above_5 = lambda df: "Yes" if (df['salary'] > 500000).any() else "No"
print(f"Does anyone have Salary Above 5 lakhs: {any_sal_above_5(df_employees)}")

slow_execution()

# Filtering the dataframe based on a condition
sal_between_2_and_4 =  df_employees[df_employees['salary'].between(200000, 400000)]
print("Employees with salaries between 2 lakhs and 4 lakhs")
print(sal_between_2_and_4)

pd.set_option('display.precision', 1)
print(f"\n{df_employees.describe()}")

slow_execution()

# For Transpose
print(f"\nTranspose of the table:\n{df_employees.T}")

slow_execution()

# Sorting
print(f"\nSorted table:\n{df_employees.sort_values(by='first_name', ascending=False)}")

slow_execution()

# Adding the location column using a series
df_employees['location'] = pd.Series(["Pune", "Delhi", "New Jersey","Pune"], name = "Location")
print("\nTable after adding Location column:")
print(df_employees)

slow_execution()

print("\nString op on a df column")
print(df_employees["location"].str.upper())

slow_execution()

# Removing the location column
df_employees = df_employees.drop(columns=['location'])

# Removing random number of records from the df
rand_no_of_record_to_remove = random.randint(0, len(df_employees))
df_employees = df_employees.iloc[rand_no_of_record_to_remove:]

print("\nTable after removing Location column along with a few records:")
print(df_employees)