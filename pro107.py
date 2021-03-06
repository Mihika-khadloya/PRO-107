import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df=pd.read_csv("data107.csv")
fig=go.Figure(go.Scatter(x=df.groupby("level")["attempt"].mean(),y=["Level 1","Level 2","Level 3","Level 4"],orientation="h"))
fig.show()