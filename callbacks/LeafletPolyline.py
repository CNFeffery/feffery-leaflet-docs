import json
from dash.dependencies import Input, Output

from server import app


app.clientside_callback(
    '''( positions ) => JSON.stringify(positions, null, 4)''',
    Output('polyline-editable-demo-output', 'children'),
    Input('polyline-editable-demo', 'positions')
)


@app.callback(
    Output('polyline-event-demo-output', 'children'),
    [Input('polyline-event-demo', 'nClicks'),
     Input('polyline-event-demo', 'mouseOverCount')]
)
def polyline_event_demo(nClicks, mouseOverCount):

    return json.dumps(
        {
            'nClicks': nClicks,
            'mouseOverCount': mouseOverCount
        },
        indent=4,
        ensure_ascii=False
    )
