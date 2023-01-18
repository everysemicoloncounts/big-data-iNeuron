1. Load the CSV into a DataFrame:
```
import pandas as pd
df = pd.read_csv('data.csv')

```

2. Apply the pandas dtype property and verify the data type of each in the DataFrame object.
```
# importing pandas package
import pandas as pd

# create a Pandas DataFrame
df = pd.DataFrame({'Col1':[4.1, 23.43], 'Col2':['a', 'w'], 'Col3':[1, 8]})

print("DataFrame:")
print(df)

# apply the dtype attribute
result = df.dtypes // result variable contains the data types of the dataframe object.

print("Output:")
print(result)

```

3. Code #1 : Selecting all the rows from the given dataframe in which ‘Percentage’ is greater than 80 using basic method.
```
# importing pandas
import pandas as pd

record = {

'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
'Age': [21, 19, 20, 18, 17, 21],
'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
'Percentage': [88, 92, 95, 70, 65, 78] }

# create a dataframe
dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])

print("Given Dataframe :\n", dataframe)

# selecting rows based on condition
rslt_df = dataframe[dataframe['Percentage'] > 80]

print('\nResult dataframe :\n', rslt_df)


```

Code #2 : Selecting all the rows from the given dataframe in which ‘Percentage’ is greater than 80 using loc[].
```
# importing pandas
import pandas as pd
  
record = {
  'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
  'Age': [21, 19, 20, 18, 17, 21],
  'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
  'Percentage': [88, 92, 95, 70, 65, 78]}
  
# create a dataframe
dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])
  
print("Given Dataframe :\n", dataframe) 
  
# selecting rows based on condition
rslt_df = dataframe.loc[dataframe['Percentage'] > 80]
  
print('\nResult dataframe :\n', rslt_df)

```

Code #3 : Selecting all the rows from the given dataframe in which ‘Percentage’ is not equal to 95 using loc[].
```
# importing pandas
import pandas as pd
  
record = {
  'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
  'Age': [21, 19, 20, 18, 17, 21],
  'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
  'Percentage': [88, 92, 95, 70, 65, 78]}
  
# create a dataframe
dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])
  
print("Given Dataframe :\n", dataframe) 
  
# selecting rows based on condition
rslt_df = dataframe.loc[dataframe['Percentage'] != 95]
  
print('\nResult dataframe :\n', rslt_df)

```

4. Rename the columns in Dataframe:
Method 1: Using rename() function
One way of renaming the columns in a Pandas Dataframe is by using the rename() function. This method is quite useful when we need to rename some selected columns because we need to specify information only for the columns which are to be renamed.

Example 1: Rename a single column.
```
# Import pandas package
import pandas as pd
  
# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
                            'New Zealand', 'Australia'],
            'odi': ['England', 'India', 'New Zealand',
                            'South Africa', 'Pakistan'],
            't20': ['Pakistan', 'India', 'Australia',
                            'England', 'New Zealand']}
  
# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)
  
# Before renaming the columns
print(rankings_pd)
  
rankings_pd.rename(columns = {'test':'TEST'}, inplace = True)
  
# After renaming the columns
print("\nAfter modifying first column:\n", rankings_pd.columns)

```

Example 2: Rename multiple columns.
```
# Import pandas package
import pandas as pd
   
# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
                            'New Zealand', 'Australia'],
              'odi': ['England', 'India', 'New Zealand',
                            'South Africa', 'Pakistan'],
               't20': ['Pakistan', 'India', 'Australia',
                              'England', 'New Zealand']}
   
# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)
   
# Before renaming the columns
print(rankings_pd.columns)
   
rankings_pd.rename(columns = {'test':'TEST', 'odi':'ODI',
                              't20':'T20'}, inplace = True)
   
# After renaming the columns
print(rankings_pd.columns)

```

Method 2: By assigning a list of new column names
The columns can also be renamed by directly assigning a list containing the new names to the columns attribute of the Dataframe object for which we want to rename the columns. The disadvantage of this method is that we need to provide new names for all the columns even if want to rename only some of the columns. 

