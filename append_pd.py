import pandas as pd
def append_hough_row(df, new_row):
    columns=['IS CIRCLE', 'CIRCLED IMG', 'HOUGH SCORE', 'MEAN X', ' MEAN Y']
    return pd.concat([ df, pd.DataFrame([new_row], columns=columns)], join = "inner")