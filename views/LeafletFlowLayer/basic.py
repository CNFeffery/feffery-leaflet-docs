import re
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

docs_content = fuc.FefferySplit(
    [
        fuc.FefferySplitPane(
            html.Div(
                [
                    flc.LeafletMap(
                        [
                            flc.LeafletTileLayer(
                                url='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png'
                            ),

                            flc.LeafletFlowLayer(
                                flowData=[
                                    {
                                        'from': {
                                            'lng': 106.55,
                                            'lat': 29.57
                                        },
                                        'to': {
                                            'lng': 116.3,
                                            'lat': 39.9
                                        },
                                        'labels': {
                                            'from': '重庆市',
                                            'to': '北京市'
                                        },
                                        'value': 1000
                                    },
                                    {
                                        'from': {
                                            'lng': 106.55,
                                            'lat': 29.57
                                        },
                                        'to': {
                                            'lng': 113.15,
                                            'lat': 23.06
                                        },
                                        'labels': {
                                            'from': None,
                                            'to': '广州市'
                                        },
                                        'value': 3000
                                    },
                                    {
                                        'from': {
                                            'lng': 106.55,
                                            'lat': 29.57
                                        },
                                        'to': {
                                            'lng': 121.52,
                                            'lat': 30.8
                                        },
                                        'labels': {
                                            'from': None,
                                            'to': '上海市'
                                        },
                                        'value': 2000
                                    },
                                    {
                                        'from': {
                                            'lng': 106.55,
                                            'lat': 29.57
                                        },
                                        'to': {
                                            'lng': 104.04,
                                            'lat': 30.4
                                        },
                                        'labels': {
                                            'from': None,
                                            'to': '成都市'
                                        },
                                        'value': 2000,
                                        'color': '#e84118'
                                    }
                                ],
                                maxWidth=6,
                                arcLabelFontSize='18px'
                            )
                        ],
                        zoom=5,
                        center={
                            'lng': 106.55,
                            'lat': 29.57
                        },
                        style={
                            'height': '100%'
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
                                    'LeafletFlowLayer参数说明',
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
                                    open('documents/LeafletFlowLayer.md', encoding='utf-8')
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
language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
import feffery_leaflet_components as flc

flc.LeafletMap(
    [
        flc.LeafletTileLayer(
            url='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png'
        ),

        flc.LeafletFlowLayer(
            flowData=[
                {
                    'from': {
                        'lng': 106.55,
                        'lat': 29.57
                    },
                    'to': {
                        'lng': 116.3,
                        'lat': 39.9
                    },
                    'labels': {
                        'from': '重庆市',
                        'to': '北京市'
                    },
                    'value': 1000
                },
                {
                    'from': {
                        'lng': 106.55,
                        'lat': 29.57
                    },
                    'to': {
                        'lng': 113.15,
                        'lat': 23.06
                    },
                    'labels': {
                        'from': None,
                        'to': '广州市'
                    },
                    'value': 3000
                },
                {
                    'from': {
                        'lng': 106.55,
                        'lat': 29.57
                    },
                    'to': {
                        'lng': 121.52,
                        'lat': 30.8
                    },
                    'labels': {
                        'from': None,
                        'to': '上海市'
                    },
                    'value': 2000
                },
                {
                    'from': {
                        'lng': 106.55,
                        'lat': 29.57
                    },
                    'to': {
                        'lng': 104.04,
                        'lat': 30.4
                    },
                    'labels': {
                        'from': None,
                        'to': '成都市'
                    },
                    'value': 2000,
                    'color': '#e84118'
                }
            ],
            maxWidth=6,
            arcLabelFontSize='18px'
        )
    ],
    zoom=5,
    center={
        'lng': 106.55,
        'lat': 29.57
    },
    style={
        'height': '100%'
    }
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
    id='LeafletFlowLayer-basic-container',
    sizes=[60, 40],
    gutterSize=10,
    style={
        'height': '100%'
    }
)
