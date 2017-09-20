import pandas as pd
import numpy as np

data = pd.DataFrame([])

for i in np.arange(0, 4):
  if i % 2 == 0:
    data = data.append(pd.DataFrame({'A': i, 'B': i + 1}, index=[0]), ignore_index=True)
  else:
    data = data.append(pd.DataFrame({'A': i}, index=[0]), ignore_index=True)

print(data.head())
