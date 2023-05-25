import uuid
from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

import callbacks.LeafletMarker
from .side_props import render_side_props_layout

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdBackTop(
                    duration=0.3
                ),

                fac.AntdBreadcrumb(
                    items=[
                        {
                            'title': '组件介绍'
                        },
                        {
                            'title': '矢量'
                        },
                        {
                            'title': 'LeafletMarker 标记'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在地图中渲染带图标的标记。')
                    ]
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletMarker(
                                    position={
                                        'lng': 0,
                                        'lat': 0
                                    }
                                )
                            ],
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletMarker(
            position={
                'lng': 0,
                'lat': 0
            }
        )
    ],
    style={
        'height': 500
    }
)
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletMarker(
                                    position={
                                        'lng': 0,
                                        'lat': 0
                                    },
                                    iconOptions={
                                        'iconUrl': 'assets/imgs/flc-logo.svg',
                                        'iconSize': [40, 40]
                                    }
                                )
                            ],
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '自定义图标',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletMarker(
            position={
                'lng': 0,
                'lat': 0
            },
            iconOptions={
                'iconUrl': 'assets/imgs/flc-logo.svg',
                'iconSize': [40, 40]
            }
        )
    ],
    style={
        'height': 500
    }
)
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='自定义图标',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletMarker(
                                    id='marker-draggable-demo',
                                    position={
                                        'lng': 0,
                                        'lat': 0
                                    },
                                    draggable=True
                                )
                            ],
                            style={
                                'height': 500
                            }
                        ),
                        html.Pre(
                            id='marker-draggable-demo-output'
                        ),

                        fac.AntdDivider(
                            '可拖拽',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletMarker(
            id='marker-draggable-demo',
            position={
                'lng': 0,
                'lat': 0
            },
            draggable=True
        )
    ],
    style={
        'height': 500
    }
),
html.Pre(
    id='marker-draggable-demo-output'
)

...

app.clientside_callback(
    '''( position ) => JSON.stringify(position, null, 4)''',
    Output('marker-draggable-demo-output', 'children'),
    Input('marker-draggable-demo', 'position')
)
"""
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='可拖拽',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletMarker(
                                    id='marker-editable-demo',
                                    position={
                                        'lng': 0,
                                        'lat': 0
                                    },
                                    editable=True
                                )
                            ],
                            editToolbar=True,
                            # 关闭其他无关地图编辑功能
                            editToolbarControlsOptions={
                                'drawMarker': False,
                                'drawCircleMarker': False,
                                'drawPolyline': False,
                                'drawRectangle': False,
                                'drawPolygon': False,
                                'drawCircle': False,
                                'drawText': False,
                                'editMode': False,
                                'removalMode': False,
                                'rotateMode': False
                            },
                            style={
                                'height': 500
                            }
                        ),
                        html.Pre(
                            id='marker-editable-demo-output'
                        ),

                        fac.AntdDivider(
                            '可编辑',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '为标记组件设置参数',
                                fac.AntdText(
                                    'editable=True',
                                    code=True
                                ),
                                '后，可配合地图实例的地图编辑相关功能实现对标记的拖拽'
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletMarker(
            id='marker-editable-demo',
            position={
                'lng': 0,
                'lat': 0
            },
            editable=True
        )
    ],
    editToolbar=True,
    # 关闭其他无关地图编辑功能
    editToolbarControlsOptions={
        'drawMarker': False,
        'drawCircleMarker': False,
        'drawPolyline': False,
        'drawRectangle': False,
        'drawPolygon': False,
        'drawCircle': False,
        'drawText': False,
        'editMode': False,
        'removalMode': False,
        'rotateMode': False
    },
    style={
        'height': 500
    }
),
html.Pre(
    id='marker-editable-demo-output'
)

...

app.clientside_callback(
    '''( position ) => JSON.stringify(position, null, 4)''',
    Output('marker-editable-demo-output', 'children'),
    Input('marker-editable-demo', 'position')
)
"""
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='可编辑',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletMarker(
                                    id='marker-event-demo',
                                    position={
                                        'lng': 0,
                                        'lat': 0
                                    }
                                )
                            ],
                            style={
                                'height': 500
                            }
                        ),
                        html.Pre(
                            id='marker-event-demo-output'
                        ),

                        fac.AntdDivider(
                            '鼠标事件监听',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletMarker(
            id='marker-event-demo',
            position={
                'lng': 0,
                'lat': 0
            }
        )
    ],
    style={
        'height': 500
    }
),
html.Pre(
    id='marker-event-demo-output'
)

...

import json

...

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
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='鼠标事件监听',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '基础使用', 'href': '#基础使用'},
                    {'title': '自定义图标', 'href': '#自定义图标'},
                    {'title': '可拖拽', 'href': '#可拖拽'},
                    {'title': '可编辑', 'href': '#可编辑'},
                    {'title': '鼠标事件监听', 'href': '#鼠标事件监听'},
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'padding': '25px'
            }
        ),
        # 侧边参数栏
        render_side_props_layout(
            component_name='LeafletMarker'
        )
    ],
    id=str(uuid.uuid4()),
    style={
        'display': 'flex'
    }
)
