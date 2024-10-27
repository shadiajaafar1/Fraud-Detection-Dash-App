import dash
from dash import html

dash.register_page(__name__,path="/",name="About Us")


layout = html.Div([
    html.Div(
            html.Img(src="assets\images\intro1.png", style={'width': '100%'})
    ),
    html.Div(
        html.Img(src="assets\images\intro2.png", style={'width': '100%'})
    )
    ,
    html.Div(
        html.Img(src="assets\images\intro3.png", style={'width': '100%'})
    )
    
])