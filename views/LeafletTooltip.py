from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

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
                            'title': '附加内容'
                        },
                        {
                            'title': 'LeafletTooltip 提示框'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　用于为矢量图层中各单体要素组件添加额外的轻量信息提示内容，通常在用户鼠标移入对应要素后展开。'
                        )
                    ]
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletCircleMarker(
                                    flc.LeafletTooltip(
                                        fac.AntdText(
                                            'tooltip示例内容',
                                            italic=True
                                        )
                                    ),
                                    center={
                                        'lng': 0,
                                        'lat': 0
                                    },
                                    radius=25
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

                        fac.AntdParagraph(
                            [
                                '将',
                                fac.AntdText(
                                    'LeafletTooltip',
                                    strong=True
                                ),
                                '置于矢量组件中',
                                fac.AntdText(
                                    'LeafletCircleMarker',
                                    strong=True
                                ),
                                '、',
                                fac.AntdText(
                                    'LeafletMarker',
                                    strong=True
                                ),
                                '、',
                                fac.AntdText(
                                    'LeafletPolyline',
                                    strong=True
                                ),
                                '、',
                                fac.AntdText(
                                    'LeafletRectangle',
                                    strong=True
                                ),
                                '、',
                                fac.AntdText(
                                    'LeafletCircle',
                                    strong=True
                                ),
                                '、',
                                fac.AntdText(
                                    'LeafletPolygon',
                                    strong=True
                                ),
                                '的',
                                fac.AntdText(
                                    'children',
                                    strong=True
                                ),
                                '中即可为对应要素组件添加额外的信息框'
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
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletCircleMarker(
            flc.LeafletTooltip(
                fac.AntdText(
                    'tooltip示例内容',
                    italic=True
                )
            ),
            center={
                'lng': 0,
                'lat': 0
            },
            radius=25
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
                                flc.LeafletLayerGroup(
                                    [
                                        flc.LeafletCircleMarker(
                                            flc.LeafletTooltip(
                                                fac.AntdText(
                                                    f'direction: {direction}',
                                                    italic=True
                                                ),
                                                direction=direction
                                            ),
                                            center={
                                                'lng': i,
                                                'lat': 0
                                            },
                                            radius=15
                                        )
                                        for i, direction in zip(
                                            range(-2, 3),
                                            [
                                                'right', 'left', 'center',
                                                'top', 'bottom'
                                            ]
                                        )
                                    ]
                                )
                            ],
                            zoom=7,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '设置展开方向',
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
        flc.LeafletLayerGroup(
            [
                flc.LeafletCircleMarker(
                    flc.LeafletTooltip(
                        fac.AntdText(
                            f'direction: {direction}',
                            italic=True
                        ),
                        direction=direction
                    ),
                    center={
                        'lng': i,
                        'lat': 0
                    },
                    radius=15
                )
                for i, direction in zip(
                    range(-2, 3),
                    [
                        'right', 'left', 'center',
                        'top', 'bottom'
                    ]
                )
            ]
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
                    id='设置展开方向',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletCircleMarker(
                                    flc.LeafletTooltip(
                                        fac.AntdText(
                                            'permanent=True',
                                            italic=True
                                        ),
                                        permanent=True
                                    ),
                                    center={
                                        'lng': 0,
                                        'lat': 0
                                    },
                                    radius=25
                                )
                            ],
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '保持展开',
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
        flc.LeafletCircleMarker(
            flc.LeafletTooltip(
                fac.AntdText(
                    'permanent=True',
                    italic=True
                ),
                permanent=True
            ),
            center={
                'lng': 0,
                'lat': 0
            },
            radius=25
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
                    id='保持展开',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletCircleMarker(
                                    flc.LeafletTooltip(
                                        fac.AntdText(
                                            'sticky=True',
                                            italic=True
                                        ),
                                        sticky=True,
                                        direction='top'
                                    ),
                                    center={
                                        'lng': 0,
                                        'lat': 0
                                    },
                                    radius=50
                                )
                            ],
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '开启鼠标跟随',
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
        flc.LeafletCircleMarker(
            flc.LeafletTooltip(
                fac.AntdText(
                    'sticky=True',
                    italic=True
                ),
                sticky=True,
                direction='top'
            ),
            center={
                'lng': 0,
                'lat': 0
            },
            radius=50
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
                    id='开启鼠标跟随',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fuc.FefferyStyle(
                            rawStyle='''
.custom-tooltip-demo {
    background: linear-gradient(135deg,#cc95c0,#dbd4b4,#7aa1d2);
    border: none;
    padding: 12px 24px;
    font-size: 18px;
}

/*隐藏小箭头*/
.custom-tooltip-demo::before {
    display: none;
}
'''
                        ),
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletCircleMarker(
                                    flc.LeafletTooltip(
                                        '示例内容',
                                        className='custom-tooltip-demo'
                                    ),
                                    center={
                                        'lng': 0,
                                        'lat': 0
                                    },
                                    radius=25
                                )
                            ],
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '自定义容器样式',
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
fuc.FefferyStyle(
    rawStyle='''
.custom-tooltip-demo {
    background: linear-gradient(135deg,#cc95c0,#dbd4b4,#7aa1d2);
    border: none;
    padding: 12px 24px;
    font-size: 18px;
}

/*隐藏小箭头*/
.custom-tooltip-demo::before {
    display: none;
}
'''
),
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletCircleMarker(
            flc.LeafletTooltip(
                '示例内容',
                className='custom-tooltip-demo'
            ),
            center={
                'lng': 0,
                'lat': 0
            },
            radius=25
        )
    ],
    style={
        'height': 500
    }
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
                    id='自定义容器样式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fuc.FefferyStyle(
                            rawStyle='''
.tooltip-as-label-demo {
    font-size: 28px;
    font-weight: bold;
    background: none;
    border: none;
    box-shadow: none;
    -webkit-text-stroke: 1px white;
}

/*隐藏小箭头*/
.tooltip-as-label-demo::before {
    display: none;
}
'''
                        ),
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletCircleMarker(
                                    flc.LeafletTooltip(
                                        '地点A',
                                        className='tooltip-as-label-demo',
                                        permanent=True,
                                        direction='center'
                                    ),
                                    center={
                                        'lng': 0,
                                        'lat': 0
                                    },
                                    radius=0,
                                    pathOptions={
                                        'weight': 0
                                    }
                                )
                            ],
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            'tooltip充当文字标注',
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
fuc.FefferyStyle(
    rawStyle='''
.tooltip-as-label-demo {
    font-size: 28px;
    font-weight: bold;
    background: none;
    border: none;
    box-shadow: none;
    -webkit-text-stroke: 1px white;
}

/*隐藏小箭头*/
.tooltip-as-label-demo::before {
    display: none;
}
'''
),
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletCircleMarker(
            flc.LeafletTooltip(
                '地点A',
                className='tooltip-as-label-demo',
                permanent=True,
                direction='center'
            ),
            center={
                'lng': 0,
                'lat': 0
            },
            radius=0,
            pathOptions={
                'weight': 0
            }
        )
    ],
    style={
        'height': 500
    }
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
                    id='tooltip充当文字标注',
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
                    {'title': '设置展开方向', 'href': '#设置展开方向'},
                    {'title': '保持展开', 'href': '#保持展开'},
                    {'title': '开启鼠标跟随', 'href': '#开启鼠标跟随'},
                    {'title': '自定义容器样式', 'href': '#自定义容器样式'},
                    {'title': 'tooltip充当文字标注', 'href': '#tooltip充当文字标注'},
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
            component_name='LeafletTooltip'
        )
    ],
    style={
        'display': 'flex'
    }
)
