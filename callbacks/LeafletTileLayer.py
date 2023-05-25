from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('tile-layer-basic-demo', 'url'),
    Output('tile-layer-basic-demo-current-url', 'children'),
    Input('tile-layer-basic-demo-switch-url', 'value')
)
def tile_layer_basic_demo_update_url(value):

    return value, value
