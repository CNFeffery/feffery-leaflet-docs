from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

import callbacks.LeafletFeatureGroup
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
                            'title': '容器'
                        },
                        {
                            'title': 'LeafletFeatureGroup 要素组'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于充当若干要素组件的承载容器，并具有相关额外功能。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '填充要素',
                                    id='feature-group-basic-demo-put'
                                ),
                                fac.AntdButton(
                                    '移除要素',
                                    id='feature-group-basic-demo-delete'
                                )
                            ],
                            style={
                                'marginBottom': 5
                            }
                        ),
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletFeatureGroup(
                                    [
                                        flc.LeafletCircleMarker(
                                            center={
                                                'lng': i,
                                                'lat': 0
                                            }
                                        )
                                        for i in range(-1, 2)
                                    ]
                                ),
                                flc.LeafletFeatureGroup(
                                    id='feature-group-basic-demo'
                                )
                            ],
                            zoom=7,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    'LeafletFeatureGroup',
                                    strong=True
                                ),
                                '可用于嵌套若干要素类组件，适合在应用中控制向地图新增要素，或从地图中移除已有要素'
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
                                codeString='''
import random

...

fac.AntdSpace(
    [
        fac.AntdButton(
            '填充要素',
            id='feature-group-basic-demo-put'
        ),
        fac.AntdButton(
            '移除要素',
            id='feature-group-basic-demo-delete'
        )
    ],
    style={
        'marginBottom': 5
    }
),
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletFeatureGroup(
            [
                flc.LeafletCircleMarker(
                    center={
                        'lng': i,
                        'lat': 0
                    }
                )
                for i in range(-1, 2)
            ]
        ),
        flc.LeafletFeatureGroup(
            id='feature-group-basic-demo'
        )
    ],
    zoom=7,
    style={
        'height': 500
    }
)

...

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
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '置顶蓝色组',
                                    id='feature-group-to-top-demo1-update'
                                ),
                                fac.AntdButton(
                                    '置顶红色组',
                                    id='feature-group-to-top-demo2-update'
                                )
                            ],
                            style={
                                'marginBottom': 5
                            }
                        ),
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletFeatureGroup(
                                    [
                                        flc.LeafletCircleMarker(
                                            center={
                                                'lng': -1,
                                                'lat': 0
                                            },
                                            radius=200
                                        )
                                    ],
                                    id='feature-group-to-top-demo1'
                                ),
                                flc.LeafletFeatureGroup(
                                    [
                                        flc.LeafletCircleMarker(
                                            center={
                                                'lng': 1,
                                                'lat': 0
                                            },
                                            pathOptions={
                                                'color': 'red'
                                            },
                                            radius=200
                                        )
                                    ],
                                    id='feature-group-to-top-demo2'
                                )
                            ],
                            zoom=7,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '手动置顶要素组',
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
fac.AntdSpace(
    [
        fac.AntdButton(
            '置顶蓝色组',
            id='feature-group-to-top-demo1-update'
        ),
        fac.AntdButton(
            '置顶红色组',
            id='feature-group-to-top-demo2-update'
        )
    ],
    style={
        'marginBottom': 5
    }
),
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletFeatureGroup(
            [
                flc.LeafletCircleMarker(
                    center={
                        'lng': -1,
                        'lat': 0
                    },
                    radius=200
                )
            ],
            id='feature-group-to-top-demo1'
        ),
        flc.LeafletFeatureGroup(
            [
                flc.LeafletCircleMarker(
                    center={
                        'lng': 1,
                        'lat': 0
                    },
                    pathOptions={
                        'color': 'red'
                    },
                    radius=200
                )
            ],
            id='feature-group-to-top-demo2'
        )
    ],
    zoom=7,
    style={
        'height': 500
    }
)

...

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
                    id='手动置顶要素组',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdButton(
                            '随机刷新数据',
                            id='feature-group-bounds-demo-update',
                            style={
                                'marginBottom': 5
                            }
                        ),
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletFeatureGroup(
                                    id='feature-group-bounds-demo'
                                )
                            ],
                            zoom=7,
                            style={
                                'height': 500
                            }
                        ),
                        html.Pre(id='feature-group-bounds-demo-output'),

                        fac.AntdDivider(
                            '获取组内要素整体坐标范围',
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
fac.AntdButton(
    '随机刷新数据',
    id='feature-group-bounds-demo-update',
    style={
        'marginBottom': 5
    }
),
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletFeatureGroup(
            id='feature-group-bounds-demo'
        )
    ],
    zoom=7,
    style={
        'height': 500
    }
),
html.Pre(id='feature-group-bounds-demo-output')

...

import json
import random

...

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
                    id='获取组内要素整体坐标范围',
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
                    {'title': '手动置顶要素组', 'href': '#手动置顶要素组'},
                    {'title': '获取组内要素整体坐标范围', 'href': '#获取组内要素整体坐标范围'},
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
            component_name='LeafletFeatureGroup'
        )
    ],
    style={
        'display': 'flex'
    }
)
