import uuid
from dash import html
import feffery_antd_components as fac
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
                            'title': '基础组件'
                        },
                        {
                            'title': 'LeafletMap 地图容器'
                        },
                        {
                            'title': '基础使用'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        '地图容器是',
                        fac.AntdText(
                            'flc',
                            strong=True
                        ),
                        '中构建一个地图实例的基础，地图容器通过嵌套其他',
                        fac.AntdText(
                            'flc',
                            strong=True
                        ),
                        '子功能组件来实现更复杂的地图功能。'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                html.Div(
                    [
                        flc.LeafletMap(
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
                                '利用带有高度的',
                                fac.AntdText(
                                    'LeafletMap',
                                    strong=True
                                ),
                                '组件来定义地图容器'
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
                                flc.LeafletTileLayer()
                            ],
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '叠加在线底图',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '地图容器通常都需要搭配在线底图使用'
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
        flc.LeafletTileLayer()
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
                    id='叠加在线底图',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=14,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '设置初始中心及缩放层级',
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
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=14,
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
                    id='设置初始中心及缩放层级',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            doubleClickZoom=False,
                            dragging=False,
                            zoomControl=False,
                            scrollWheelZoom=False,
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=14,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '更多放缩拖拽相关参数',
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
        flc.LeafletTileLayer()
    ],
    doubleClickZoom=False,
    dragging=False,
    zoomControl=False,
    scrollWheelZoom=False,
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=14,
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
                    id='更多放缩拖拽相关参数',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=14,
                            minZoom=13,
                            maxZoom=16,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '限定可缩放层级范围',
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
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=14,
    minZoom=13,
    maxZoom=16,
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
                    id='限定可缩放层级范围',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=14,
                            maxBounds={
                                'minx': 106.57,
                                'miny': 29.55,
                                'maxx': 106.58,
                                'maxy': 29.57
                            },
                            minZoom=14,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '限制地图在固定范围内',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '通过设置参数',
                                fac.AntdText(
                                    'maxBounds',
                                    code=True
                                ),
                                '可以实现将地图锁定在指定范围内，当用户尝试拖拽地图出此范围时会自动进行回弹'
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
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=14,
    maxBounds={
        'minx': 106.57,
        'miny': 29.55,
        'maxx': 106.58,
        'maxy': 29.57
    },
    minZoom=14,
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
                    id='限制地图在固定范围内',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=14,
                            smoothWheelZoom=True,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '丝滑缩放模式',
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
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=14,
    smoothWheelZoom=True,
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
                    id='丝滑缩放模式',
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
                    {'title': '叠加在线底图', 'href': '#叠加在线底图'},
                    {'title': '设置初始中心及缩放层级', 'href': '#设置初始中心及缩放层级'},
                    {'title': '更多放缩拖拽相关参数', 'href': '#更多放缩拖拽相关参数'},
                    {'title': '限定可缩放层级范围', 'href': '#限定可缩放层级范围'},
                    {'title': '限制地图在固定范围内', 'href': '#限制地图在固定范围内'},
                    {'title': '丝滑缩放模式', 'href': '#丝滑缩放模式'},
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
            component_name='LeafletMap'
        )
    ],
    id=str(uuid.uuid4()),
    style={
        'display': 'flex'
    }
)
