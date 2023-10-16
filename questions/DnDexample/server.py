import io
import pandas as pd


def generate(data):

    # Generate complete html string
    df = pd.DataFrame({"Column1": ["Row1", "Row2", "Row3", "Row4", "Row5"],
                   "Column2": ["Row1", "Row2", "Row3", "Row4", "Row5"],
                   "Column3": ["Row1", "Row2", "Row3", "Row4", "Row5"],
                   "Column4": ["Row1", "Row2", "Row3", "Row4", "Row5"],
                   "Column5": ["Row1", "Row2", "Row3", "Row4", "Row5"]})
                   
    mytable = df.to_html()
    data["params"]["mytable"] = mytable


def operation(df):
    cols = df.columns.to_list()
    new_cols = cols[1:] + [cols[0]]
    answer_df = df[new_cols]

    
