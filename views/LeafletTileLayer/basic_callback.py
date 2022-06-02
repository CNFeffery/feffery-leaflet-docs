import re
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
                            flc.LeafletTileLayer(
                                id='tile-layer'
                            )
                        ],
                        style={
                            'height': '100%'
                        }
                    ),

                    fac.AntdSelect(
                        id='tile-layer-select',
                        options=[
                            {
                                'label': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                                'value': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
                            },
                            {
                                'label': 'http://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
                                'value': 'http://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}'
                            },
                            {
                                'label': 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                                'value': 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png'
                            },
                            {
                                'label': 'http://{s}.tile.stamen.com/terrain/{z}/{x}/{y}.jpg',
                                'value': 'http://{s}.tile.stamen.com/terrain/{z}/{x}/{y}.jpg'
                            },
                            {
                                'label': 'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
                                'value': 'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
                            },
                            {
                                'label': 'http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png',
                                'value': 'http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png'
                            },
                            {
                                'label': 'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png',
                                'value': 'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png'
                            },
                            {
                                'label': 'https://stamen-tiles-a.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}.png',
                                'value': 'https://stamen-tiles-a.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}.png'
                            },
                            {
                                'label': 'https://d.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png',
                                'value': 'https://d.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png'
                            },
                            {
                                'label': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                                'value': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
                            },
                            {
                                'label': 'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
                                'value': 'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png'
                            }
                        ],
                        allowClear=False,
                        defaultValue='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                        style={
                            'position': 'absolute',
                            'width': 'calc(100% - 300px)',
                            'right': '10px',
                            'top': '10px',
                            'zIndex': 999
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
                                    'LeafletTileLayer参数说明',
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
                                    open('documents/LeafletTileLayer.md', encoding='utf-8')
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
from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc

html.Div(
    [
        flc.LeafletMap(
            [
                flc.LeafletTileLayer(
                    id='tile-layer'
                )
            ],
            style={
                'height': '100%'
            }
        ),

        fac.AntdSelect(
            id='tile-layer-select',
            options=[
                {
                    'label': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                    'value': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
                },
                {
                    'label': 'http://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
                    'value': 'http://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}'
                },
                {
                    'label': 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                    'value': 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png'
                },
                {
                    'label': 'http://{s}.tile.stamen.com/terrain/{z}/{x}/{y}.jpg',
                    'value': 'http://{s}.tile.stamen.com/terrain/{z}/{x}/{y}.jpg'
                },
                {
                    'label': 'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
                    'value': 'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
                },
                {
                    'label': 'http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png',
                    'value': 'http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png'
                },
                {
                    'label': 'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png',
                    'value': 'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png'
                },
                {
                    'label': 'https://stamen-tiles-a.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}.png',
                    'value': 'https://stamen-tiles-a.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}.png'
                },
                {
                    'label': 'https://d.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png',
                    'value': 'https://d.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png'
                },
                {
                    'label': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                    'value': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
                },
                {
                    'label': 'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
                    'value': 'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png'
                }
            ],
            allowClear=False,
            defaultValue='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            style={
                'position': 'absolute',
                'width': 'calc(100% - 300px)',
                'right': '10px',
                'top': '10px',
                'zIndex': 999
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
    Output('tile-layer', 'url'),
    Input('tile-layer-select', 'value')
)
def tile_switch(value):
    return value
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
    id='LeafletTileLayer-basic-callback-container',
    sizes=[60, 40],
    gutterSize=10,
    style={
        'height': '100%'
    }
)


@app.callback(
    Output('tile-layer', 'url'),
    Input('tile-layer-select', 'value')
)
def tile_switch(value):
    return value
