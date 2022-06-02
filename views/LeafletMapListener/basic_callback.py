import re
import json
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc
from dash.dependencies import Input, Output

from server import app

docs_content = fuc.FefferySplit(
    [
        fuc.FefferySplitPane(
            html.Div(
                [
                    flc.LeafletMap(
                        [
                            flc.LeafletTileLayer(),
                            flc.LeafletMapListener(
                                id='listener-callback',
                            )
                        ],
                        style={
                            'height': '70%'
                        }
                    ),

                    html.Div(
                        id='listener-callback-output',
                        style={
                            'height': '30%',
                            'overflowY': 'auto'
                        }
                    )
                ],
                style={
                    'height': '100%'
                }
            ),
            style={
                'height': '100%',
                'padding': '3px 0 3px 3px'
            }
        ),

        fuc.FefferySplitPane(
            fuc.FefferySplit(
                [
                    fuc.FefferySplitPane(
                        [
                            fac.AntdAffix(
                                fac.AntdParagraph(
                                    'LeafletMapListener参数说明',
                                    style={
                                        'fontSize': '20px',
                                        'borderLeft': '4px solid rgb(24, 144, 255)',
                                        'paddingLeft': '5px',
                                        'marginBottom': 0
                                    }
                                ),
                                offsetTop=0,
                                target='parameters-container'
                            ),
                            fac.AntdAccordion(
                                [
                                    fac.AntdAccordionItem(
                                        fmc.FefferyMarkdown(
                                            markdownStr=parameter
                                        ),
                                        title=re.findall('\*\*(.*?)：\*\*', parameter)[0],
                                        key=i
                                    )
                                    for i, parameter in enumerate(
                                    open('documents/LeafletMapListener.md', encoding='utf-8')
                                        .read()
                                        .split('---')
                                )
                                ],
                                accordion=False
                            )
                        ],
                        id='parameters-container',
                        style={
                            'overflowY': 'auto'
                        }
                    ),
                    fuc.FefferySplitPane(
                        [
                            fac.AntdAffix(
                                fac.AntdParagraph(
                                    '当前示例源码',
                                    style={
                                        'fontSize': '20px',
                                        'borderLeft': '4px solid rgb(24, 144, 255)',
                                        'paddingLeft': '5px',
                                        'marginBottom': 0
                                    }
                                ),
                                offsetTop=0,
                                target='demo-code-container'
                            ),
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
import json
from dash import html
import feffery_leaflet_components as flc

html.Div(
    [
        flc.LeafletMap(
            [
                flc.LeafletTileLayer(),
                flc.LeafletMapListener(
                    id='listener-callback',
                )
            ],
            style={
                'height': '70%'
            }
        ),

        html.Div(
            id='listener-callback-output',
            style={
                'height': '30%',
                'overflowY': 'auto'
            }
        )
    ],
    style={
        'height': '100%'
    }
)

...

@app.callback(
    Output('listener-callback-output', 'children'),
    [Input('listener-callback', '_center'),
     Input('listener-callback', '_zoom'),
     Input('listener-callback', '_clickedLatLng'),
     Input('listener-callback', '_bounds')]
)
def listener_callback(_center, _zoom, _clickedLatLng, _bounds):
    return html.Pre(
        json.dumps(
            {
                '_center': _center,
                '_zoom': _zoom,
                '_clickedLatLng': _clickedLatLng,
                '_bounds': _bounds
            },
            indent=4,
            ensure_ascii=False
        )
    )
''')
                        ],
                        id='demo-code-container',
                        style={
                            'overflowY': 'auto'
                        }
                    ),
                ],
                direction='vertical',
                sizes=[50, 50],
                gutterSize=10,
                style={
                    'height': '100%'
                }
            ),
            style={
                'height': '100%',
                'padding': '3px 3px 3px 0'
            }
        )
    ],
    id='LeafletMapListener-basic-callback-container',
    sizes=[60, 40],
    gutterSize=10,
    style={
        'height': '100%'
    }
)


@app.callback(
    Output('listener-callback-output', 'children'),
    [Input('listener-callback', '_center'),
     Input('listener-callback', '_zoom'),
     Input('listener-callback', '_clickedLatLng'),
     Input('listener-callback', '_bounds')]
)
def listener_callback(_center, _zoom, _clickedLatLng, _bounds):
    return html.Pre(
        json.dumps(
            {
                '_center': _center,
                '_zoom': _zoom,
                '_clickedLatLng': _clickedLatLng,
                '_bounds': _bounds
            },
            indent=4,
            ensure_ascii=False
        )
    )
