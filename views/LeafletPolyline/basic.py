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
                            flc.LeafletTileLayer(),
                            # 单折线示例
                            flc.LeafletPolyline(
                                positions=[
                                    {'lng': 0, 'lat': 0},
                                    {'lng': 1, 'lat': 0},
                                    {'lng': 1, 'lat': 1},
                                    {'lng': 2, 'lat': 1},
                                    {'lng': 2, 'lat': 2}
                                ]
                            ),
                            # 多折线示例
                            flc.LeafletPolyline(
                                positions=[
                                    [
                                        {'lng': 0, 'lat': -2},
                                        {'lng': 1, 'lat': -2},
                                        {'lng': 1, 'lat': -1},
                                        {'lng': 2, 'lat': -1},
                                        {'lng': 2, 'lat': 0}
                                    ],
                                    [
                                        {'lng': 0, 'lat': -3.5},
                                        {'lng': 1, 'lat': -3.5},
                                        {'lng': 1, 'lat': -2.5},
                                        {'lng': 2, 'lat': -2.5},
                                        {'lng': 2, 'lat': -1.5}
                                    ],
                                ],
                                pathOptions={
                                    'color': 'red',
                                    'dashArray': '5, 5'
                                }
                            )
                        ],
                        zoom=6,
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
                                    'LeafletPolyline参数说明',
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
                                    open('documents/LeafletPolyline.md', encoding='utf-8')
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
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
import feffery_leaflet_components as flc
                                
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        # 单折线示例
        flc.LeafletPolyline(
            positions=[
                {'lng': 0, 'lat': 0},
                {'lng': 1, 'lat': 0},
                {'lng': 1, 'lat': 1},
                {'lng': 2, 'lat': 1},
                {'lng': 2, 'lat': 2}
            ]
        ),
        # 多折线示例
        flc.LeafletPolyline(
            positions=[
                [
                    {'lng': 0, 'lat': -2},
                    {'lng': 1, 'lat': -2},
                    {'lng': 1, 'lat': -1},
                    {'lng': 2, 'lat': -1},
                    {'lng': 2, 'lat': 0}
                ],
                [
                    {'lng': 0, 'lat': -3.5},
                    {'lng': 1, 'lat': -3.5},
                    {'lng': 1, 'lat': -2.5},
                    {'lng': 2, 'lat': -2.5},
                    {'lng': 2, 'lat': -1.5}
                ],
            ],
            pathOptions={
                'color': 'red',
                'dashArray': '5, 5'
            }
        )
    ],
    zoom=6,
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
    id='LeafletPolyline-basic-container',
    sizes=[60, 40],
    gutterSize=10,
    style={
        'height': '100%'
    }
)
