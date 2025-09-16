{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "01ed9ca2-05c8-43e4-bae0-d369eccb36ad",
   "metadata": {},
   "source": [
    "PROBLEM 2: Save your file as Surname_Pandas-P2.py\n",
    "Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and\n",
    "indexing operations.\n",
    "a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.\n",
    "b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.\n",
    "c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?\n",
    "d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4\n",
    "Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a9a510b5-3ccf-41df-8b77-7f3d7dde23af",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "21f458f9-4f1a-4a5c-8b21-4948e85aa233",
   "metadata": {},
   "outputs": [],
   "source": [
    "# to load the csv file\n",
    "cars = pd.read_csv('cars.csv')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8b9859b8-e5f7-409c-a5cf-07b78ff80b0d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# indexes positions for odd numbers\n",
    "odd_columns = cars.iloc[:5, ::2]\n",
    "\n",
    "# display odd-number positions\n",
    "print(odd_columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b95237b-5e36-4c2e-bc32-3e9255402871",
   "metadata": {},
   "outputs": [],
   "source": [
    "# takes rows that contain the Mazda RX4 data in the Model label \n",
    "Mazda_RX4_row = cars[cars['Model'] == 'Mazda RX4']\n",
    "\n",
    "# displays rows that contain Mazda RX4 Model\n",
    "print(Mazda_RX4_row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86a224e8-3bcd-4242-bbea-4ca35f67df01",
   "metadata": {},
   "outputs": [],
   "source": [
    "# selects the cyl label column with model of Camaro Z28\n",
    "cylinders = cars[cars['Model'] == 'Mazda RX4']\n",
    "\n",
    "# displays how many cars have Camaro Z28 model\n",
    "print(cylinders.values[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ccb5134-1536-41ad-9ca2-aa56a0f76ab6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# \n",
    "models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']\n",
    "#\n",
    "subset = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]\n",
    "\n",
    "#\n",
    "print(subset)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
