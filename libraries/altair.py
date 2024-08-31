import altair as alt
import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [6, 7, 2, 4, 5]
})

chart = alt.Chart(df).mark_line().encode(
    x='x',
    y='y'
)

chart.show()
