import pandas as pd

df = pd.DataFrame( 
    [ 
        [1, 'Math for Juniors', 3, False], 
        [2, 'Geometry in Nature', 1, False], 
        [3, 'Just a Chance', 1, True], 
        [4, 'About zero', 2, False], 
    ] 
)

df.columns = ['Id', 'Name', 'Amount', 'Promo']

print(df)
print(df[['Name', 'Amount']])

print(df.iloc[1:, 1])
print(df.iloc[:, 2])

print( df[df.Amount > 0] ) #warunki
print( df[(df.Amount > 0) | (df.Promo == True)] ) 
