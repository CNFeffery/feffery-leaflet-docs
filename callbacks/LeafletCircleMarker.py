import json
from dash.dependencies import Input, Output

from server import app


app.clientside_callback(
    '''( center ) => JSON.stringify(center, null, 4)''',
    Output('circle-marker-editable-demo-output', 'children'),
    Input('circle-marker-editable-demo', 'center')
)


@app.callback(
    Output('circle-marker-event-demo-output', 'children'),
    [Input('circle-marker-event-demo', 'nClicks'),
     Input('circle-marker-event-demo', 'mouseOverCount')]
)
def circle_marker_event_demo(nClicks, mouseOverCount):

    return json.dumps(
        {
            'nClicks': nClicks,
            'mouseOverCount': mouseOverCount
        },
        indent=4,
        ensure_ascii=False
    )
