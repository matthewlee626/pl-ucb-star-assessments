import random
import pandas as pd
import prairielearn as pl


def generate(data):
    dummy_data = {
        'Category': ['A', 'A', 'B', 'B'],
        'Item': ['X', 'Y', 'X', 'Y'],
        'Value': [10, 15, 20, 25],
        'Quantity': [100, 150, 200, 250]
    }
    input_df = pd.DataFrame(dummy_data)
    data["params"]["input_df"] = pl.to_json(input_df)