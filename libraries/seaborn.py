import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species")
plt.show()
