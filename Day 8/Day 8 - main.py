import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {'Customer': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Units': [50, 120, 250, 80, 300],
        'Bill': [550, 1034, 1950, 750, 2300]}
df = pd.DataFrame(data)

sns.scatterplot(data=df, x='Units', y='Bill').set_title("Units vs Bill")
plt.show()

sns.barplot(data=df.nlargest(5, 'Bill'), x='Customer', y='Bill').set_title("Top 5")
plt.show()