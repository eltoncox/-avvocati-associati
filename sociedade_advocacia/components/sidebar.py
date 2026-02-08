import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from components import modal_novo_processo, modal_novo_advogado, modal_advogados
from app import app

# ========= Layout ========= #
layout = dbc.Container([
    modal_novo_processo.layout,
    modal_novo_advogado.layout,
    modal_advogados.layout,
    dbc.Container([
        dbc.Row([dbc.Col([html.H1("ASIMOV", style={'color': 'yellow'})])]),
        dbc.Row([dbc.Col([html.H3("ASSOCIATES", style={'color': 'white'})])]),
    ], style={'padding-top': '50px', 'margin-bottom': '100px'}, className='text-center'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dbc.Nav([
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), "\tINÍCIO"], href="/home", active=True, style={'text-align': 'left'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-plus-circle dbc'), "\tPROCESSOS"], id='processo_button', active=True, style={'text-align': 'left'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-user-plus dbc'), "\tADVOGADOS"], id='lawyers_button', active=True, style={'text-align': 'left'})),
            ], vertical="lg", pills=True, fill=True)
        ])
    ]),
], style={'height': '100vh', 'padding': '0px', 'position':'sticky', 'top': 0, 'background-color': '#232423'})


# ======= Callbacks ======== #

# Modal da LISTA (Cadastro de Advogados)
@app.callback(
    Output('modal_lawyers', "is_open"),
    Input('lawyers_button', 'n_clicks'),
    Input('quit_button', 'n_clicks'),
    Input('new_adv_button', 'n_clicks'),
    State('modal_lawyers', "is_open"),
    prevent_initial_call=True
)
def abrir_fechar_modal_lista(n_open, n_quit, n_new, is_open):
    trigger = dash.callback_context.triggered[0]["prop_id"].split(".")[0]

    if trigger == "lawyers_button":
        return True
    if trigger in ("quit_button", "new_adv_button"):
        return False

    return is_open


# Modal NOVO ADVOGADO
@app.callback(
    Output('modal_new_lawyer', "is_open"),
    Input('new_adv_button', 'n_clicks'),
    Input("cancel_button_novo_advogado", 'n_clicks'),
    State('modal_new_lawyer', "is_open"),
    prevent_initial_call=True
)
def abrir_fechar_modal_novo(n_new, n_cancel, is_open):
    trigger = dash.callback_context.triggered[0]["prop_id"].split(".")[0]

    if trigger == "new_adv_button":
        return True
    if trigger == "cancel_button_novo_advogado":
        return False

    return is_open
