import pandas as pd
import plotly.express as px
df=pd.read_csv("covid.csv")
figure=px.scatter(df,x="date",y="cases",color="country",title="Covid-19 cases in different countries of the world")
figure.show()