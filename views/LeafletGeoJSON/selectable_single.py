import re
import requests
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc
from dash.dependencies import Input, Output

from server import app

docs_content = fuc.FefferySplit(
    [
        fuc.FefferySplitPane(
            html.Div(
                [
                    flc.LeafletMap(
                        [
                            flc.LeafletTileLayer(),

                            flc.LeafletGeoJSON(
                                id='geojson-selectable-single',
                                data=(
                                    requests
                                        .get('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')
                                        .json()
                                ),
                                mode='selectable',
                                featureIdField='name'
                            )
                        ],
                        style={
                            'height': '100%'
                        }
                    ),

                    html.Div(
                        id='selectable-single-result',
                        style={
                            'background': 'white',
                            'position': 'absolute',
                            'height': '100px',
                            'width': '250px',
                            'bottom': '10px',
                            'padding': '15px',
                            'right': '10px',
                            'zIndex': 999,
                            'borderRadius': '10px'
                        }
                    )
                ],
                style={
                    'height': '100%',
                    'position': 'relative'
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
import requests
from dash import html
import feffery_leaflet_components as flc

html.Div(
    [
        flc.LeafletMap(
            [
                flc.LeafletTileLayer(),

                flc.LeafletGeoJSON(
                    id='geojson-selectable-single',
                    data=(
                        requests
                            .get('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')
                            .json()
                    ),
                    mode='selectable',
                    featureIdField='name'
                )
            ],
            style={
                'height': '100%'
            }
        ),

        html.Div(
            id='selectable-single-result',
            style={
                'background': 'white',
                'position': 'absolute',
                'height': '100px',
                'width': '250px',
                'bottom': '10px',
                'padding': '15px',
                'right': '10px',
                'zIndex': 999,
                'borderRadius': '10px'
            }
        )
    ],
    style={
        'height': '100%',
        'position': 'relative'
    }
)

...

@app.callback(
    Output('selectable-single-result', 'children'),
    Input('geojson-selectable-single', 'selectedFeatureIds')
)
def selectable_single_callback(selectedFeatureIds):
    if selectedFeatureIds:
        return f'已选择要素id字段：{selectedFeatureIds}'

    return '请点击选择一个要素'
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
    id='LeafletGeoJSON-selectable-single-container',
    sizes=[60, 40],
    gutterSize=10,
    style={
        'height': '100%'
    }
)


@app.callback(
    Output('selectable-single-result', 'children'),
    Input('geojson-selectable-single', 'selectedFeatureIds')
)
def selectable_single_callback(selectedFeatureIds):
    if selectedFeatureIds:
        return f'已选择要素id字段：{selectedFeatureIds}'

    return '请点击选择一个要素'
