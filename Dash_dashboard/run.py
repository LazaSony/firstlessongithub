from config import PRODUCTION
from app import app
from static.layout import layout

app.layout = layout

if __name__ == "__main__":

    if PRODUCTION:
        app.run_server(debug=False,  port = 8053)
    else:
        app.run_server(debug=True, use_reloader=True,  port = 8053)