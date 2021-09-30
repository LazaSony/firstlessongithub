import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),
    html.Div(id='my-output2'),

])


@app.callback(
    [
        Output(component_id='my-output', component_property='children'),
        Output(component_id='my-output2', component_property='children'),
    ],
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    my_output_1 = input_value.lowercase()
    my_output_2 = input_value.uppercase()
    return my_output_1, my_output_2


if __name__ == '__main__':
    app.run_server(debug=True)