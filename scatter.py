import pandas as pd
import plotly.express as px

df = pd.read_csv("C - 103.csv")

fig = px.scatter(df, x = "date", y = "cases", color = "country")

fig.show()