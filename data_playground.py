import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Code below allows me to view entire table when I print it (in PyCharm IDE)
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 30)

# nba_data.csv downloaded from Kaggle
nba = pd.read_csv("nba_data.csv", index_col=0)

# Shows the head and tail of the data in PyCharm
print(nba)

# Select [all rows, [some columns]].arrange by points scored.print the top x columns
print(nba.loc[:, ['player_name', 'season', 'pts']].sort_values(by='pts', ascending=False).iloc[0:30])


# Function to fix the season column to be a single year int
def fix_season(row):
    row.season = int(row.season[0:4]) + 1
    return row


# Applies the function above to the nba dataframe
nba = nba.apply(fix_season, axis='columns')

