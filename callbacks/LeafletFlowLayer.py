import random
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('flow-layer-data-update-demo', 'flowData'),
    Input('flow-layer-data-update-demo-trigger', 'nClicks')
)
def flow_layer_update_data_demo(nClicks):

    random_points = [
        (random.uniform(90, 130), random.uniform(20, 40))
        for i in range(5)
    ]

    return [
        {
            'from': {
                'lng': point1[0],
                'lat': point1[1]
            },
            'to': {
                'lng': point2[0],
                'lat': point2[1]
            },
            'labels': {
                'from': f'地点{idx1}',
                'to': f'地点{idx2}'
            }
        }
        for idx2, point2 in enumerate(random_points)
        for idx1, point1 in enumerate(random_points)
        if idx1 != idx2
    ]
