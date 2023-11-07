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
                            'title': 'LeafletStaticHeatMap 静态热力图'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于渲染不会随地图缩放而变化的高性能热力图层。')
                    ]
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletStaticHeatMap(
                                    points=[
                                        {
                                            'lng': 113.265564 + random.normalvariate(0, 0.005),
                                            'lat': 23.114191 + random.normalvariate(0, 0.005)
                                        }
                                        for i in range(1000)
                                    ],
                                    size=150,
                                    opacity=0.8
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

                        fac.AntdParagraph(
                            [
                                '与',
                                fac.AntdText(
                                    'LeafletHeatMap',
                                    strong=True
                                ),
                                '不同，',
                                fac.AntdText(
                                    'LeafletStaticHeatMap',
                                    strong=True
                                ),
                                '通过调整',
                                fac.AntdText(
                                    'size',
                                    code=True
                                ),
                                '等参数所呈现出的热力图层效果相对稳定，不会随着地图缩放等级变化而发生明显变化。'
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

flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletStaticHeatMap(
            points=[
                {
                    'lng': 113.265564 + random.normalvariate(0, 0.005),
                    'lat': 23.114191 + random.normalvariate(0, 0.005)
                }
                for i in range(1000)
            ],
            size=150,
            opacity=0.8
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
                    {'title': '基础使用', 'href': '#基础使用'}
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
            component_name='LeafletStaticHeatMap'
        )
    ],
    style={
        'display': 'flex'
    }
)
