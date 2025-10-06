
---

# Avenis-Advance-Programming-PA3

# PROBLEM 1: 

For this project, the pandas library is imported to use its methods for manipulating DataFrames.  
```python
import pandas as pd
````

Import the pandas library.

**Code for part A:**

This code loads the `cars.csv` file into a DataFrame named **cars** using pandas.

```python
# Load the CSV file into a DataFrame
cars = pd.read_csv("cars.csv")
```

It then retrieves the first five and last five rows of the DataFrame and stores them in two variables: **first_five** and **last_five**.

```python
# Target the first five and last five rows
first_five = cars.head()
last_five = cars.tail()
```

**Code for part B:**
Finally, it prints the two results to display them in the console.

```python
# Display both results
print("First five rows:")
print(first_five)
print("\nLast five rows:")
print(last_five)
```

**-------------------------------------------------------------------------------**

# PROBLEM 2

**Code for part A:**

Loads the same `cars.csv` file into a DataFrame named **cars**.
```python
# Load the CSV file
cars = pd.read_csv('cars.csv')
```

Selects the first five rows with **odd-numbered columns** (1st, 3rd, 5th, 7th...).
Using  the `iloc` indexer:
* `:5` takes the first five rows.
* `::2` takes every second column (i.e., 1st, 3rd, 5th...).

```python
# Select the first five rows with odd-numbered columns
odd_columns = cars.iloc[:5, ::2]

# Display the result
odd_columns
```
**-------------------------------------------------------------------------------**

**Code for part B:**

Extracts the row containing the **Model “Mazda RX4”**.
Checks which rows have `"Mazda RX4"` in the Model column and displays that entire row.
```python
# Selects the row where the Model is 'Mazda RX4'
Mazda_RX4_row = cars[cars['Model'] == 'Mazda RX4']

# Display the row
Mazda_RX4_row
```

**-------------------------------------------------------------------------------**

**Code for part C:**

Finds how many **cylinders** the car model `"Camaro Z28"` has.
Filters the DataFrame to only include `"Camaro Z28"` and shows its details, including the number of cylinders.
```python
# Selects the 'cyl' column for the model 'Camaro Z28'
cylinders = cars[cars['Model'] == 'Camaro Z28']

# Display the result
cylinders
```

**-------------------------------------------------------------------------------**

**Code for part D:**

Determines the **number of cylinders** (`cyl`) and **gear type** (`gear`) for specific models:
`Mazda RX4 Wag`, `Ford Pantera L`, and `Honda Civic`.
Creates a list of specific models, checks if each row’s Model is in that list, and displays the Model, Cylinders, and Gear Type.
```python
# Select specific models
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']

# Filter and select relevant columns
subset = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]

# Display the result
subset
```
