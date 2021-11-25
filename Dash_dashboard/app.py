from dash import Dash
import dash_bootstrap_components as dbc
from model.classifier import PredictionCharges

app = Dash(__name__, 
           assets_folder="static/assets/css/", 
           external_stylesheets=[dbc.themes.GRID, dbc.themes.BOOTSTRAP]) 


app.title = "First app"

model = PredictionCharges()