Code:
```
# Import pandas package
import pandas as pd
  
# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
                            'New Zealand', 'Australia'],
              'odi': ['England', 'India', 'New Zealand',
                            'South Africa', 'Pakistan'],
               't20': ['Pakistan', 'India', 'Australia',
                              'England', 'New Zealand']}
  
# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)
  
# Before renaming the columns
print(rankings_pd.columns)
  
rankings_pd.columns = ['TEST', 'ODI', 'T-20']
  
# After renaming the columns
print(rankings_pd.columns)

```

Method 3: Rename column names using DataFrame set_axis() function

In this example, we will rename the column name using the set_axis function, we will pass the new column name and axis that should be replaced with a new name in the column as a parameter.

Code:
```
# Import pandas package
import pandas as pd
  
# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
                     'New Zealand', 'Australia'],
            'odi': ['England', 'India', 'New Zealand',
                    'South Africa', 'Pakistan'],
            't20': ['Pakistan', 'India', 'Australia',
                    'England', 'New Zealand']}
  
# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)
  
# Before renaming the columns
print(rankings_pd.columns)
  
rankings_pd.set_axis(['A', 'B', 'C'], axis='columns', inplace=True)
  
# After renaming the columns
print(rankings_pd.columns)
rankings_pd.head()

```

Method 4: Rename column names using DataFrame add_prefix() and add_suffix() functions

In this example, we will rename the column name using the add_Sufix and add_Prefix function, we will pass the prefix and suffix that should be added to the first and last name of the column name.

Code:
```
# Import pandas package
import pandas as pd
  
# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
                     'New Zealand', 'Australia'],
            'odi': ['England', 'India', 'New Zealand',
                    'South Africa', 'Pakistan'],
            't20': ['Pakistan', 'India', 'Australia',
                    'England', 'New Zealand']}
  
# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)
  
# Before renaming the columns
print(rankings_pd.columns)
  
rankings_pd = rankings_pd.add_prefix('col_')
rankings_pd = rankings_pd.add_suffix('_1')
  
# After renaming the columns
rankings_pd.head()

```

Method 5: Replace specific texts of column names using Dataframe.columns.str.replace function

In this example, we will rename the column name using the replace function, we will pass the old name with the new name as a parameter for the column.

Code: 
```
# Import pandas package
import pandas as pd
  
# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
                     'New Zealand', 'Australia'],
            'odi': ['England', 'India', 'New Zealand',
                    'South Africa', 'Pakistan'],
            't20': ['Pakistan', 'India', 'Australia',
                    'England', 'New Zealand']}
  
# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)
  
# Before renaming the columns
print(rankings_pd.columns)
# df = rankings_pd
  
rankings_pd.columns = rankings_pd.columns.str.replace('test', 'Col_TEST')
rankings_pd.columns = rankings_pd.columns.str.replace('odi', 'Col_ODI')
rankings_pd.columns = rankings_pd.columns.str.replace('t20', 'Col_T20')
  
rankings_pd.head()

```

5. 
Method 1: Drop Columns from a Dataframe using drop() method. 

Example 1: Remove specific single columns. 
```
# Import pandas package
import pandas as pd
  
# create a dictionary with five fields each
data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Remove column name 'A'
df.drop(['A'], axis=1)

```

Example 2: Remove specific multiple columns. 
```
# Import pandas package
import pandas as pd
  
# create a dictionary with five fields each
data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Remove two columns name is 'C' and 'D'
df.drop(['C', 'D'], axis=1)
  
# df.drop(columns =['C', 'D'])

```

Example 3: Remove columns based on column index. 
```
# Import pandas package
import pandas as pd
  
# create a dictionary with five fields each
data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Remove three columns as index base
df.drop(df.columns[[0, 4, 2]], axis=1, inplace=True)
  
df

```

Method 2: Drop Columns from a Dataframe using iloc[] and drop() method. 

