import json
from dash.dependencies import Input, Output

from server import app

app.clientside_callback(
    '''( radius, center ) => JSON.stringify({ center, radius }, null, 4)''',
    Output('circle-editable-demo-output', 'children'),
    Input('circle-editable-demo', 'center'),
    Input('circle-editable-demo', 'radius'),
)


@app.callback(
    Output('circle-event-demo-output', 'children'),
    [Input('circle-event-demo', 'nClicks'),
     Input('circle-event-demo', 'mouseOverCount')]
)
def circle_event_demo(nClicks, mouseOverCount):

    return json.dumps(
        {
            'nClicks': nClicks,
            'mouseOverCount': mouseOverCount
        },
        indent=4,
        ensure_ascii=False
    )
