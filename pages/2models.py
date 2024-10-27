import dash
from dash import html, dcc, Dash, Input, Output, callback
import dash_table
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/2models", name="Classifier")

data = [
    {"Model": "Logistic Regression", "ROC AUC": 0.740867, "Precision": 0.071429, "Recall": 0.000471, "F1 Score": 0.000937, "Elapsed Time": 285.221055},
    {"Model": "Random Forest", "ROC AUC": 0.882752, "Precision": 0.902703, "Recall": 0.157473, "F1 Score": 0.268165, "Elapsed Time": 425.084264},
    {"Model": "XGboost", "ROC AUC": 0.879682, "Precision": 0.840153, "Recall": 0.154880, "F1 Score": 0.261545, "Elapsed Time": 114.876388},
    {"Model": "Balanced Random Forest", "ROC AUC": 0.882432, "Precision": 0.124836, "Recall": 0.809288, "F1 Score": 0.216306, "Elapsed Time": 584.580105},
]   

data_nuevo = [
    {"Model": "Stacking", "ROC AUC": 0.889560, "Precision": 0.783822, "Recall": 0.258133, "F1 Score": 0.388367, "Elapsed Time": 791.302695},
]

layout = html.Div([
    html.H2("Single Models", style={'textAlign': 'left', 'color': 'white', 'marginBottom': '20px'}),
    # Modelos individuales
    dbc.Container([
        # Contenedor de la tabla
        dbc.Row([
            dbc.Col(
                html.Div(
                    dash_table.DataTable(
                        id='table',
                        columns=[{'name': i, 'id': i} for i in data[0].keys()],
                        data=data,
                        style_table={'width': '100%', 'height': '100%', 'marginBottom': '0px'},
                        style_cell={'textAlign': 'left', 'padding': '12px', 'fontSize': '14px'},
                        style_header={'backgroundColor': '#0c1d44', 'color': 'white', 'fontSize': '13px'},
                        style_data={'backgroundColor': '#0c1d44', 'color': 'white', 'fontSize': '12px'}
                    ), className='table-container'
                ), width=7, className='dash-col'
            ),
            dbc.Col(
                html.Div([
                    html.Img(src='assets/images/roc2.png', style={'width': '100%', 'height': '100%'})
                ], className='image-container'), width=5
            ),
        ], className='dash-row'),
        # Contenedor de imágenes adicionales en la segunda fila
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.Div([
                        html.Img(src='assets/images/lr1.png')
                    ], className='second-row-image-item'),
                    html.Div([
                        html.Img(src='assets/images/rf1.png')
                    ], className='second-row-image-item'),
                    html.Div([
                        html.Img(src='assets/images/xg1.png')
                    ], className='second-row-image-item'),
                    html.Div([
                        html.Img(src='assets/images/balanced.png')
                    ], className='second-row-image-item'),
                ], className='second-row-images-container'),
            width=12),
        ], className='dash-row'),
    ], fluid=True, className='dash-container'),
    
    html.H2("Stacking Model", style={'textAlign': 'left', 'color': 'white', 'marginBottom': '20px'}),
    # Modelo nuevo
    dbc.Container([
        # Contenedor de la tabla
        dbc.Row([
            dbc.Col(
                html.Div(
                    dash_table.DataTable(
                        id='table',
                        columns=[{'name': i, 'id': i} for i in data_nuevo[0].keys()],
                        data=data_nuevo,
                        style_table={'width': '100%', 'height': '100%', 'marginBottom': '0px'},
                        style_cell={'textAlign': 'left', 'padding': '12px', 'fontSize': '14px'},
                        style_header={'backgroundColor': '#005184', 'color': 'white', 'fontSize': '13px'},
                        style_data={'backgroundColor': '#005184', 'color': 'white', 'fontSize': '12px'}
                    ), className='table-container-nuevo'
                ), width=12, className='dash-col'
            ),
        ], className='dash-row'),
        # Contenedor de imágenes adicionales en la segunda fila
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.Div([
                        html.Img(src='assets/images/cm_nuevo.jpg')
                    ], className='second-row-image-item-nuevo'),
                    html.Div([
                        html.Img(src='assets/images/fi_nuevo.jpg')
                    ], className='second-row-image-item-nuevo'),
                    html.Div([
                        html.Img(src='assets/images/croc_nuevo.jpg')
                    ], className='second-row-image-item-nuevo'),
                ], className='second-row-images-container-nuevo'),
            width=12),
        ], className='dash-row'),
    ], fluid=True, className='dash-container')
], style={'margin': '15px', 'padding': '0px'})