Remove all columns between a specific column to another column. 
```
# Import pandas package
import pandas as pd
# create a dictionary with five fields each
data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Remove all columns between column index 1 to 3
df.drop(df.iloc[:, 1:3], inplace=True, axis=1)
  
df

```

6. 

```
# Import pandas package 
import pandas as pd
  
# create a dictionary with five fields each
data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B4'], 
    'C':['C1', 'C2', 'C3', 'C3', 'C3'], 
    'D':['D1', 'D2', 'D2', 'D2', 'D2'], 
    'E':['E1', 'E1', 'E1', 'E1', 'E1'] }
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# Get the unique values of 'B' column
df.B.unique()

```

7. Pandas isnull() function detect missing values in the given object. It return a boolean same-sized object indicating if the values are NA. Missing values gets mapped to True and non-missing value gets mapped to False.

Syntax: DataFrame.isnull()
Parameters: None

8. 


9. 

```
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)

df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)
frames = [df1, df2, df3]
result = pd.concat(frames)

```

10. 

Creating a Dataframe:
```
# importing modules
import pandas as pd
  
# creating a dataframe
df1 = pd.DataFrame({'Name':['Raju', 'Rani', 'Geeta', 'Sita', 'Sohit'],
                    'Marks':[80, 90, 75, 88, 59]})
  
# creating another dataframe with different data
df2 = pd.DataFrame({'Name':['Raju', 'Divya', 'Geeta', 'Sita'],
                    'Grade':['A', 'A', 'B', 'A'],
                    'Rank':[3, 1, 4, 2 ],
                    'Gender':['Male', 'Female', 'Female', 'Female']})
# display df1
display(df1)
  
# display df2
display(df2)

```

Now merge the dataframe on columns "Name", "Grade", "Rank" :

```
# applying merge
df1.merge(df2[['Name', 'Grade', 'Rank']])

```

11. Dataframe.aggregate() function is used to apply some aggregation across one or more column. Aggregate using callable, string, dict, or list of string/callables. Most frequently used aggregations are:

sum: Return the sum of the values for the requested axis
min: Return the minimum of the values for the requested axis
max: Return the maximum of the values for the requested axis

Syntax:
    DataFrame.aggregate(func, axis=0, *args, **kwargs)

Parameters:
    func : callable, string, dictionary, or list of string/callables. Function to use for aggregating the data. If a function, must either work when passed a DataFrame or when passed to DataFrame.apply. For a DataFrame, can pass a dict, if the keys are DataFrame column names.
    axis : (default 0) {0 or ‘index’, 1 or ‘columns’} 0 or ‘index’: apply function to each column. 1 or ‘columns’: apply function to each row.

Returns:
    Aggregated DataFrame

12. pandas.pivot(index, columns, values) function produces pivot table based on 3 columns of the DataFrame. Uses unique values from index / columns and fills with values.

Parameters:
    index[ndarray] : Labels to use to make new frame’s index
    columns[ndarray] : Labels to use to make new frame’s columns
    values[ndarray] : Values to use for populating new frame’s values

Returns:
    Reshaped DataFrame
Exception:
    ValueError raised if there are any duplicates.

13. DataFrame.astype() method is used to cast pandas object to a specified dtype. This function also provides the capability to convert any suitable existing column to a categorical type.


Converting the data types of column "A" and column "B"
```
# importing pandas as pd
import pandas as pd
 
# sample dataframe
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'c', 'd', 'e'],
    'C': [1.1, '1.0', '1.3', 2, 5]})
 
# using dictionary to convert specific columns
convert_dict = {'A': int,
                'C': float
                }
 
df = df.astype(convert_dict)
print(df.dtypes)

```

14. 
Syntax:
    DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’)

