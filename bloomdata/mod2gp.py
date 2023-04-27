# from pandas import DataFrame
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestClassifier

# from sklearn.metrics import mean_absolute_error

import pandas as pd

# Build my class of type DataFrame
# df holds a DataFrame 'object'
# when I create a new object and save it to a variable
#  I say that I have 'instantiated' that object
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

if __name__ == '__main__':

    # Variables that form part of an 'object'
    # are called 'attributes'
    # we will access them using 'dot-notation'
    print(df.dtypes)
    print(df.shape)
    print(df.index)
    print(df.columns)

    # Functions that form part of an 'object'
    # are called 'methods'
    print(df.head())
    print(df.describe())
    print(df.isna().sum())

    # a method associated with a Panda 'Series' object
    # aka 'columns'
    # which lives inside of a dataframe
    print(df['a'].value_counts())