import pandas as pd
  
# list of strings
lst = ['21.678030263937238 ']
  
# list of int
lst2 = ['71.89884338765924']
  
# Calling DataFrame constructor after zipping
# both lists, with columns specified
df = pd.DataFrame(list(zip(lst, lst2)),
               columns =['Name', 'val'])
print(df)

