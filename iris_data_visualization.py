import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
#multivariate analysis
print(df.head())
sns.pairplot(df, hue= "species", height=2)
print("Correlation Table:")
print(df.drop("species", axis=1).corr())
plt.show()