from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

colorscales = px.colors.named_colorscales()
#df = px.data.iris()
folder = ""
file = "GLB.Ts+dSST.csv"
df = pd.read_csv(folder + file)
#df = df.sort_values(by='Year', ascending=False)
print(df.head())

tempData = df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
years = df['Year']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig = px.imshow(
    tempData,
    x=months,
    y=years,
    #color_continuous_scale='RdBu_r',
    color_continuous_scale='Portland',
    labels=dict(x="Month", y="Year", color=u"Temp(C\xb0)")
    )
fig.update_layout(title_text='Global Average Temperatures 1880-2023', yaxis_title=None, xaxis_title=None)
fig.update_xaxes(side="bottom")
fig.update_yaxes(autorange=True, dtick=20)

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)