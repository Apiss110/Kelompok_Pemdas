# %%
import pandas as pd

df = pd.read_csv('jumlah_penderita_diabetes_jabar.csv')
df

# %%
df.head()

# %%
df.tail()

# %%


# %%
df.info()
df

df.groupby("tahun")["jumlah_penderita_dm"].sum()