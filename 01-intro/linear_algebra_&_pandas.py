import numpy as np
import pandas as pd

# scalar operations
u = np.array([2, 4, 5, 6])
2 * u
# array([ 4,  8, 10, 12])

v = np.array([1, 0, 0, 2])
u + v
# array([3, 4, 5, 8])


# Multiplication
u * v
# array([ 2,  0,  0, 12])

# dot product
# u·v = 2·1 + 4·0 + 5·0 + 6·2 = 2 + 12 = 14
def vector_vector_multiplication(u, v):
    assert u.shape[0] == v.shape[0]
    
    n = u.shape[0]
    
    result = 0.0

    for i in range(n):
        result = result + u[i] * v[i]
    
    return result

# matrix-vector multiplication
def matrix_vector_multiplication(U, v):
    assert U.shape[1] == v.shape[0]
    
    num_rows = U.shape[0]
    
    result = np.zeros(num_rows)
    
    for i in range(num_rows):
        result[i] = vector_vector_multiplication(U[i], v)
    
    return result

# inverse of ma matrix

Vs = np.array([[1. , 1. , 2. ],
       [0. , 0.5, 1. ],
       [0. , 2. , 1. ]])

Vs_inv = np.linalg.inv(Vs)


# refresher on pandas

data = [
    ['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],
    ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],
    ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
    ['GMC', 'Acadia',  2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],
    ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],
]

columns = [
    'Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
    'Transmission Type', 'Vehicle_Style', 'MSRP'
]

# turn into a complete dataframe


df = pd.DataFrame(data, columns = columns)
df

# create with dictionaries
data = [
    {
        "Make": "Nissan",
        "Model": "Stanza",
        "Year": 1991,
        "Engine HP": 138.0,
        "Engine Cylinders": 4,
        "Transmission Type": "MANUAL",
        "Vehicle_Style": "sedan",
        "MSRP": 2000
    },
    {
        "Make": "Hyundai",
        "Model": "Sonata",
        "Year": 2017,
        "Engine HP": None,
        "Engine Cylinders": 4,
        "Transmission Type": "AUTOMATIC",
        "Vehicle_Style": "Sedan",
        "MSRP": 27150
    },
    # ...
]
# no need to provide column names

# peeking at the column:
df.head(n=2)


# series
# column == pandas series


# access a particular column 
df['Engine HP']

# access multiple columns
df[['Make', 'Model', 'MSRP']]

# add a new column 
df['id'] = [1, 2, 3, 4, 5]

# delete a column
del df['id']


# Index (rows)

df.index

# access elements by their index
df.loc[1]
# row indexed by 1

# change index to something else
df.index = ['a', 'b', 'c', 'd', 'e']

# regardless of how the dataframe is indexed, we can access them by positional index
df.iloc[[1, 2, 4]]

# reset index to the numbered index
# keeps the previous index by creating a new column called index with the old values
# if we want to drop the old values, we can use the parameter drop = True
df = df.reset_index(drop=True)


# Element-wise operations

# all the column values gets multiplied by that number
df['Engine HP'] * 2

# comparison
df['Year'] >= 2015

# Filtering
# filter dataframe so that only the columns/rows that satisfy that condition is outputed to the new dataframe

df[(df['Make'] == 'Nissan') & (df['Year'] >= 2015) ]


# String operations
# (unique to pandas)

# case sensitive
df['Vehicle_Style'].str.lower()

# replacement, parameter = (old, new)
df['Vehicle_Style'].str.replace(' ', '_')

# NOTE: thse operations do not modify (overwrite) the series, it just returns a new series
# to apply the modifications
df['Vehicle_Style'] = df['Vehicle_Style'].str.replace(' ', '_').str.lower()


# summarizing operations in numPy
# summarizing columns
df.MSRP.mean()
df.MSRP.max()

# describe: reports all the useful statistics at once
df.MSRP.describe().round(2)


# cateogorial variable operations:

# unique values there are:
df.Make.nunique()
# returns the number of unqiue values in a column
df.Make.unique()
# returns the column of unique values


# missing values
# detect for each column: whether it contains null values
df.isnull().sum()

df.groupby('Transmission Type').MSRP.max()

# retrieve the specific column values
df.MSRP.values

# convert a pandas dataframe back into a list of dictionaries
df.to_dict(orient='records')
[{'Make': 'Nissan',
  'Model': 'Stanza',
  'Year': 1991,
  'Engine HP': 138.0,
  'Engine Cylinders': 4,
  'Transmission Type': 'MANUAL',
  'Vehicle_Style': 'sedan',
  'MSRP': 2000},
 # ...
 ]
