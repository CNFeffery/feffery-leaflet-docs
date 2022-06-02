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

                            # 单多边形
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
                            ),

                            # 有孔单多边形
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
                                ],
                                pathOptions={
                                    'color': 'red'
                                }
                            ),

                            # 多多边形
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
                                    ],

                                    [
                                        [
                                            {
                                                'lng': 8,
                                                'lat': -8
                                            },
                                            {
                                                'lng': 8,
                                                'lat': -10
                                            },
                                            {
                                                'lng': 10,
                                                'lat': -10
                                            },
                                            {
                                                'lng': 8,
                                                'lat': -8
                                            },
                                        ],
                                        [
                                            {
                                                'lng': 8.1,
                                                'lat': -8.25
                                            },
                                            {
                                                'lng': 8.25,
                                                'lat': -9.75
                                            },
                                            {
                                                'lng': 9.25,
                                                'lat': -9.5
                                            },
                                            {
                                                'lng': 8.1,
                                                'lat': -8.25
                                            },
                                        ],
                                    ]
                                ],
                                pathOptions={
                                    'color': 'yellow'
                                }
                            )
                        ],
                        zoom=5,
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
                                    'LeafletPolygon参数说明',
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
                                    open('documents/LeafletPolygon.md', encoding='utf-8')
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

        # 单多边形
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
        ),

        # 有孔单多边形
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
            ],
            pathOptions={
                'color': 'red'
            }
        ),

        # 多多边形
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
                ],

                [
                    [
                        {
                            'lng': 8,
                            'lat': -8
                        },
                        {
                            'lng': 8,
                            'lat': -10
                        },
                        {
                            'lng': 10,
                            'lat': -10
                        },
                        {
                            'lng': 8,
                            'lat': -8
                        },
                    ],
                    [
                        {
                            'lng': 8.1,
                            'lat': -8.25
                        },
                        {
                            'lng': 8.25,
                            'lat': -9.75
                        },
                        {
                            'lng': 9.25,
                            'lat': -9.5
                        },
                        {
                            'lng': 8.1,
                            'lat': -8.25
                        },
                    ],
                ]
            ],
            pathOptions={
                'color': 'yellow'
            }
        )
    ],
    zoom=5,
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
    id='LeafletPolygon-basic-container',
    sizes=[60, 40],
    gutterSize=10,
    style={
        'height': '100%'
    }
)
