import pandas as pd
from pandas.core.interchange import dataframe

nba_df = pd.DataFrame({
    'Team': ['Cleveland Cavaliers', 'Boston Celtics', 'Golden State Warriors', 'Oklahoma City Thunder', 'Houston Rockets', 'Los Angeles Lakers', 'LA Clippers', 'Orlando Magic', 'Denver Nuggets', 'Memphis Grizzlies'],
    'GP': [18, 17, 16, 16, 18, 16, 18, 18, 15, 17],
    'W': [17, 14, 12, 12, 12, 10, 11, 11, 9, 10,],
    'L': [1, 3, 4, 4, 6, 6, 7, 7, 6, 7],
    'Win %': [.944, .824, .750, .750, .667, .625, .611, .611, .600, .588],
    'Min': [48.0, 48.9, 48.3, 48.0, 48.3, 48.0, 48.3, 48.0, 48.7, 48.0],
    'Points': [123.4, 119.9, 117.6, 114.3, 113.8, 116.4, 109.5, 107.0, 117.5, 120.3]
})

def nba_df_info(df):
    print("DataFrame Info:")
    df.info()
    print("\nSize of DataFrame:")
    print(f"Rows - {df.shape[0]}\nColumns - {df.shape[1]}")
    print("\nColumn Data Types:")
    print(df.dtypes)

#function for question 1
nba_df_info(nba_df)

#pulling information for the top seed from the East and West based on current info for question 2
top_seeds = nba_df.iloc[[0, 2]]
print('\n',top_seeds)

#Sorts DataFrame by points for question 3/ ascending False = highest to lowest
sorted_df = nba_df.sort_values(by='Points', ascending=False)
print('\n',sorted_df)

#List for AST column values
new_column_info = [28.4, 25.6, 30.2, 25.3, 22.7, 26.9, 25.5, 24.6, 30.3, 29.8]

#using .insert() to insert new 'AST' column at index 7 using the info from previous list
nba_df.insert(7, 'AST', new_column_info)
print('\n',nba_df)

#using .loc to add a new row at the end of the DataFrame
nba_df.loc[len(nba_df)] = ['Toronto Raptors', 17, 4, 13, .235, 48.9, 112.9, 27.9]
print('\n',nba_df)

nba_df.to_csv('extra_credit.csv')