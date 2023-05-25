import uuid
from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

import callbacks.LeafletPolygon
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
                            'title': 'LeafletPolygon 多边形'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在地图中渲染多边形。')
                    ]
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletPolygon(
                                    positions=[
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 3,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 3,
                                            'lat': 3
                                        },
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        }
                                    ]
                                )
                            ],
                            zoom=6,
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
        flc.LeafletPolygon(
            positions=[
                {
                    'lng': 0,
                    'lat': 0
                },
                {
                    'lng': 3,
                    'lat': 0
                },
                {
                    'lng': 3,
                    'lat': 3
                },
                {
                    'lng': 0,
                    'lat': 0
                }
            ]
        )
    ],
    zoom=6,
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
                                flc.LeafletPolygon(
                                    positions=[
                                        [
                                            [
                                                {
                                                    'lng': 4,
                                                    'lat': -4
                                                },
                                                {
                                                    'lng': 4,
                                                    'lat': -6
                                                },
                                                {
                                                    'lng': 6,
                                                    'lat': -6
                                                },
                                                {
                                                    'lng': 4,
                                                    'lat': -4
                                                },
                                            ]
                                        ],

                                        [
                                            [
                                                {
                                                    'lng': 4,
                                                    'lat': -8
                                                },
                                                {
                                                    'lng': 4,
                                                    'lat': -10
                                                },
                                                {
                                                    'lng': 6,
                                                    'lat': -10
                                                },
                                                {
                                                    'lng': 4,
                                                    'lat': -8
                                                },
                                            ]
                                        ]
                                    ]
                                )
                            ],
                            zoom=6,
                            center={
                                'lng': 4,
                                'lat': -8
                            },
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '多部件多边形',
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
        flc.LeafletPolygon(
            positions=[
                [
                    [
                        {
                            'lng': 4,
                            'lat': -4
                        },
                        {
                            'lng': 4,
                            'lat': -6
                        },
                        {
                            'lng': 6,
                            'lat': -6
                        },
                        {
                            'lng': 4,
                            'lat': -4
                        },
                    ]
                ],

                [
                    [
                        {
                            'lng': 4,
                            'lat': -8
                        },
                        {
                            'lng': 4,
                            'lat': -10
                        },
                        {
                            'lng': 6,
                            'lat': -10
                        },
                        {
                            'lng': 4,
                            'lat': -8
                        },
                    ]
                ]
            ]
        )
    ],
    zoom=6,
    center={
        'lng': 4,
        'lat': -8
    },
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
                    id='多部件多边形',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletPolygon(
                                    positions=[
                                        [
                                            {
                                                'lng': -4,
                                                'lat': -4
                                            },
                                            {
                                                'lng': 1,
                                                'lat': -4
                                            },
                                            {
                                                'lng': -1,
                                                'lat': -1
                                            },
                                            {
                                                'lng': -4,
                                                'lat': -4
                                            }
                                        ],
                                        [
                                            {
                                                'lng': -2,
                                                'lat': -3.5
                                            },
                                            {
                                                'lng': -1,
                                                'lat': -3.5
                                            },
                                            {
                                                'lng': -2,
                                                'lat': -2.5
                                            },
                                            {
                                                'lng': -2,
                                                'lat': -3.5
                                            }
                                        ]
                                    ]
                                )
                            ],
                            zoom=5,
                            center={
                                'lng': 0,
                                'lat': -2
                            },
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '有孔多边形',
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
        flc.LeafletPolygon(
            positions=[
                [
                    {
                        'lng': -4,
                        'lat': -4
                    },
                    {
                        'lng': 1,
                        'lat': -4
                    },
                    {
                        'lng': -1,
                        'lat': -1
                    },
                    {
                        'lng': -4,
                        'lat': -4
                    }
                ],
                [
                    {
                        'lng': -2,
                        'lat': -3.5
                    },
                    {
                        'lng': -1,
                        'lat': -3.5
                    },
                    {
                        'lng': -2,
                        'lat': -2.5
                    },
                    {
                        'lng': -2,
                        'lat': -3.5
                    }
                ]
            ]
        )
    ],
    zoom=5,
    center={
        'lng': 0,
        'lat': -2
    },
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
                    id='有孔多边形',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletPolygon(
                                    positions=[
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 3,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 3,
                                            'lat': 3
                                        },
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        }
                                    ],
                                    pathOptions={
                                        'color': 'black',
                                        'weight': 2,
                                        'dashArray': '5, 2, 5',
                                        'fillOpacity': 0.4,
                                        'fillColor': 'red'
                                    }
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '自定义样式',
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
        flc.LeafletPolygon(
            positions=[
                {
                    'lng': 0,
                    'lat': 0
                },
                {
                    'lng': 3,
                    'lat': 0
                },
                {
                    'lng': 3,
                    'lat': 3
                },
                {
                    'lng': 0,
                    'lat': 0
                }
            ],
            pathOptions={
                'color': 'black',
                'weight': 2,
                'dashArray': '5, 2, 5',
                'fillOpacity': 0.4,
                'fillColor': 'red'
            }
        )
    ],
    zoom=6,
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
                    id='自定义样式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletPolygon(
                                    id='polygon-editable-demo',
                                    positions=[
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 3,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 3,
                                            'lat': 3
                                        },
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        }
                                    ],
                                    editable=True
                                )
                            ],
                            zoom=6,
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
                                'removalMode': False
                            },
                            style={
                                'height': 500
                            }
                        ),

                        html.Pre(
                            id='polygon-editable-demo-output',
                            style={
                                'maxHeight': 300,
                                'overflowY': 'auto',
                                'background': '#f8f9fa'
                            }
                        ),

                        fac.AntdDivider(
                            '可编辑',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '为多边形组件设置参数',
                                fac.AntdText(
                                    'editable=True',
                                    code=True
                                ),
                                '后，可配合地图实例的地图编辑相关功能实现对多边形进行折点增加、折点编辑、平移、旋转操作'
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
        flc.LeafletPolygon(
            id='polygon-editable-demo',
            positions=[
                {
                    'lng': 0,
                    'lat': 0
                },
                {
                    'lng': 3,
                    'lat': 0
                },
                {
                    'lng': 3,
                    'lat': 3
                },
                {
                    'lng': 0,
                    'lat': 0
                }
            ],
            editable=True
        )
    ],
    zoom=6,
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
        'removalMode': False
    },
    style={
        'height': 500
    }
),

