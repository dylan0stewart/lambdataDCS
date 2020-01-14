"""
Utility functions for working with DataFrames
"""
import pandas

def tvt_split(X):
    '''
    This function will split your dataframe into a 60%/20%/20% split for your
    train, validation, and test sets accordingly.
    '''
    X = X.copy()
    train, validate, test = np.split(.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])

def show_nans(X):
    '''
    This Function will copy your dataframe, then print out a list of which 
    columns have NaNs, and how many there are in that column.
    '''
    X = X.copy()
    cols_w_nans = X.columns[X.isna().any()].tolist()
    df_nan_cols = pd.DataFrame(df[cols_with_nans])
    return df_nan_cols.isnull().sum()
