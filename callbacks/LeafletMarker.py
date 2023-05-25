import json
from dash.dependencies import Input, Output

from server import app

app.clientside_callback(
    '''( position ) => JSON.stringify(position, null, 4)''',
    Output('marker-draggable-demo-output', 'children'),
    Input('marker-draggable-demo', 'position')
)

app.clientside_callback(
    '''( position ) => JSON.stringify(position, null, 4)''',
    Output('marker-editable-demo-output', 'children'),
    Input('marker-editable-demo', 'position')
)


@app.callback(
    Output('marker-event-demo-output', 'children'),
    [Input('marker-event-demo', 'nClicks'),
     Input('marker-event-demo', 'mouseOverCount')]
)
def marker_event_demo(nClicks, mouseOverCount):

    return json.dumps(
        {
            'nClicks': nClicks,
            'mouseOverCount': mouseOverCount
        },
        indent=4,
        ensure_ascii=False
    )