from plotnine import ggplot, aes, geom_line, labs
import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 5, 7, 11]
})

plot = ggplot(df, aes(x='x', y='y')) + geom_line() + labs(title='Simple Line Plot')
print(plot)