Parameters: This method will take following parameters :
    by: Single/List of column names to sort Data Frame by.
    axis: 0 or ‘index’ for rows and 1 or ‘columns’ for Column.
    ascending: Boolean value which sorts Data frame in ascending order if True.
    inplace: Boolean value. Makes the changes in passed data frame itself if True.
    kind: String which can have three inputs(‘quicksort’, ‘mergesort’ or ‘heapsort’) of the algorithm used to sort data frame.
    na_position: Takes two string input ‘last’ or ‘first’ to set position of Null values. Default is ‘last’.

Return Type:
    Returns a sorted Data Frame with Same dimensions as of the function caller Data Frame.

Sort Dataframe rows based on a single column.

```
# import pandas library as pd
import pandas as pd
  
# List of Tuples
students = [('Ankit', 22, 'Up', 'Geu'),
           ('Ankita', 31, 'Delhi', 'Gehu'),
           ('Rahul', 16, 'Tokyo', 'Abes'),
           ('Simran', 41, 'Delhi', 'Gehu'),
           ('Shaurya', 33, 'Delhi', 'Geu'),
           ('Harshita', 35, 'Mumbai', 'Bhu' ),
           ('Swapnil', 35, 'Mp', 'Geu'),
           ('Priya', 35, 'Uk', 'Geu'),
           ('Jeet', 35, 'Guj', 'Gehu'),
           ('Ananya', 35, 'Up', 'Bhu')
            ]
  
# Create a DataFrame object from
# list of tuples with columns
# and indices.
details = pd.DataFrame(students, columns =['Name', 'Age', 
                                           'Place', 'College'],
                        index =[ 'b', 'c', 'a', 'e', 'f',
                                'g', 'i', 'j', 'k', 'd'])

# Sort the rows of dataframe by 'Name' column
rslt_df = details.sort_values(by = 'Name')
  
# show the resultant Dataframe
rslt_df

```

15. DataFrame.copy(deep=True)[source]

Make a copy of this object’s indices and data.

When deep=True (default), a new object will be created with a copy of the calling object’s data and indices. Modifications to the data or indices of the copy will not be reflected in the original object (see notes below).

When deep=False, a new object will be created without copying the calling object’s data or index (only references to the data and index are copied). Any changes to the data of the original will be reflected in the shallow copy (and vice versa).

Parameters:
    deep: bool, default True
        Make a deep copy, including a copy of the data and the indices. With deep=False neither the indices nor the data are copied.

Returns:
    copy: Series or DataFrame
        Object type matches caller.

Notes

When deep=True, data is copied but actual Python objects will not be copied recursively, only the reference to the object. This is in contrast to copy.deepcopy in the Standard Library, which recursively copies object data (see examples below).

While Index objects are copied when deep=True, the underlying numpy array is not copied for performance reasons. Since Index is immutable, the underlying data can be safely shared and a copy is not needed.

```
s = pd.Series([1, 2], index=["a", "b"])
s_copy = s.copy()
s_copy

```
Shallow copy versus default (deep) copy:

```
s = pd.Series([1, 2], index=["a", "b"])
deep = s.copy()
shallow = s.copy(deep=False)

```

Shallow copy shares data and index with original.
Deep copy has own copy of data and index.

16. 
Method 1: Using loc
```
# import module
import pandas as pd
 
# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                           
                          'Age': [30, 35, 37, 33, 34, 30],
                           
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                           
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
# filter dataframe
display(dataFrame.loc[(dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')),
                    ['Name','JOB']])

```

Method 2: Using NumPy
```
# import module
import pandas as pd
import numpy as np
 
# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                           
                          'Age': [30, 35, 37, 33, 34, 30],
                           
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                           
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
 
# filter dataframe                                  
filtered_values = np.where((dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')))
print(filtered_values)
display(dataFrame.loc[filtered_values])

```

Method 3: Using Query (eval and query works only with columns)
```
# import module
import pandas as pd
 
# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                           
                          'Age': [30, 35, 37, 33, 34, 30],
                           
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                           
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
 
# filter dataframe
display(dataFrame[(dataFrame['Salary']>=100000) & (dataFrame['Age']<40) & dataFrame['JOB'].str.startswith('P')][['Name','Age','Salary']])

```

