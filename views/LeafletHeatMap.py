import random
from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

# import callbacks.AntdButton
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
                            'title': '特殊图层'
                        },
                        {
                            'title': 'LeafletHeatMap 热力图'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于渲染随地图缩放而动态变化的热力图层。')
                    ]
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletHeatMap(
                                    points=[
                                        {
                                            'lng': 113.265564 + random.normalvariate(0, 0.005),
                                            'lat': 23.114191 + random.normalvariate(0, 0.005)
                                        }
                                        for i in range(1000)
                                    ]
                                )
                            ],
                            center={
                                "lat": 23.114191,
                                "lng": 113.265564
                            },
                            zoom=16,
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
import random

...

flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletHeatMap(
            points=[
                {
                    'lng': 113.265564 + random.normalvariate(0, 0.005),
                    'lat': 23.114191 + random.normalvariate(0, 0.005)
                }
                for i in range(1000)
            ]
        )
    ],
    center={
        "lat": 23.114191,
        "lng": 113.265564
    },
    zoom=16,
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
                                flc.LeafletHeatMap(
                                    points=[
                                        {
                                            'lng': 113.265564 + random.normalvariate(0, 0.005),
                                            'lat': 23.114191 + random.normalvariate(0, 0.005)
                                        }
                                        for i in range(1000)
                                    ],
                                    gradient={
                                        0.4: '#fffbe6',
                                        0.65: '#ffc53d',
                                        1: '#ff4d4f'
                                    }
                                )
                            ],
                            center={
                                "lat": 23.114191,
                                "lng": 113.265564
                            },
                            zoom=16,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '自定义配色方案',
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
import random

...

flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletHeatMap(
            points=[
                {
                    'lng': 113.265564 + random.normalvariate(0, 0.005),
                    'lat': 23.114191 + random.normalvariate(0, 0.005)
                }
                for i in range(1000)
            ],
            gradient={
                0.4: '#fffbe6',
                0.65: '#ffc53d',
                1: '#ff4d4f'
            }
        )
    ],
    center={
        "lat": 23.114191,
        "lng": 113.265564
    },
    zoom=16,
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
                    id='自定义配色方案',
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
                    {'title': '自定义配色方案', 'href': '#自定义配色方案'},
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
            component_name='LeafletHeatMap'
        )
    ],
    style={
        'display': 'flex'
    }
)
