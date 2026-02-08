import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from dash import dash_table
from dash.dash_table.Format import Group

from app import app
from components import home

# ======== Layout ========= #
layout = dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Cadastro de Advogados")),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        html.Div(id='table_adv', className="dbc"),
                    ]),
                ])
            ]),
            dbc.ModalFooter([
                dbc.Button("Sair", id="quit_button", color="danger"),
                dbc.Button("Novo", id="new_adv_button", color="success")
            ])
        ], id="modal_lawyers", size="lg", is_open=False)
            


# ====== Callbacks ======= #
# Tabela com os advogados da empresa
@app.callback(
    Output('table_adv', 'children'),
    Input('store_adv', 'data')
    # Input(ThemeChangerAIO.ids.radio("theme"), "value")]
)
def table(data):
    df = pd.DataFrame(data)

    df = df.fillna('-')
    return [dash_table.DataTable(
        id='datatable',
        columns = [{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        filter_action="native",    
        sort_action="native",       
        sort_mode="single", 
        page_size=10,            
        page_current=0)]


from dash.exceptions import PreventUpdate
import dash  # precisa disso para callback_context

@app.callback(
    Output("div_erro2", "children", allow_duplicate=True),
    Output("div_erro2", "style", allow_duplicate=True),
    Input("new_adv_button", "n_clicks"),        # quando clica em NOVO
    Input("modal_new_lawyer", "is_open"),       # quando o modal abre
    prevent_initial_call=True
)
def limpar_mensagem_ao_abrir(n_new, is_open):
    trigger = dash.callback_context.triggered[0]["prop_id"].split(".")[0]

    # limpa quando clicar em NOVO, ou quando o modal acabou de abrir
    if trigger == "new_adv_button" or is_open:
        return "", {}

    raise PreventUpdate
