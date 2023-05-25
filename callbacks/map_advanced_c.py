from dash.dependencies import Input, Output

from server import app


app.clientside_callback(
    '''( _drawnShapes ) => JSON.stringify(_drawnShapes, null, 4)''',
    Output('leaflet-map-edit-demo-output', 'children'),
    Input('leaflet-map-edit-demo', '_drawnShapes'),
    prevent_initial_call=True
)
