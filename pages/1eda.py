from dash import html, dcc, Dash, Input, Output, callback
import pandas as pd
import plotly.graph_objects as go
import dash
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, ALL  # Asegúrate de incluir ALL aquí


color_fraude = ['#06D6A0', '#EB5160']  # verde, rojo
#---------------------------------------Funciones-----------------------------------------------------------
def boxplot_transaction(df):
    color_fraude = {0: '#06D6A0', 1: '#EB5160'}
    fraud_labels = {0: 'False', 1: 'True'}
    fig = px.box(df, x='isFraud', y='TransactionDT',
                 labels={'isFraud': 'Fraud', 'TransactionDT': 'Transaction Time'},
                 title='<b>Fraud Transaction Time Distribution</b>',
                 color='isFraud',
                 color_discrete_map=color_fraude)
    
    fig.for_each_trace(lambda t: t.update(name = fraud_labels[int(t.name)]))

    fig.update_layout(
        title={
            'text': '<b>Transaction Time Distribution</b>',
            'y': 0.9, 
            'x': 0.5, 
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 15, 'color': 'white'}  
        },
        xaxis_title='Fraud',
        yaxis_title='Duration of the Transaction',
        xaxis={'title': {'font': {'size': 14, 'color': 'white'}},
               'color': 'white'}, 
        yaxis={'title': {'font': {'size': 14, 'color': 'white'}},
               'color': 'white'},
        template='plotly_white',
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        margin=dict(t=45, b=15)
    )
    
    fig.update_layout(legend={'title_font': {'color': 'white'}, 'font': {'color': 'white'}})

    return fig


def transaction_histogram(df):
    x_non_fraudulent = df[df['isFraud'] == 0]['TransactionDT']
    x_fraudulent = df[df['isFraud'] == 1]['TransactionDT']
    fig = go.Figure()

    fig.add_trace(go.Histogram(
        x=x_non_fraudulent,
        nbinsx=500, 
        name='False', 
        marker_color='#06D6A0' 
    ))
    
    fig.add_trace(go.Histogram(
        x=x_fraudulent,
        nbinsx=500,
        name='True',  
        marker_color='#EB5160' 
    ))

    fig.update_layout(
    legend_title_text='Fraud',
    title={
        'text': '<b>TransactionDT Distribution</b>',  
        'y': 0.9,  
        'x': 0.5, 
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 15, 'color': 'white'}
    },
    xaxis={
        'title': {'text': 'TransactionDT', 'font': {'size': 14, 'color': 'white'}},
        'color': 'white'
    },
    yaxis={
        'title': {'text': 'Frecuency', 'font': {'size': 14, 'color': 'white'}},
        'color': 'white',
        
    },
    template='plotly_white',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)', 
    showlegend=True,
    bargap=0.1,  
    bargroupgap=0.2,  
    barmode='overlay',  
    legend={
        'title_font': {'color': 'white'},
        'font': {'color': 'white'} 
    },
    margin=dict(t=45, b=15)
)
    fig.update_traces(opacity=0.75)  
    return fig

def boxplot_card2(df):
    color_fraud = {0: '#06D6A0', 1: '#EB5160'}
    fig = px.box(df, x='isFraud', y='card2',
                 labels={'isFraud': 'Fraud', 'card2': 'Card2'},
                 title='<b>Distribution of card2 by fraud</b>',
                 color='isFraud',
                 color_discrete_map=color_fraud,
                 category_orders={'isFraud': [0, 1]},  # Ordenar las categorías en el eje x
                 )

    fig.update_layout(
        title={
            'text': '<b>Distribution of card2 by fraud</b>',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 15, 'color': 'white'}
        },
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='Fraud',
        yaxis_title='card2',
        xaxis=dict(
            title='Fraud',
            title_font={'size': 14, 'color': 'white'},
            tickfont={'color': 'white'},
            type='category'
        ),
        yaxis=dict(
            title='card2',
            title_font={'size': 14, 'color': 'white'},
            tickfont={'color': 'white'}
        ),
        legend={'title': 'Fraud', 'title_font': {'color': 'white'}, 'font': {'color': 'white'}, 'itemsizing': 'constant'},  # Cambiar el título de la leyenda
        showlegend=True,
        margin=dict(t=45, b=15)
    )

    # Cambiar los textos de la leyenda
    fig.for_each_trace(lambda trace: trace.update(name="true" if trace.name == '1' else "false"))

    return fig


