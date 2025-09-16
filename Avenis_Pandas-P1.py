{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7ef8ea9b-f9e8-42bc-b5bf-2944c7a02686",
   "metadata": {},
   "source": [
    "PROBLEM 1\n",
    "\n",
    "Using knowledge obtained from the experiment and demonstrations:\n",
    "\n",
    "a. Load the corresponding .csv file into a data frame named cars using pandas.\n",
    "b. Display the first five and last five rows of the resulting cars."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2be2b48e-3673-4381-8101-aa0ba84a271d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# (a) Load the CSV file into a DataFrame\n",
    "cars = pd.read_csv(\"cars.csv\")\n",
    "\n",
    "# (b) Target the first five and last five rows\n",
    "first_five = cars.head()\n",
    "last_five = cars.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1d41a214-f5ab-4737-b50f-966d1a2b3fae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First five rows:\n",
      "               Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
      "0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4   \n",
      "1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   \n",
      "2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4   \n",
      "3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3   \n",
      "4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3   \n",
      "\n",
      "   carb  \n",
      "0     4  \n",
      "1     4  \n",
      "2     1  \n",
      "3     1  \n",
      "4     2  \n",
      "\n",
      "Last five rows:\n",
      "             Model   mpg  cyl   disp   hp  drat     wt  qsec  vs  am  gear  \\\n",
      "27    Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.9   1   1     5   \n",
      "28  Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.5   0   1     5   \n",
      "29    Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.5   0   1     5   \n",
      "30   Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.6   0   1     5   \n",
      "31      Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.6   1   1     4   \n",
      "\n",
      "    carb  \n",
      "27     2  \n",
      "28     4  \n",
      "29     6  \n",
      "30     8  \n",
      "31     2  \n"
     ]
    }
   ],
   "source": [
    "# Display both results\n",
    "print(\"First five rows:\")\n",
    "print(first_five)\n",
    "print(\"\\nLast five rows:\")\n",
    "print(last_five)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a1dc2dc-4ade-4f0f-952e-7d74f5e96bef",
   "metadata": {},
   "outputs": [],
   "source": []
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