Method 5: Eval multiple conditions  (“eval” and “query” works only with columns )

```
# import module
import pandas as pd
 
# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                           
                          'Age': [30, 35, 37, 33, 34, 30],
                           
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                           
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
 
# filter dataframe
display(dataFrame[dataFrame.eval("Salary <=100000 & (Age <40) & JOB.str.startswith('A').values")])

```

Dataframes are a very essential concept in Python and filtration of data is required can be performed based on various conditions. They can be achieved in any one of the above ways. Points to be noted:

    loc works with column labels and indexes.
    eval and query works only with columns.
    Boolean indexing works with values in a column only.

17. Pandas dataframe.mean() function return the mean of the values for the requested axis. If the method is applied on a pandas series object, then the method returns a scalar value which is the mean value of all the observations in the dataframe. If the method is applied on a pandas dataframe object, then the method returns a pandas series object which contains the mean of the values over the specified axis.

Syntax:
    DataFrame.mean(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)

Parameters :
    axis : {index (0), columns (1)}
    skipna : Exclude NA/null values when computing the result

    level : If the axis is a MultiIndex (hierarchical), count along a particular level, collapsing into a Series

    numeric_only : Include only float, int, boolean columns. If None, will attempt to use everything, then use only numeric data. Not implemented for Series.

Returns :
    mean : Series or DataFrame (if level specified)

Example #1: Use mean() function to find the mean of all the observations over the index axis.

```
# importing pandas as pd
import pandas as pd
  
# Creating the dataframe 
df = pd.DataFrame({"A":[12, 4, 5, 44, 1],
                   "B":[5, 2, 54, 3, 2], 
                   "C":[20, 16, 7, 3, 8],
                   "D":[14, 3, 17, 2, 6]})

# Even if we do not specify axis = 0,
# the method will return the mean over
# the index axis by default
df.mean(axis = 0)

```

Example #2: Use mean() function on a dataframe which has Na values. Also find the mean over the column axis.

```
# importing pandas as pd
import pandas as pd
  
# Creating the dataframe 
df = pd.DataFrame({"A":[12, 4, 5, None, 1],
                   "B":[7, 2, 54, 3, None],
                   "C":[20, 16, 11, 3, 8],.
                   "D":[14, 3, None, 2, 6]})
  
# skip the Na values while finding the mean
df.mean(axis = 1, skipna = True)

```

18. Pandas dataframe.std() function return sample standard deviation over requested axis. By default the standard deviations are normalized by N-1. It is a measure that is used to quantify the amount of variation or dispersion of a set of data values.

Syntax :
    DataFrame.std(axis=None, skipna=None, level=None, ddof=1, numeric_only=None, **kwargs)

Parameters :
    axis : {index (0), columns (1)}
    skipna : Exclude NA/null values. If an entire row/column is NA, the result will be NA
    level : If the axis is a MultiIndex (hierarchical), count along a particular level, collapsing into a Series
    ddof : Delta Degrees of Freedom. The divisor used in calculations is N – ddof, where N represents the number of elements.
    numeric_only : Include only float, int, boolean columns. If None, will attempt to use everything, then use only numeric data. Not implemented for Series.

Return :
    std : Series or DataFrame (if level specified)

Example #1: Use std() function to find the standard deviation of data along the index axis.

```
# importing pandas as pd
import pandas as pd
  
# Creating the dataframe 
df = pd.read_csv("nba.csv")

# finding STD
df.std(axis = 0, skipna = True)

```

Example #2: Use std() function to find the standard deviation over the column axis.

```
# importing pandas as pd
import pandas as pd
  
# Creating the dataframe 
df = pd.read_csv("nba.csv")
  
# STD over the column axis.
df.std(axis = 1, skipna = True)

```

19. Correlation is used to summarize the strength and direction of the linear association between two quantitative variables. It is denoted by r and values between -1 and +1. A positive value for r indicates a positive association, and a negative value for r indicates a negative association.

