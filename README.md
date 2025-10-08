

# Avenis-Advance-Programming-PA3

---

# PROBLEM 1

For this project, the pandas library is imported to use its methods for manipulating DataFrames.  

```python
import pandas as pd
````

Import the pandas library.

---

### Code for part A

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

---

### Code for part B

Finally, it prints the two results to display them in the console.

```python
# Display both results
print("First five rows:")
print(first_five)
print("\nLast five rows:")
print(last_five)
```

**Output:**

```
First five rows:
             Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb
0        Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
1    Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
2       Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
3   Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
4  Hornet Sportabout 18.7   8  360.0  175  3.15  3.440  17.02   0   0     3     2

Last five rows:
             Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb
27     Porsche 914-2 26.0    4  120.3   91  4.43  2.140  16.70   0   1     5     2
28      Lotus Europa 30.4    4   95.1  113  3.77  1.513  16.90   1   1     5     2
29    Ford Pantera L 15.8    8  351.0  264  4.22  3.170  14.50   0   1     5     4
30      Ferrari Dino 19.7    6  145.0  175  3.62  2.770  15.50   0   1     5     6
31     Maserati Bora 15.0    8  301.0  335  3.54  3.570  14.60   0   1     5     8
```

---

# PROBLEM 2

---

### Code for part A

Loads the same `cars.csv` file into a DataFrame named **cars**.

```python
# Load the CSV file
cars = pd.read_csv('cars.csv')
```

Selects the first five rows with **odd-numbered columns** (1st, 3rd, 5th, 7th...).

```python
# Select the first five rows with odd-numbered columns
odd_columns = cars.iloc[:5, ::2]

# Display the result
odd_columns
```

**Output:**

```
             Model  cyl   hp     wt  vs  gear
0        Mazda RX4    6  110  2.620   0     4
1    Mazda RX4 Wag    6  110  2.875   0     4
2       Datsun 710    4   93  2.320   1     4
3   Hornet 4 Drive    6  110  3.215   1     3
4  Hornet Sportabout  8  175  3.440   0     3
```

---

### Code for part B

Extracts the row containing the **Model “Mazda RX4”**.

```python
# Selects the row where the Model is 'Mazda RX4'
Mazda_RX4_row = cars[cars['Model'] == 'Mazda RX4']

# Display the row
Mazda_RX4_row
```

**Output:**

```
      Model      mpg  cyl  disp   hp  drat    wt   qsec  vs  am  gear  carb
0  Mazda RX4   21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
```

---

### Code for part C

Finds how many **cylinders** the car model `"Camaro Z28"` has.

```python
# Selects the 'cyl' column for the model 'Camaro Z28'
cylinders = cars[cars['Model'] == 'Camaro Z28']

# Display the result
cylinders
```

**Output:**

```
       Model      mpg  cyl  disp   hp  drat    wt   qsec  vs  am  gear  carb
23  Camaro Z28  13.3    8  350.0  245  3.73  3.840  15.41   0   0     3     4
```

---

### Code for part D

Determines the **number of cylinders** (`cyl`) and **gear type** (`gear`) for specific models:
`Mazda RX4 Wag`, `Ford Pantera L`, and `Honda Civic`.

```python
# Select specific models
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']

# Filter and select relevant columns
subset = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]

# Display the result
subset
```

**Output:**

```
            Model   cyl  gear
1     Mazda RX4 Wag    6     4
29    Ford Pantera L   8     5
18        Honda Civic  4     4
```