def scatter_c5(df):
    df['Fraude_Label'] = df['isFraud'].map({0: 'No Fraud', 1: 'Fraud'})
    
    fig = px.scatter(df, x='C5', y='isFraud',
                     color='Fraude_Label', 
                     labels={'isFraud': '', 'C5': 'C5'},
                     title='<b>Relationship of C5 with Fraud</b>',
                     color_discrete_map={'No Fraud': '#06D6A0', 'Fraud': '#EB5160'}) 

    fig.update_layout(
        title={
            'text': '<b>Relationship of C5 with Fraud</b>',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 15, 'color': 'white'}
        },
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='C5',
        xaxis={
            'title': {'font': {'size': 14, 'color': 'white'}},
            'tickfont': {'color': 'white'}
        },
        yaxis={
            'title': {'font': {'size': 14, 'color': 'white'}},
            'tickmode': 'array',
            'tickvals': [0, 1],
            'ticktext': ['No Fraud', 'Fraud'],
            'tickfont': {'color': 'white'}
        },
        showlegend=False,
        margin=dict(t=45, b=15)
    )

    return fig

def barra_card4(df):
    grouped_data = df.groupby(['card4', 'isFraud']).size().unstack(fill_value=0)
    fig = go.Figure()
    fraud_labels = {0: 'False', 1: 'True'}
    for is_fraud, color in zip(grouped_data.columns, ['#06D6A0', '#EB5160']):
        fig.add_trace(go.Bar(
            x=grouped_data.index,
            y=grouped_data[is_fraud],
            name= fraud_labels[is_fraud],
            marker_color=color
        ))

    fig.update_layout(
        barmode='group',
        title={
            'text': '<b>Distribution of card4 by Fraud</b>',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 15, 'color': 'white'}
        },
        xaxis_title='Card Type',
        yaxis_title='Frequency',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis={
            'title': {'font': {'size': 14, 'color': 'white'}},
            'tickfont': {'color': 'white'}
            
        },
        yaxis={
            'title': {'font': {'size': 14, 'color': 'white'}},
            'tickfont': {'color': 'white'},
            'tickmode': 'array',
            'tickvals': list(range(0, grouped_data.max().max() + 1, 50000)),
            'ticktext': [f'{val//1000}K' for val in range(0, grouped_data.max().max() + 1, 50000)]
            
        },
        legend_title_text='Fraud', 
        legend={'title_font': {'color': 'white'}, 'font': {'color': 'white'}},
        showlegend=True,
        margin=dict(t=50, b=15)
    )

    return fig

def correlacion(df):
    df_numeric = df[['TransactionDT','card2', 'C5', 'TransactionAmt']]
    correlation_matrix = df_numeric.corr(method='spearman')
    
    color_scale = [
        [0.0, '#E8E8E8'],
        [0.5, '#E29797'],  
        [1.0, '#EB5160'] 
    ]

    fig = ff.create_annotated_heatmap(
        z=correlation_matrix.values,
        x=list(correlation_matrix.columns),
        y=list(correlation_matrix.index),
        annotation_text=correlation_matrix.round(2).values,
        colorscale=color_scale,
        showscale=True
    )

    fig.update_layout(
        title={
            'text': '<b>Correlation Matrix</b>',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 15, 'color': 'white'} 
        },
         xaxis=dict(
            side='bottom',  
            tickmode='auto' 
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white'},
        margin=dict(t=50, b=20)
    )
    return fig

#----------------------------------------------------------------------------------------------------------------------------

dash.register_page(__name__,path="/1eda",name="EDA")

df = pd.read_csv('datos_eda.csv')
categorias = df['card6'].dropna().unique()[:2]

def update_figures(filter_value):
    filtered_df = df[df['card6'] == filter_value] if filter_value else df   
    fig2 = boxplot_transaction(filtered_df)
    fig3 = transaction_histogram(filtered_df)
    fig4 = boxplot_card2(filtered_df)
    fig10 = barra_card4(filtered_df)
    fig11 = correlacion(filtered_df)
    fig9 = scatter_c5(filtered_df)
    figures = [fig2, fig3, fig4, fig10, fig9, fig11]
    
    for fig in figures:  
        fig.update_layout(
            autosize=True,
            height=300 
        )
    
    return figures

def get_transaction_counts(filter_value):
    filtered_df = df[df['card6'] == filter_value] if filter_value else df
    counts = filtered_df['isFraud'].value_counts()
    non_fraudulent = counts.get(0, 0) 
    fraudulent = counts.get(1, 0) 
    return non_fraudulent, fraudulent

def get_average_transaction_amount_0(category):
    if category:
        filtered_df = df[(df['card6'] == category) & (df['isFraud'] == 0)]
    else:
        filtered_df = df[df['isFraud'] == 0]
    
    average_transactionamt = filtered_df['TransactionAmt'].mean()
    return average_transactionamt

def get_average_transaction_amount_1(category):
    if category:
        filtered_df = df[(df['card6'] == category) & (df['isFraud'] == 1)]
    else:
        filtered_df = df[df['isFraud'] == 1]
    
    average_transactionamt = filtered_df['TransactionAmt'].mean()
    return average_transactionamt



layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.Strong("Non-Fraudulent Transactions", className="small-text", style={'color': 'white', 'font-size': '14px', 'padding': '1px'})),
                    dbc.CardBody(id='card-no-fraudulent', className="mb-0", style={'background-color': '#0c1d44', 'color': 'white', 'text-align': 'center', 'font-size': '20px', 'padding': '1px'})  
                ], className="btn btn-light custom-btn m-1 text-white fw-bold text-color-custom bg-0c1d44")  
            ], md=2),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.Strong("Fraudulent Transactions", className="small-text", style={'color': 'white', 'font-size': '14px', 'padding': '1px'})),
                    dbc.CardBody(id='card-fraudulent', className="mb-0", style={'background-color': '#0c1d44', 'color': 'white', 'text-align': 'center', 'font-size': '20px', 'padding': '1px'})  
                ], className="btn btn-light custom-btn m-1 text-white fw-bold text-color-custom bg-0c1d44") 
            ], md=2),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.Strong("Average Amt of Fraud", className="small-text", style={'color': 'white', 'font-size': '14px', 'padding': '1px'})),
                    dbc.CardBody(id='card-average-transactionamt-1', className="mb-0", style={'background-color': '#0c1d44', 'color': 'white', 'text-align': 'center', 'font-size': '20px', 'padding': '1px'})
                ], className="btn btn-light custom-btn m-1 text-white fw-bold text-color-custom bg-0c1d44") 
            ], md=2),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.Strong("Average Amt of No Fraud", className="small-text", style={'color': 'white', 'font-size': '14px', 'padding': '1px'})),
                    dbc.CardBody(id='card-average-transactionamt-0', className="mb-0", style={'background-color': '#0c1d44', 'color': 'white', 'text-align': 'center', 'font-size': '20px', 'padding': '1px'})
                ], className="btn btn-light custom-btn m-1 text-white fw-bold text-color-custom bg-0c1d44") 
            ], md=2),
            dbc.Col([
                html.H2("Select card type", className="small-text", style={'color': 'white', 'font-size': '16px', 'background-color': '#0c1d44', 'padding': '10px', 'border-radius': '10px 5px 0 0', 'font-weight': 'bold'}),  # Aplicando estilos CSS al título
                dcc.Dropdown(
                    id='category-selector',
                    options=[{'label': category, 'value': category} for category in categorias],
                    value=None,
                    placeholder="Credit",
                    className='mb-0'
                )
            ], md=4)
        ])
    ], fluid=True, className='dash-container mb-0',  style={'background-color': 'transparent', 'marginBottom': '0px'}),
    dbc.Container([
        dbc.Row([
            dbc.Col(id='graphs-row', children=[], style={
                'display': 'flex',
                'flexWrap': 'wrap',
                'marginTop': 0
            }, md=8),
            dbc.Col([
                html.Div([
                    html.Img(src='/assets/images/hora_season.png', style={
                        'width': '100%', 
                        'marginBottom': '10px', 
                        'border-radius': '15px', 
                        'box-shadow': '0 6px 12px rgba(0, 0, 0, 0.9)'
                    })
                ], style={'text-align': 'center'})
            ], md=6),
            dbc.Col([
                html.Div([
                    html.Img(src='/assets/images/dia_season.png', style={
                        'width': '100%', 
                        'border-radius': '15px', 
                        'box-shadow': '0 6px 12px rgba(0, 0, 0, 0.9)'
                    })
                ], style={'text-align': 'center'})
            ], md=6)
        ], style={'display': 'flex', 'flexWrap': 'wrap', 'marginTop': 0})
    ], fluid=True, className='dash-container mb-0',  style={'background-color': 'transparent'})
])



@callback(
    [Output('card-no-fraudulent', 'children'),
     Output('card-fraudulent', 'children'),
     Output('card-average-transactionamt-1', 'children'),
     Output('card-average-transactionamt-0', 'children'),
     Output('graphs-row', 'children')],
    [Input('category-selector', 'value')]
)
def update_output(selected_category):
    figures = update_figures(selected_category)
    no_fraudulent, fraudulent = get_transaction_counts(selected_category)
    average_transactionamt_1 = get_average_transaction_amount_1(selected_category)
    average_transactionamt_0 = get_average_transaction_amount_0(selected_category)
    children = [
        dbc.Col(dcc.Graph(figure=fig), style={'padding': '10px'}, width=4)
        for fig in figures
    ]
    

    avg_transactionamt_1 = f"{average_transactionamt_1:,.2f}"
    avg_transactionamt_0 = f"{average_transactionamt_0:,.2f}"
    
    return f"{no_fraudulent:,}", f"{fraudulent:,}", avg_transactionamt_1, avg_transactionamt_0, children

