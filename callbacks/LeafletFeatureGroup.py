import json
import dash
import random
import feffery_leaflet_components as flc
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('feature-group-basic-demo', 'children'),
    [Input('feature-group-basic-demo-put', 'nClicks'),
     Input('feature-group-basic-demo-delete', 'nClicks')],
    prevent_initial_call=True
)
def feature_group_basic_demo(put, delete):

    if dash.ctx.triggered_id == 'feature-group-basic-demo-put':
        return [
            flc.LeafletCircleMarker(
                center={
                    'lng': i,
                    'lat': random.uniform(-3, 3)
                },
                pathOptions={
                    'color': 'red'
                }
            )
            for i in range(-1, 2)
        ]

    # 否则执行delete操作
    return []


@app.callback(
    [Output('feature-group-to-top-demo1', 'bringToFront'),
     Output('feature-group-to-top-demo2', 'bringToFront')],
    [Input('feature-group-to-top-demo1-update', 'nClicks'),
     Input('feature-group-to-top-demo2-update', 'nClicks')],
    prevent_initial_call=True
)
def feature_group_to_top_demo(update_blue, update_red):

    if dash.ctx.triggered_id == 'feature-group-to-top-demo1-update':
        return [True, dash.no_update]

    return [dash.no_update, True]


@app.callback(
    Output('feature-group-bounds-demo', 'children'),
    Input('feature-group-bounds-demo-update', 'nClicks')
)
def feature_group_bounds_demo(nClicks):

    return [
        flc.LeafletCircleMarker(
            center={
                'lng': random.uniform(-3, 3),
                'lat': random.uniform(-3, 3)
            }
        )
        for i in range(-1, 2)
    ]


@app.callback(
    Output('feature-group-bounds-demo-output', 'children'),
    Input('feature-group-bounds-demo', '_bounds')
)
def feature_group_bounds_demo_show_bounds(_bounds):

    return json.dumps(
        {
            '_bounds': _bounds
        },
        indent=4,
        ensure_ascii=True
    )
