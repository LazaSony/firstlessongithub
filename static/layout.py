from app import app, model

from dash import dcc,html
from dash_bootstrap_components import Container, Row, Col
from dash.dependencies import Input, Output, State
import dash_daq as daq
import plotly.express as px
import pandas as pd

layout = Container([
    Row([
        Col([
            # INPUTS
            Row([
                Col(["Age",
                    daq.NumericInput(
                        min=0,
                        max=100,
                        value=20,
                        id="input-age"
                    )
                ],
                    width=2,
                ),    
                Col(["Sex",
                    dcc.RadioItems(
                        options=[
                            {'label': 'M', 'value': "male"},
                            {'label': 'F', 'value': "female"},
                        ],
                        id="input-sex"
                    ),
                ],
                    width=2,
                ),   
                Col(["BMI",
                    dcc.Input(
                        placeholder='Enter BMI...',
                        type='number',
                        value=30.6,
                        min=10,
                        max=55,
                        id="input-bmi"
                    )
                ],
                    width=2,
                ),
                Col(["Children",
                    dcc.Slider(
                        min=0,
                        max=6,
                        marks={i: f'{i} children' for i in range(6)},
                        value=0,
                        id="input-children"
                    )
                ],
                    width=2
                ),
                Col([
                    "Smoker",
                    dcc.RadioItems(
                        options=[
                            {'label': 'Yes', 'value': "yes"},
                            {'label': 'No', 'value': "no"},
                        ],
                        value='no',
                        id="input-smoker"
                    ),  
                ],
                    width=2, 
                ),
                Col([
                    dcc.Dropdown(
                        options=[
                            {'label': 'South-West', 'value': 'southwest'},
                            {'label': 'South-East', 'value': 'southeast'},
                            {'label': 'North-West', 'value': 'northwest'},
                            {'label': 'North-East', 'value': 'northeast'}
                        ],
                        placeholder="Select a region",
                        id="input-region"
                    )
                ],
                    width=2
                ),
            ]),
            # SUBMIT
            Row([
                Col([
                    html.Button('Submit', id='submit-val', n_clicks=0),
                ],
                    width=12
                )
            ]),
            # OUTPUT 
            Row([ 
                Col([
                    html.Div(id='output-result',
                             children='Enter a value and press submit')
                
                ],
                    width=12
                )
            ])
        ], 
        width=8, style={"background-color":"orange"}
        ),
        # RIGHT col
        Col([
            Row([
                Col(["Charges plot",
                    dcc.Graph(id='plot-charges'),
                ],
                    width=12
                )
            ]),
            Row([
                Col(["BMI plot",
                    dcc.Graph(id='plot-bmi'),
                ],
                    width=12
                )
            ]),
            Row([
                Col(["Children plot",
                    dcc.Graph(id='plot-children'),
                ],
                    width=12
                )
            ]),
            Row([
                Col(["Age input",
                    dcc.RangeSlider(
                        min=0,
                        max=100,
                        marks={
                            0: '0',
                            10: '10 ',
                            20: '20',
                            30: '30',
                            40: '40',
                            50: '50',
                            60: '60',
                            70: '70',
                            80: '80',
                            90: '90',
                            100: '100 years'
                        },
                        value=[0, 20],
                        allowCross=False,
                        id="graph-input-age"
                    )
                ],
                    width=12
                )
            ]),
            Row([
                Col(["Sex",
                    dcc.RadioItems(
                        options=[
                            {'label': 'M', 'value': "male"},
                            {'label': 'F', 'value': "female"},
                        ],
                        id="graph-input-sex",
                        value='male'
                    ),
                ],
                    width=12
                )
            ]),
            Row([
                Col(["Region input",
                    dcc.Dropdown(
                        options=[
                            {'label': 'South-West', 'value': 'southwest'},
                            {'label': 'South-East', 'value': 'southeast'},
                            {'label': 'North-West', 'value': 'northwest'},
                            {'label': 'North-East', 'value': 'northeast'}
                        ],
                        placeholder="Select a region",
                        value='southwest',
                        id="graph-input-region"
                    )
                ],
                    width=12
                )
            ]),
        ],
            width=4, 
        )
    ], 
        id = "right-col-id",
        className="right-col-class-name"
    )
    ], 
    style={"background-color":"red"}
)


@app.callback(
    Output("output-result", "children"),
    Input("submit-val", "n_clicks"),
    [
        State("input-age", "value"),
        State("input-sex", "value"),
        State("input-bmi", "value"),
        State("input-children", "value"),
        State("input-smoker", "value"),
        State("input-region", "value"),
    ]
)
def sumbit_results_for_prediction(n_clicks, age, sex, bmi, children, smoker, region):

    if all([sex, region]):
        response = model.predict([age, sex, bmi, children, smoker, region])
    else:
        response = "Please fill all required input fields:"
        if not sex:
            response += " sex"
        if not region:
            response += " region"
    return response



@app.callback(
    [
        Output("plot-charges", "figure"),
        Output("plot-bmi", "figure"),
        Output("plot-children", "figure")
    ],
    [
        Input("graph-input-age", "value"),
        Input("graph-input-sex", "value"),
        Input("graph-input-region", "value") 
    ]
)

def redraw_graphs(age, sex, region):
    age_min, age_max = age[0], age[1]
    df = pd.read_csv("data\insurance.csv")
    df_filtered = df[(df["age"].between(age_min, age_max)) & (df["region"] == region) & (df["sex"] == sex)]
    
    

    
    fig_charges = px.histogram(df_filtered, x="charges",width=300, height=200)
    fig_bmi = px.histogram(df_filtered, x="bmi",width=300, height=200)
    fig_children = px.histogram(df_filtered, x="children",width=300, height=200)

    fig_charges['layout'].update(margin=dict(l=0,r=0,b=0,t=0))
    fig_bmi['layout'].update(margin=dict(l=0,r=0,b=0,t=0))
    fig_children['layout'].update(margin=dict(l=0,r=0,b=0,t=0))
    return fig_charges,fig_bmi,fig_children