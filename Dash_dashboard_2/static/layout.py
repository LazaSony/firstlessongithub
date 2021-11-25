from app import app,sql
from dash import dcc,html
from dash_bootstrap_components import Container, Row, Col
from dash.dependencies import Input, Output, State
import dash_daq as daq
import plotly.express as px
import pandas as pd
import dash_table as dt

layout = Container([
    Row([
        # LEFT SIDE
        Col([
            # INPUTS - INSERT  
            Row([
                
            ]),
            # TABLE - CONTROLS
            Row([
                Col([
                    dcc.Dropdown(
                        id='dropdown-table',
                        options=[
                            {'label': 'Airlines', 'value': 'airlines'},
                            {'label': 'Airports', 'value': 'airports'},
                            {'label': 'Routes', 'value': 'routes'}
                        ],
                        value='airlines',
                        searchable=False,
                    ), 
                ],
                    width=12
                )
            ]),
            # TABLE
            Row([
                Col([
                    dt.DataTable(
                        id='my-table', 
                    ),    
                ],
                    width=12
                )
            ]),

        ], 
            width=8
        ),
        # RIGHT SIDE
        Col([
            # GRAPH
            Row([
                Col([

                ],
                    width=12
                )
            ]),
            # GRAPH - CONTROLS
            Row([
                Col([
                    
                ],
                    width=12
                )
            ])
        ],
            width=4
        )

    ])


    ]
)


# table - display output based on selected dropdown

# input fields for database table insert

# one interactive graph




@app.callback(
    [
        Output('my-table', 'columns'),
        Output('my-table', 'data')
    ],
    Input('dropdown-table', 'value')
)
def select_table(dropdown_selection):
    if dropdown_selection == "airlines":
        df=sql.select_all_airlines() 
    elif dropdown_selection == "airports":
        df=sql.select_all_airports() 
    elif dropdown_selection == "routes":
        df=sql.select_all_routes
    cols = [{"name": i, "id": i} for i in df.columns]
    data = df.to_dict(orient='records')
    return cols, data