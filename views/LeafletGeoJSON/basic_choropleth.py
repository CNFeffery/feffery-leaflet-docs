import re
import random
import requests
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

data = (
    requests
        .get('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')
        .json()
)

# 构建随机示例属性字段
for i in range(len(data['features'])):
    data['features'][i]['properties'] = {
        **data['features'][i]['properties'],
        'random_value': round(random.uniform(0, 1), 3)
    }

    data['features'][i]['properties']['tooltip'] = '{}，示例数值：{}'.format(
        data['features'][i]['properties']['name'],
        data['features'][i]['properties']['random_value']
    )

docs_content = fuc.FefferySplit(
    [
        fuc.FefferySplitPane(
            html.Div(
                [
                    flc.LeafletMap(
                        [
                            flc.LeafletTileLayer(),

                            flc.LeafletGeoJSON(
                                data=data,
                                mode='choropleth',
                                featureValueField='random_value',
                                showTooltip=True,
                                featureValueToStyles={
                                    'bins': [
                                        [0, 0.33],
                                        [0.33, 0.66],
                                        [0.66, 1]
                                    ],
                                    'styles': [
                                        {
                                            'fillColor': '#ffccc7',
                                            'fillOpacity': 1,
                                            'weight': 1,
                                            'color': 'white'
                                        },
                                        {
                                            'fillColor': '#ff7875',
                                            'fillOpacity': 1,
                                            'weight': 1,
                                            'color': 'white'
                                        },
                                        {
                                            'fillColor': '#f5222d',
                                            'fillOpacity': 1,
                                            'weight': 1,
                                            'color': 'white'
                                        }
                                    ]
                                }
                            )
                        ],
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
                                    'LeafletGeoJSON参数说明',
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
                                    open('documents/LeafletGeoJSON.md', encoding='utf-8')
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
import random
import requests
import feffery_leaflet_components as flc

data = (
    requests
        .get('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')
        .json()
)

# 构建随机示例属性字段
for i in range(len(data['features'])):
    data['features'][i]['properties'] = {
        **data['features'][i]['properties'],
        'random_value': round(random.uniform(0, 1), 3)
    }

    data['features'][i]['properties']['tooltip'] = '{}，示例数值：{}'.format(
        data['features'][i]['properties']['name'],
        data['features'][i]['properties']['random_value']
    )
    
...

flc.LeafletMap(
    [
        flc.LeafletTileLayer(),

        flc.LeafletGeoJSON(
            data=data,
            mode='choropleth',
            featureValueField='random_value',
            showTooltip=True,
            featureValueToStyles={
                'bins': [
                    [0, 0.33],
                    [0.33, 0.66],
                    [0.66, 1]
                ],
                'styles': [
                    {
                        'fillColor': '#ffccc7',
                        'fillOpacity': 1,
                        'weight': 1,
                        'color': 'white'
                    },
                    {
                        'fillColor': '#ff7875',
                        'fillOpacity': 1,
                        'weight': 1,
                        'color': 'white'
                    },
                    {
                        'fillColor': '#f5222d',
                        'fillOpacity': 1,
                        'weight': 1,
                        'color': 'white'
                    }
                ]
            }
        )
    ],
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
    id='LeafletGeoJSON-basic-choropleth-container',
    sizes=[60, 40],
    gutterSize=10,
    style={
        'height': '100%'
    }
)