html.Pre(
    id='polygon-editable-demo-output',
    style={
        'maxHeight': 300,
        'overflowY': 'auto',
        'background': '#f8f9fa'
    }
)

...

app.clientside_callback(
    '''( positions ) => JSON.stringify(positions, null, 4)''',
    Output('polygon-editable-demo-output', 'children'),
    Input('polygon-editable-demo', 'positions')
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
                                flc.LeafletPolygon(
                                    id='polygon-event-demo',
                                    positions=[
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 3,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 3,
                                            'lat': 3
                                        },
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        }
                                    ]
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),
                        html.Pre(
                            id='polygon-event-demo-output'
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
        flc.LeafletPolygon(
            id='polygon-event-demo',
            positions=[
                {
                    'lng': 0,
                    'lat': 0
                },
                {
                    'lng': 3,
                    'lat': 0
                },
                {
                    'lng': 3,
                    'lat': 3
                },
                {
                    'lng': 0,
                    'lat': 0
                }
            ]
        )
    ],
    zoom=6,
    style={
        'height': 500
    }
),
html.Pre(
    id='polygon-event-demo-output'
)

...

import json

...

@app.callback(
    Output('polygon-event-demo-output', 'children'),
    [Input('polygon-event-demo', 'nClicks'),
     Input('polygon-event-demo', 'mouseOverCount')]
)
def polygon_event_demo(nClicks, mouseOverCount):

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
                    {'title': '多部件多边形', 'href': '#多部件多边形'},
                    {'title': '有孔多边形', 'href': '#有孔多边形'},
                    {'title': '自定义样式', 'href': '#自定义样式'},
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
            component_name='LeafletPolyline'
        )
    ],
    id=str(uuid.uuid4()),
    style={
        'display': 'flex'
    }
)