Syntax:
    dataframe[‘first_column’].corr(dataframe[‘second_column’])
where,

    dataframe is the input dataframe
    first_column is correlated with second_column of the dataframe

Example 1: Python program to get the correlation among two columns

```
# import pandas module
import pandas as pd
 
# create dataframe with 3 columns
data = pd.DataFrame({
    "column1": [12, 23, 45, 67],
    "column2": [67, 54, 32, 1],
    "column3": [34, 23, 56, 23]
}
)
# display dataframe
print(data)
 
# correlation between column 1 and column2
print(data['column1'].corr(data['column2']))
 
# correlation between column 2 and column3
print(data['column2'].corr(data['column3']))
 
# correlation between column 1 and column3
print(data['column1'].corr(data['column3']))

```

Example 2: Get the element-wise correlation

```
# import pandas module
import pandas as pd
 
# create dataframe with 3 columns
data = pd.DataFrame({
    "column1": [12, 23, 45, 67],
    "column2": [67, 54, 32, 1],
    "column3": [34, 23, 56, 23]
}
)
# get correlation between element wise
print(data.corr())

```

20. 

```
import pandas as pd
titanic = pd.read_csv("data/titanic.csv")
titanic.head()
ages = titanic["Age"]
ages.head()

```
Each column in a DataFrame is a Series. As a single column is selected, the returned object is a pandas Series.

21. 
The iloc[ ] is used for selection based on position. It is similar to loc[] indexer but it takes only integer values to make selections. 
Example 1: select a single row. 

```
# import pandas
import pandas as pd
 
# List of Tuples
employees = [('Stuti', 28, 'Varanasi', 20000),
            ('Saumya', 32, 'Delhi', 25000),
            ('Aaditya', 25, 'Mumbai', 40000),
            ('Saumya', 32, 'Delhi', 35000),
            ('Saumya', 32, 'Delhi', 30000),
            ('Saumya', 32, 'Mumbai', 20000),
            ('Aaditya', 40, 'Dehradun', 24000),
            ('Seema', 32, 'Delhi', 70000)
            ]
 
# Create a DataFrame object from list
df = pd.DataFrame(employees,
                columns =['Name', 'Age',
                'City', 'Salary'])
 
# Using the operator .iloc[]
# to select single row
result = df.iloc[2]
 
# Show the dataframe
result
# import pandas
import pandas as pd
 
# List of Tuples
employees = [('Stuti', 28, 'Varanasi', 20000),
            ('Saumya', 32, 'Delhi', 25000),
            ('Aaditya', 25, 'Mumbai', 40000),
            ('Saumya', 32, 'Delhi', 35000),
            ('Saumya', 32, 'Delhi', 30000),
            ('Saumya', 32, 'Mumbai', 20000),
            ('Aaditya', 40, 'Dehradun', 24000),
            ('Seema', 32, 'Delhi', 70000)
            ]
 
# Create a DataFrame object from list
df = pd.DataFrame(employees,
                columns =['Name', 'Age',
                'City', 'Salary'])
 
# Using the operator .iloc[]
# to select single row
result = df.iloc[2]
 
# Show the dataframe
result

```

Example 2: Select multiple rows.

```
# import pandas
import pandas as pd
 
# List of Tuples
employees = [('Stuti', 28, 'Varanasi', 20000),
             ('Saumya', 32, 'Delhi', 25000),
             ('Aaditya', 25, 'Mumbai', 40000),
             ('Saumya', 32, 'Delhi', 35000),
             ('Saumya', 32, 'Delhi', 30000),
             ('Saumya', 32, 'Mumbai', 20000),
             ('Aaditya', 40, 'Dehradun', 24000),
             ('Seema', 32, 'Delhi', 70000)
             ]
 
# Create a DataFrame object from list
df = pd.DataFrame(employees,
                  columns=['Name', 'Age',
                           'City', 'Salary'])
 
# Using the operator .iloc[]
# to select multiple rows
result = df.iloc[[2, 3, 5]]
 
# Show the dataframe
result

```

