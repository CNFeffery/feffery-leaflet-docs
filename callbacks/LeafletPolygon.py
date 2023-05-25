import json
from dash.dependencies import Input, Output

from server import app


app.clientside_callback(
    '''( positions ) => JSON.stringify(positions, null, 4)''',
    Output('polygon-editable-demo-output', 'children'),
    Input('polygon-editable-demo', 'positions')
)


@app.callback(
    Output('polygon-event-demo-output', 'children'),
    [Input('polygon-event-demo', 'nClicks'),
     Input('polygon-event-demo', 'mouseOverCount')]
)
def polygon_event_demo(nClicks, mouseOverCount):

    return json.dumps(
        {
            'nClicks': nClicks,
            'mouseOverCount': mouseOverCount
        },
        indent=4,
        ensure_ascii=False
    )
