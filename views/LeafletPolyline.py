import uuid
from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

import callbacks.LeafletPolyline
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
                            'title': 'LeafletPolyline 折线'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在地图中渲染折线。')
                    ]
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletPolyline(
                                    positions=[
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 1,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 1,
                                            'lat': 1
                                        },
                                        {
                                            'lng': 2,
                                            'lat': 1
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
        flc.LeafletPolyline(
            positions=[
                {
                    'lng': 0,
                    'lat': 0
                },
                {
                    'lng': 1,
                    'lat': 0
                },
                {
                    'lng': 1,
                    'lat': 1
                },
                {
                    'lng': 2,
                    'lat': 1
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
                                flc.LeafletPolyline(
                                    positions=[
                                        [
                                            {
                                                'lng': 0+i,
                                                'lat': 0+i
                                            },
                                            {
                                                'lng': 1+i,
                                                'lat': 0+i
                                            },
                                            {
                                                'lng': 1+i,
                                                'lat': 1+i
                                            },
                                            {
                                                'lng': 2+i,
                                                'lat': 1+i
                                            }
                                        ]
                                        for i in range(-10, 10, 2)
                                    ]
                                )
                            ],
                            zoom=5,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '多部件折线',
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
        flc.LeafletPolyline(
            positions=[
                [
                    {
                        'lng': 0+i,
                        'lat': 0+i
                    },
                    {
                        'lng': 1+i,
                        'lat': 0+i
                    },
                    {
                        'lng': 1+i,
                        'lat': 1+i
                    },
                    {
                        'lng': 2+i,
                        'lat': 1+i
                    }
                ]
                for i in range(-10, 10, 2)
            ]
        )
    ],
    zoom=5,
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
                    id='多部件折线',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletPolyline(
                                    positions=[
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 1,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 1,
                                            'lat': 1
                                        },
                                        {
                                            'lng': 2,
                                            'lat': 1
                                        }
                                    ],
                                    pathOptions={
                                        'color': 'red',
                                        'dashArray': '5, 2, 5'
                                    }
                                )
                            ],
                            zoom=7,
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
        flc.LeafletPolyline(
            positions=[
                {
                    'lng': 0,
                    'lat': 0
                },
                {
                    'lng': 1,
                    'lat': 0
                },
                {
                    'lng': 1,
                    'lat': 1
                },
                {
                    'lng': 2,
                    'lat': 1
                }
            ],
            pathOptions={
                'color': 'red',
                'dashArray': '5, 2, 5'
            }
        )
    ],
    zoom=7,
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
                                flc.LeafletPolyline(
                                    positions=[
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 1,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 1,
                                            'lat': 1
                                        },
                                        {
                                            'lng': 2,
                                            'lat': 1
                                        }
                                    ],
                                    arrowheads=True
                                ),

                                flc.LeafletPolyline(
                                    positions=[
                                        {
                                            'lng': 0-2,
                                            'lat': 0-2
                                        },
                                        {
                                            'lng': 1-2,
                                            'lat': 0-2
                                        },
                                        {
                                            'lng': 1-2,
                                            'lat': 1-2
                                        },
                                        {
                                            'lng': 2-2,
                                            'lat': 1-2
                                        }
                                    ],
                                    arrowheads={
                                        'fill': True,
                                        'frequency': '100px'
                                    },
                                    arrowheadsPathOptions={
                                        'color': 'red'
                                    },
                                    pathOptions={
                                        'color': 'red',
                                        'opacity': 0.4
                                    }
                                )
                            ],
                            zoom=7,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '添加箭头',
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
        flc.LeafletPolyline(
            positions=[
                {
                    'lng': 0,
                    'lat': 0
                },
                {
                    'lng': 1,
                    'lat': 0
                },
                {
                    'lng': 1,
                    'lat': 1
                },
                {
                    'lng': 2,
                    'lat': 1
                }
            ],
            arrowheads=True
        ),

        flc.LeafletPolyline(
            positions=[
                {
                    'lng': 0-2,
                    'lat': 0-2
                },
                {
                    'lng': 1-2,
                    'lat': 0-2
                },
                {
                    'lng': 1-2,
                    'lat': 1-2
                },
                {
                    'lng': 2-2,
                    'lat': 1-2
                }
            ],
            arrowheads={
                'fill': True,
                'frequency': '100px'
            },
            arrowheadsPathOptions={
                'color': 'red'
            },
            pathOptions={
                'color': 'red',
                'opacity': 0.4
            }
        )
    ],
    zoom=7,
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
                    id='添加箭头',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletPolyline(
                                    id='polyline-editable-demo',
                                    positions=[
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 1,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 1,
                                            'lat': 1
                                        },
                                        {
                                            'lng': 2,
                                            'lat': 1
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
                            id='polyline-editable-demo-output',
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
                                '为折线组件设置参数',
                                fac.AntdText(
                                    'editable=True',
                                    code=True
                                ),
                                '后，可配合地图实例的地图编辑相关功能实现对折线进行折点增加、折点编辑、折线平移、折线旋转等操作'
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
        flc.LeafletPolyline(
            id='polyline-editable-demo',
            positions=[
                {
                    'lng': 0,
                    'lat': 0
                },
                {
                    'lng': 1,
                    'lat': 0
                },
                {
                    'lng': 1,
                    'lat': 1
                },
                {
                    'lng': 2,
                    'lat': 1
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
    id='polyline-editable-demo-output',
    style={
        'maxHeight': 300,
        'overflowY': 'auto',
        'background': '#f8f9fa'
    }
)

...

app.clientside_callback(
    '''( positions ) => JSON.stringify(positions, null, 4)''',
    Output('polyline-editable-demo-output', 'children'),
    Input('polyline-editable-demo', 'positions')
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
                                flc.LeafletPolyline(
                                    id='polyline-event-demo',
                                    positions=[
                                        {
                                            'lng': 0,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 1,
                                            'lat': 0
                                        },
                                        {
                                            'lng': 1,
                                            'lat': 1
                                        },
                                        {
                                            'lng': 2,
                                            'lat': 1
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
                            id='polyline-event-demo-output'
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
        flc.LeafletPolyline(
            id='polyline-event-demo',
            positions=[
                {
                    'lng': 0,
                    'lat': 0
                },
                {
                    'lng': 1,
                    'lat': 0
                },
                {
                    'lng': 1,
                    'lat': 1
                },
                {
                    'lng': 2,
                    'lat': 1
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
    id='polyline-event-demo-output'
)

...

import json

...

@app.callback(
    Output('polyline-event-demo-output', 'children'),
    [Input('polyline-event-demo', 'nClicks'),
     Input('polyline-event-demo', 'mouseOverCount')]
)
def polyline_event_demo(nClicks, mouseOverCount):

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
                    {'title': '多部件折线', 'href': '#多部件折线'},
                    {'title': '自定义样式', 'href': '#自定义样式'},
                    {'title': '添加箭头', 'href': '#添加箭头'},
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
