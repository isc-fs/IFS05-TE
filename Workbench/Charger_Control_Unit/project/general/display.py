# Libraries for Display
from collections import deque
from turtle import update
import dash
import pandas as pd
from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from dash.dependencies import Input, Output
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import numpy
from sqlalchemy import true, values
from classes import bms_class

colors = {
'background': '#111111',
'text': '#7FDBFF'
}
celdas = []
matrixes=[]

numCells = bms_class.BMS_CLASS.getNumCells()
for i in range(0, numCells):
    celda = str(i+1)
    celdas.append(celda)
celdas.reverse()

### INICIALIZAR APP
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
### EMPEZA LAYOUT
app.layout = html.Div( style={'backgroundColor': colors['background']},children=[
    
    html.Div([
        dcc.Graph(id='live-update-graph-tempBateries')
    ], style= {'width': '100%','width': '50%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='live-update-graph-tensionBateries')
    ], style= {'width': '100%','width': '50%', 'display': 'inline-block'}),


    dbc.Modal(  #ERROR WARNING
    [
        dbc.ModalHeader("Error"),
        dbc.ModalBody(id="update-error"),
        dbc.ModalFooter(
            dbc.Button("Close", id = "close", className="ml-auto",n_clicks=0),
        ),
        ],
        id = 'modal',
        is_open= False,
        backdrop=False,
        fade=True

    ),


    html.Div([      #ACTUALIZAR CADA SEGUNDO: NECESARIO EN CADA APP
        html.Div(id='live-update-text'),
        dcc.Interval(
            id='interval-component',
            interval=2*1000, # in milliseconds
            n_intervals=0            
            )
        ])
])

#TEMPERATURES
@app.callback(Output('live-update-graph-tempBateries', 'figure'),
            [Input('interval-component', 'n_intervals'), Input('modal', 'is_open')])
def update_graph_live(n, is_open):
    global matrixes                                 ##VARIABLE MATRIX ES UNA VARIABLE GLOBAL
    matrixes=bms_class.BMS_CLASS.getMatrixes()      ##SE OBTIENE DE BMS_CLASS
    temp=matrixes[0]                                ##SE OBTIENE TEMP
    if is_open==False:                              ##NO HA HABIDO ERROR POR AHORA
        df = pd.DataFrame(temp)                     ##SE OBTIENE DATAFRAME
        df_invert = df[::-1].reset_index(drop=True) ##SE INVIERTE DATFARAME (ESTÉTICA)
        df_invert.index = celdas                    ##SE OTORGA INDEX A DATAFRAME
        fig = px.imshow(df_invert, color_continuous_scale='reds') ##TEMPERATURAS EN ESCALA DE ROJOS
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'],
            title='Temperaturas de las celdas de las baterías',
            height=700,
            width=900,
            xaxis_title="Baterías",
            yaxis_title="Celdas"

        )
        return fig
    else:                                      ##MODAL ABIERTO->HAY ERROR
        fig=px.imshow(numpy.empty)
        return fig

###TENSIONES
@app.callback(Output('live-update-graph-tensionBateries', 'figure'),
            [Input('interval-component', 'n_intervals'), Input('modal', 'is_open')])
def update_graph_live(n, is_open):
    tens=matrixes[1]
    if is_open==False:
        df = pd.DataFrame(tens)
        df_invert = df[::-1].reset_index(drop=True)
        df_invert.index = celdas
        fig = px.imshow(df_invert, color_continuous_scale='algae')
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'],
            title='Tensiones de las celdas de las baterías',
            height=700,
            width=900,
            xaxis_title="Baterías",
            yaxis_title="Celdas"
        )
        return fig
    else:
        fig=px.imshow(numpy.empty)
        return fig


@app.callback(
    [Output('update-error', 'children'), Output('modal', 'is_open'), Output('close','n_clicks')],
    [Input('interval-component', 'n_intervals'), Input('close','n_clicks'),Input('modal', 'is_open')])

def error_update(n1, n2, is_open):
    error_temp=matrixes[2]
    error_tension=matrixes[3]
    msj=""
    if n2:                      ##SI SE PULSA PARA QUE SE CIERRE EL MODAL, IS_OPEN PASA A SER FALSE Y SE CIERRA
        print("n2")
        print(n2)
        is_open=False
        n2=0
        return html.Span(), is_open, n2


    for can in error_temp.keys():
        for id in range(0,numCells):
            if error_temp[can][id]==1:
                is_open=True              ##SI HAY ERROR->SE ABRE MODAL
                return html.Span('Temperatura de {} en módulo: {}, sensor: {}'.format(matrixes[0][can][id], int(can), id)), is_open, n2
        
            if error_tension[can][id]==1:
                is_open=True              ##SI HAY ERROR->SE ABRE MODAL
                return html.Span('Tensión de {} en módulo: {}, sensor: {}'.format(matrixes[1][can][id], int(can), id)), is_open, n2


