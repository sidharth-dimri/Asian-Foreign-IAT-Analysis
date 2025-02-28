import pandas as pd
#.sav should be the input files name
df = pd.read_spss("Asian IAT.public.2021.sav")
#.csv should be the output files name
df.to_csv("Asian IAT.public.2021.csv", index=False)
