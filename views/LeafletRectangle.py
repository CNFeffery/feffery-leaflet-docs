import uuid
from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

import callbacks.LeafletRectangle
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
                            'title': 'LeafletRectangle 矩形'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在地图中渲染矩形。')
                    ]
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletRectangle(
                                    bounds={
                                        'minx': -5,
                                        'miny': -5,
                                        'maxx': 5,
                                        'maxy': 5
                                    }
                                )
                            ],
                            zoom=5,
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
        flc.LeafletRectangle(
            bounds={
                'minx': -5,
                'miny': -5,
                'maxx': 5,
                'maxy': 5
            }
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletRectangle(
                                    bounds={
                                        'minx': -5,
                                        'miny': -5,
                                        'maxx': 5,
                                        'maxy': 5
                                    },
                                    pathOptions={
                                        'color': 'red',
                                        'dashArray': '5, 2, 5'
                                    }
                                )
                            ],
                            zoom=5,
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
        flc.LeafletRectangle(
            bounds={
                'minx': -5,
                'miny': -5,
                'maxx': 5,
                'maxy': 5
            },
            pathOptions={
                'color': 'red',
                'dashArray': '5, 2, 5'
            }
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
                    id='自定义样式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletRectangle(
                                    id='rectangle-editable-demo',
                                    bounds={
                                        'minx': -5,
                                        'miny': -5,
                                        'maxx': 5,
                                        'maxy': 5
                                    },
                                    editable=True
                                )
                            ],
                            zoom=5,
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
                                'removalMode': False,
                                # 矩形要素的旋转操作会引发异常问题，请关闭
                                'rotateMode': False
                            },
                            style={
                                'height': 500
                            }
                        ),
                        html.Pre(
                            id='rectangle-editable-demo-output',
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
                                '为矩形组件设置参数',
                                fac.AntdText(
                                    'editable=True',
                                    code=True
                                ),
                                '后，可配合地图实例的地图编辑相关功能实现对矩形进行编辑、平移操作'
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
        flc.LeafletRectangle(
            id='rectangle-editable-demo',
            bounds={
                'minx': -5,
                'miny': -5,
                'maxx': 5,
                'maxy': 5
            },
            editable=True
        )
    ],
    zoom=5,
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
        'removalMode': False,
        # 矩形要素的旋转操作会引发异常问题，请关闭
        'rotateMode': False
    },
    style={
        'height': 500
    }
),
html.Pre(
    id='rectangle-editable-demo-output',
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
)

...

app.clientside_callback(
    '''( bounds ) => JSON.stringify(bounds, null, 4)''',
    Output('rectangle-editable-demo-output', 'children'),
    Input('rectangle-editable-demo', 'bounds')
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
                                flc.LeafletRectangle(
                                    id='rectangle-event-demo',
                                    bounds={
                                        'minx': -5,
                                        'miny': -5,
                                        'maxx': 5,
                                        'maxy': 5
                                    },
                                    editable=True
                                )
                            ],
                            zoom=5,
                            style={
                                'height': 500
                            }
                        ),
                        html.Pre(
                            id='rectangle-event-demo-output'
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
        flc.LeafletRectangle(
            id='rectangle-event-demo',
            bounds={
                'minx': -5,
                'miny': -5,
                'maxx': 5,
                'maxy': 5
            },
            editable=True
        )
    ],
    zoom=5,
    style={
        'height': 500
    }
),
html.Pre(
    id='rectangle-event-demo-output'
)

...

import json

...

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
            component_name='LeafletRectangle'
        )
    ],
    id=str(uuid.uuid4()),
    style={
        'display': 'flex'
    }
)
