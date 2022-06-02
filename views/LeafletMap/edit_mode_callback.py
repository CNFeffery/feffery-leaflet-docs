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
                            flc.LeafletTileLayer()
                        ],
                        id='edit-mode-callback-map',
                        editToolbar=True,
                        editToolbarControlsOptions={
                            'cutPolygon': True
                        },
                        maxDrawnShapes=5,
                        style={
                            'height': '70%'
                        }
                    ),

                    html.Div(
                        html.Div(
                            fac.AntdEmpty(
                                description='请先在地图上绘制矢量要素'
                            ),
                            style={
                                'height': '100%',
                                'alignItems': 'center',
                                'display': 'flex',
                                'justifyContent': 'center'
                            }
                        ),
                        id='edit-mode-callback-output',
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
                                    'LeafletMap参数说明',
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
                                    open('documents/LeafletMap.md', encoding='utf-8')
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
import feffery_antd_components as fac
import feffery_leaflet_components as flc

html.Div(
    [
        flc.LeafletMap(
            [
                flc.LeafletTileLayer()
            ],
            id='edit-mode-callback-map',
            editToolbar=True,
            editToolbarControlsOptions={
                'cutPolygon': True
            },
            maxDrawnShapes=5,
            style={
                'height': '70%'
            }
        ),

        html.Div(
            html.Div(
                fac.AntdEmpty(
                    description='请先在地图上绘制矢量要素'
                ),
                style={
                    'height': '100%',
                    'alignItems': 'center',
                    'display': 'flex',
                    'justifyContent': 'center'
                }
            ),
            id='edit-mode-callback-output',
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
    Output('edit-mode-callback-output', 'children'),
    Input('edit-mode-callback-map', '_drawnShapes'),
    prevent_initial_call=True
)
def edit_mode_callback(_drawnShapes):
    return html.Pre(
        json.dumps(_drawnShapes, indent=4, ensure_ascii=False)
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
    id='LeafletMap-edit-mode-callback-container',
    sizes=[60, 40],
    gutterSize=10,
    style={
        'height': '100%'
    }
)


@app.callback(
    Output('edit-mode-callback-output', 'children'),
    Input('edit-mode-callback-map', '_drawnShapes'),
    prevent_initial_call=True
)
def edit_mode_callback(_drawnShapes):
    return html.Pre(
        json.dumps(_drawnShapes, indent=4, ensure_ascii=False)
    )
