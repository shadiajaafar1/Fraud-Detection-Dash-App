import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import os

# Seleccionar el tema deseado de Bootstrap
app = dash.Dash(__name__, pages_folder="pages", use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server
# Cambiar el color de fondo y otros estilos
app.layout = html.Div([
    html.Div(
        [
            # Estilo para el título "Fraud Transactions Analysis"
             html.Img(src="assets\images\Imagen1.png", style={'height': '150px', 'width': '300px', 'margin-right': '20px'}),

            html.Div(
                children=[
                    # Estilo para el nombre de la página
                    dcc.Link(
                        page["name"],
                        href=page["relative_path"],
                        className="btn btn-light custom-btn m-1 text-white fw-bold text-color-custom bg-3F527E",
                        style={'font-size': '25px'} ,
                    )
                    for page in dash.page_registry.values()
                ],
                className="d-flex align-items-center"
            ),
        ],
                className="d-flex justify-content-between align-items-center p-3",  # Removed bg-3F527E class here as well

        style={'flexWrap': 'nowrap'}
    ),
    dash.page_container
], className="container-fluid p-3")

if __name__ == "__main__":
    app.run_server(debug=True)