22. 

23. Given a Dataframe containing data about an event, we would like to create a new column called ‘Discounted_Price’, which is calculated after applying a discount of 10% on the Ticket price.

Example 1: We can use DataFrame.apply() function to achieve this task. 
```
# importing pandas as pd
import pandas as pd
 
# Creating the DataFrame
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})
 
# Print the dataframe
print(df)

df['Discounted_Price'] = df.apply(lambda row: row.Cost -
                                  (row.Cost * 0.1), axis = 1)
 
# Print the DataFrame after addition
# of new column
print(df)

```

Example 2: We can achieve the same result by directly performing the required operation on the desired column element-wise. 
```
import pandas as pd
 
# Creating the DataFrame
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})
 
# Create a new column 'Discounted_Price' after applying
# 10% discount on the existing 'Cost' column.
 
# create a new column
df['Discounted_Price'] = df['Cost'] - (0.1 * df['Cost'])
 
# Print the DataFrame after
# addition of new column
print(df)

```

Example 3: Using DataFrame.map() function to create new column from existing column using a mapping function

```
# We will create a dataframe with some sample data:
data = {
    "name": ["John", "Ted", "Dev", "Brad", "Rex", "Smith", "Samuel", "David"],
    "salary": [10000, 20000, 50000, 45500, 19800, 95000, 5000, 50000]
}
# create dataframe from data dictionary
df = pd.DataFrame(data)
# print the dataframe
display(df.head())

# Now, we will create a mapping function (salary_stats) and use the DataFrame.map() function to create a new column from an existing column

def salary_stats(value):
    if value < 10000:
        return "very low"
    if 10000 <= value < 25000:
        return "low"
    elif 25000 <= value < 40000:
        return "average"
    elif 40000 <= value < 50000:
        return "better"
    elif value >= 50000:
        return "very good"
 
df['salary_stats'] = df['salary'].map(salary_stats)
display(df.head())

```

24. DataFrame.drop_duplicates(subset=None, *, keep='first', inplace=False, ignore_index=False)[source]

Return DataFrame with duplicate rows removed.

Considering certain columns is optional. Indexes, including time indexes are ignored.

Parameters:
    subset: column label or sequence of labels, optional
        Only consider certain columns for identifying duplicates, by default use all of the columns.

    keep: {‘first’, ‘last’, False}, default ‘first’
        Determines which duplicates (if any) to keep. - first : Drop duplicates except for the first occurrence. - last : Drop duplicates except for the last occurrence. - False : Drop all duplicates.

    inplace: bool, default False
        Whether to modify the DataFrame rather than creating a new one.

    ignore_index: bool, default False
        If True, the resulting axis will be labeled 0, 1, …, n - 1.

Returns:
    DataFrame or None
        DataFrame with duplicates removed or None if inplace=True.

```
df = pd.DataFrame({

    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],

    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],

    'rating': [4, 4, 3.5, 15, 5]

})
df

```

By default, it removes duplicate rows based on all columns.

```
df.drop_duplicates()

```

To remove duplicates on specific column(s), use subset.

```
df.drop_duplicates(subset=['brand'])

```

To remove duplicates and keep last occurrences, use keep.

```
df.drop_duplicates(subset=['brand', 'style'], keep='last')

```

25. Pandas library of python is very useful for the manipulation of mathematical data and is widely used in the field of machine learning. It comprises many methods for its proper functioning. loc() and iloc() are one of those methods. These are used in slicing data from the Pandas DataFrame. They help in the convenient selection of data from the DataFrame in Python. They are used in filtering the data according to some conditions. 

The loc() function is label based data selecting method which means that we have to pass the name of the row or column which we want to select. This method includes the last element of the range passed in it, unlike iloc(). loc() can accept the boolean data unlike iloc().

The iloc() function is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column. This method does not include the last element of the range passed in it unlike loc(). iloc() does not accept the boolean data unlike loc(). 

