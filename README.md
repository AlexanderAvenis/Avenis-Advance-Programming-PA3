# Avenis-Advance-Programming-PA3

# PROBLEM 1: 
**Instruction:** 
Save your file as Surname_Pandas-P1.py
Using knowledge obtained from the experiment and demonstrations:

a. Load the corresponding .csv file into a data frame named cars using pandas
b. Display the first five and last five rows of the resulting cars

**Code:**
```python
import pandas as pd

# (a) Load the CSV file into a DataFrame
cars = pd.read_csv("cars.csv")

# (b) Target the first five and last five rows
first_five = cars.head()
last_five = cars.tail()

# Display both results
print("First five rows:")
print(first_five)
print("\nLast five rows:")
print(last_five)
```
1. import pandas as pd imports the pandas library.
   
2. cars = pd.read_csv("cars.csv") → Load the CSV file into a table

3. cars.head() → Get first 5 rows.

4. cars.tail() → Get last 5 rows.

5. print("\nLast five rows:") and print(last_five) show the results

# PROBLEM 2
**Instruction:** 
Save your file as Surname_Pandas-P2.py Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations. 

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars. 
b. Display the row that contains the ‘Model’ of ‘Mazda RX4’. 
c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? 
d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

**Code:**
```python
import pandas as pd

# to load the csv file
cars = pd.read_csv('cars.csv')

# indexes positions for odd numbers
odd_columns = cars.iloc[:5, ::2]

# display odd-number positions
print(odd_columns)
```
1. :5 → takes the first 5 rows.

2. ::2 → takes every 2nd column (1st, 3rd, 5th…).

3. Shows the first 5 rows with odd-numbered columns.

```python
# takes rows that contain the Mazda RX4 data in the Model label 
Mazda_RX4_row = cars[cars['Model'] == 'Mazda RX4']

# displays rows that contain Mazda RX4 Model
print(Mazda_RX4_row)
```
1. cars['Model'] == 'Mazda RX4' checks which rows have the Model "Mazda RX4".

2. Only rows with that model are selected.

3. Prints the full row for Mazda RX4.

```python
# selects the cyl label column with model of Camaro Z28
cylinders = cars[cars['Model'] == 'Mazda RX4']

# displays how many cars have Camaro Z28 model
print(cylinders.values[0])
```
1. This code is mistyped — it should be "Camaro Z28", not "Mazda RX4".

2. The filter checks which rows match the Model.

3. .values[0] shows the first row’s values as an array.

4. If fixed to "Camaro Z28", it returns the number of cylinders for Camaro Z28.

```python
# takes the required models
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
# check for if Model is one of the given list
subset = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]

# displays how many cylinders and what gear type 
print(subset)
```
1. Makes a list of 3 specific car models.

2. .isin(models) checks if each row’s Model is in that list.

3. Selects only the Model, cyl, and gear columns.

4. Prints a table showing cylinders and gear type for those cars.

