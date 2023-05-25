import json
from dash.dependencies import Input, Output

from server import app


app.clientside_callback(
    '''( selectedFeatureIds ) => JSON.stringify({ selectedFeatureIds }, null, 4)''',
    Output('geojson-selectable-single-demo-output', 'children'),
    Input('geojson-selectable-single-demo', 'selectedFeatureIds')
)


app.clientside_callback(
    '''( selectedFeatureIds ) => JSON.stringify({ selectedFeatureIds }, null, 4)''',
    Output('geojson-selectable-multiple-demo-output', 'children'),
    Input('geojson-selectable-multiple-demo', 'selectedFeatureIds')
)

app.clientside_callback(
    '''( selectedFeatureIds ) => JSON.stringify({ selectedFeatureIds }, null, 4)''',
    Output('geojson-selectable-multiple-lasso-demo-output', 'children'),
    Input('geojson-selectable-multiple-lasso-demo', 'selectedFeatureIds')
)

app.clientside_callback(
    '''( _clickedFeature, _hoveredFeature ) => JSON.stringify({ _clickedFeature, _hoveredFeature }, null, 4)''',
    Output('geojson-event-demo-output', 'children'),
    [Input('geojson-event-demo', '_clickedFeature'),
     Input('geojson-event-demo', '_hoveredFeature')]
)
