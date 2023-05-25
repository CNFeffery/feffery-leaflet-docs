import json
from dash.dependencies import Input, Output

from server import app

app.clientside_callback(
    '''( bounds ) => JSON.stringify(bounds, null, 4)''',
    Output('rectangle-editable-demo-output', 'children'),
    Input('rectangle-editable-demo', 'bounds')
)


@app.callback(
    Output('rectangle-event-demo-output', 'children'),
    [Input('rectangle-event-demo', 'nClicks'),
     Input('rectangle-event-demo', 'mouseOverCount')]
)
def rectangle_event_demo(nClicks, mouseOverCount):

    return json.dumps(
        {
            'nClicks': nClicks,
            'mouseOverCount': mouseOverCount
        },
        indent=4,
        ensure_ascii=False
    )
