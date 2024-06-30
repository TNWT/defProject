import pandas as pd  
#create a pandas dataframe for testing with two columns A integer and B string 
df = pd.DataFrame([(1, 'Ms'),  (1, 'PhD'),  
                   (2, 'Ms'),  (2, 'Bs'),  
                   (3, 'PhD'), (3, 'Bs'),  
                   (4, 'Ms'),  (4, 'PhD'),   (4, 'Bs')], 
                   columns=['A', 'B']) 
print("Original data") 
print(df) 
 
# force the column's string column B to type 'category'  
df['B'] = df['B'].astype('category') 
# define the valid categories: 
df['B'] = df['B'].cat.set_categories(['PhD', 'Bs', 'Ms'], ordered=True) 
#pandas dataframe sort_values to inflicts order on your categories 
df.sort_values(['A', 'B'], inplace=True, ascending=True) 
print("Now sorted by custom categories (PhD > Bs > Ms)") 
print(df) 
# dropping duplicates keeps first
df_unique = df.drop_duplicates('A') 
print("Keep the highest value category given duplicate integer group") 
print(df_unique)