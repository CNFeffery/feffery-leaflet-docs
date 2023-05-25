import uuid
import random
import requests
from dash import html
from copy import deepcopy
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

import callbacks.LeafletGeoJSON
from .side_props import render_side_props_layout

basic_geojson = (
    requests
    .get('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')
    .json()
)

# 生成分层设色所需数据
choropleth_geojson = deepcopy(basic_geojson)
for i, feature in enumerate(choropleth_geojson['features']):
    choropleth_geojson['features'][i]['properties']['value'] = random.uniform(
        0, 100
    )

# 生成分类设色所需数据
category_geojson = deepcopy(basic_geojson)
for i, feature in enumerate(category_geojson['features']):
    category_geojson['features'][i]['properties']['category'] = random.choice(
        list('abcd')
    )


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
                            'title': '矢量'
                        },
                        {
                            'title': 'LeafletGeoJSON GeoJSON要素'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在地图中渲染具有丰富功能的GeoJSON矢量要素。')
                    ]
                ),

                fac.AntdText(
                    'LeafletGeoJSON相关文档所使用的示例GeoJSON数据来自阿里云datav公共开放接口，获取对应原始矢量数据代码如下：',
                    type='secondary',
                    style={
                        'borderLeft': '3px solid #adb5bd',
                        'paddingLeft': 8
                    }
                ),

                fmc.FefferySyntaxHighlighter(
                    codeTheme='coy-without-shadows',
                    language='python',
                    codeString='''
import requests

basic_geojson = (
    requests
    .get('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')
    .json()
)
'''
                ),

                fac.AntdDivider(isDashed=True),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletGeoJSON(
                                    data=basic_geojson
                                )
                            ],
                            zoom=6,
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
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletGeoJSON(
            data=basic_geojson
        )
    ],
    zoom=6,
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
                                flc.LeafletGeoJSON(
                                    data=basic_geojson,
                                    defaultStyle={
                                        'color': 'white',
                                        'weight': 2,
                                        'dashArray': '5, 2, 5',
                                        'fillOpacity': 0.4,
                                        'fillColor': 'red'
                                    }
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '自定义样式',
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
        flc.LeafletGeoJSON(
            data=basic_geojson,
            defaultStyle={
                'color': 'white',
                'weight': 2,
                'dashArray': '5, 2, 5',
                'fillOpacity': 0.4,
                'fillColor': 'red'
            }
        )
    ],
    zoom=6,
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
                    id='自定义样式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletGeoJSON(
                                    data=basic_geojson,
                                    hoverable=True,
                                    hoverStyle={
                                        'fillOpacity': 0.8,
                                        'color': 'white'
                                    }
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '启用鼠标悬停效果',
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
        flc.LeafletGeoJSON(
            data=basic_geojson,
            hoverable=True,
            hoverStyle={
                'fillOpacity': 0.8,
                'color': 'white'
            }
        )
    ],
    zoom=6,
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
                    id='启用鼠标悬停效果',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletGeoJSON(
                                    data=basic_geojson,
                                    clickFeatureZoom=True
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '点击缩放至要素',
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
        flc.LeafletGeoJSON(
            data=basic_geojson,
            clickFeatureZoom=True
        )
    ],
    zoom=6,
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
                    id='点击缩放至要素',
                    className='div-highlight'
                ),

                html.Div(id='要素tooltip相关功能'),
                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletGeoJSON(
                                    data=basic_geojson,
                                    featureTooltipField='name',
                                    showTooltip=True
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '为要素添加tooltip',
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
        flc.LeafletGeoJSON(
            data=basic_geojson,
            featureTooltipField='name',
            showTooltip=True
        )
    ],
    zoom=6,
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
                    id='为要素添加tooltip',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fuc.FefferyStyle(
                            rawStyle='''
.geojson-tooltip-demo {
    border-radius: 0;
    background: #4dabf7;
    color: white;
    border: none;
    font-size: 20px;
}

.geojson-tooltip-demo::before {
    display: none;
}
'''
                        ),

                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletGeoJSON(
                                    data=basic_geojson,
                                    featureTooltipField='name',
                                    showTooltip=True,
                                    tooltipClassName='geojson-tooltip-demo',
                                    tooltipDirection='center'
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '自定义tooltip样式类',
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
import feffery_utils_components as fuc

...

fuc.FefferyStyle(
    rawStyle='''
.geojson-tooltip-demo {
    border-radius: 0;
    background: #4dabf7;
    color: white;
    border: none;
    font-size: 20px;
}

.geojson-tooltip-demo::before {
    display: none;
}
'''
),

flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletGeoJSON(
            data=basic_geojson,
            featureTooltipField='name',
            showTooltip=True,
            tooltipClassName='geojson-tooltip-demo',
            tooltipDirection='center'
        )
    ],
    zoom=6,
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
                    id='自定义tooltip样式类',
                    className='div-highlight'
                ),

                html.Div(id='要素选择相关功能'),
                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletGeoJSON(
                                    id='geojson-selectable-single-demo',
                                    data=basic_geojson,
                                    mode='selectable',
                                    featureIdField='name'
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),
                        html.Pre(
                            id='geojson-selectable-single-demo-output'
                        ),

                        fac.AntdDivider(
                            '单选模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '在使用',
                                fac.AntdText(
                                    'LeafletGeoJSON',
                                    strong=True
                                ),
                                '的要素选择功能时，需要确保参数',
                                fac.AntdText(
                                    'featureIdField',
                                    code=True
                                ),
                                '对应的各要素属性字段值可以唯一识别对应要素'
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
                                codeString="""
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletGeoJSON(
            id='geojson-selectable-single-demo',
            data=basic_geojson,
            mode='selectable',
            featureIdField='name'
        )
    ],
    zoom=6,
    style={
        'height': 500
    }
),
html.Pre(
    id='geojson-selectable-single-demo-output'
)

...

app.clientside_callback(
    '''( selectedFeatureIds ) => JSON.stringify({ selectedFeatureIds }, null, 4)''',
    Output('geojson-selectable-single-demo-output', 'children'),
    Input('geojson-selectable-single-demo', 'selectedFeatureIds')
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
                    id='单选模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletGeoJSON(
                                    id='geojson-selectable-multiple-demo',
                                    data=basic_geojson,
                                    mode='selectable',
                                    selectMode='multiple',
                                    featureIdField='name'
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),
                        html.Pre(
                            id='geojson-selectable-multiple-demo-output'
                        ),

                        fac.AntdDivider(
                            '多选模式',
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
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletGeoJSON(
            id='geojson-selectable-multiple-demo',
            data=basic_geojson,
            mode='selectable',
            selectMode='multiple',
            featureIdField='name'
        )
    ],
    zoom=6,
    style={
        'height': 500
    }
),
html.Pre(
    id='geojson-selectable-multiple-demo-output'
)

...

app.clientside_callback(
    '''( selectedFeatureIds ) => JSON.stringify({ selectedFeatureIds }, null, 4)''',
    Output('geojson-selectable-multiple-demo-output', 'children'),
    Input('geojson-selectable-multiple-demo', 'selectedFeatureIds')
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
                    id='多选模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletGeoJSON(
                                    id='geojson-selectable-multiple-lasso-demo',
                                    data=basic_geojson,
                                    mode='selectable',
                                    selectMode='multiple',
                                    lassoSelect=True,
                                    featureIdField='name'
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),
                        html.Pre(
                            id='geojson-selectable-multiple-lasso-demo-output'
                        ),

                        fac.AntdDivider(
                            '套索多选',
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
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletGeoJSON(
            id='geojson-selectable-multiple-lasso-demo',
            data=basic_geojson,
            mode='selectable',
            selectMode='multiple',
            lassoSelect=True,
            featureIdField='name'
        )
    ],
    zoom=6,
    style={
        'height': 500
    }
),
html.Pre(
    id='geojson-selectable-multiple-lasso-demo-output'
)

...

app.clientside_callback(
    '''( selectedFeatureIds ) => JSON.stringify({ selectedFeatureIds }, null, 4)''',
    Output('geojson-selectable-multiple-lasso-demo-output', 'children'),
    Input('geojson-selectable-multiple-lasso-demo', 'selectedFeatureIds')
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
                    id='套索多选',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletGeoJSON(
                                    data=choropleth_geojson,
                                    mode='choropleth',
                                    featureValueField='value',
                                    featureValueToStyles={
                                        'bins': [
                                            [0, 25],
                                            [25, 50],
                                            [50, 75],
                                            [75, 101]
                                        ],
                                        'styles': [
                                            {
                                                'color': '#ffc9c9',
                                                'fillOpacity': 1,
                                                'weight': 1
                                            },
                                            {
                                                'color': '#ffa8a8',
                                                'fillOpacity': 1,
                                                'weight': 1
                                            },
                                            {
                                                'color': '#ff8787',
                                                'fillOpacity': 1,
                                                'weight': 1
                                            },
                                            {
                                                'color': '#ff6b6b',
                                                'fillOpacity': 1,
                                                'weight': 1
                                            }
                                        ]
                                    }
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '分层设色模式',
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
from copy import deepcopy

# 生成分层设色所需数据
choropleth_geojson = deepcopy(basic_geojson)
for i, feature in enumerate(choropleth_geojson['features']):
    choropleth_geojson['features'][i]['properties']['value'] = random.uniform(
        0, 100
    )

...

flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletGeoJSON(
            data=choropleth_geojson,
            mode='choropleth',
            featureValueField='value',
            featureValueToStyles={
                'bins': [
                    [0, 25],
                    [25, 50],
                    [50, 75],
                    [75, 101]
                ],
                'styles': [
                    {
                        'color': '#ffc9c9',
                        'fillOpacity': 1,
                        'weight': 1
                    },
                    {
                        'color': '#ffa8a8',
                        'fillOpacity': 1,
                        'weight': 1
                    },
                    {
                        'color': '#ff8787',
                        'fillOpacity': 1,
                        'weight': 1
                    },
                    {
                        'color': '#ff6b6b',
                        'fillOpacity': 1,
                        'weight': 1
                    }
                ]
            }
        )
    ],
    zoom=6,
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
                    id='分层设色模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletGeoJSON(
                                    data=category_geojson,
                                    mode='category',
                                    featureCategoryToStyles={
                                        'a': {
                                            'color': '#d29200',
                                            'fillOpacity': 1,
                                            'weight': 1
                                        },
                                        'b': {
                                            'color': '#ffb900',
                                            'fillOpacity': 1,
                                            'weight': 1
                                        },
                                        'c': {
                                            'color': '#fff100',
                                            'fillOpacity': 1,
                                            'weight': 1
                                        },
                                        'd': {
                                            'color': '#d83b01',
                                            'fillOpacity': 1,
                                            'weight': 1
                                        },
                                    }
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '分类设色模式',
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
from copy import deepcopy

# 生成分类设色所需数据
category_geojson = deepcopy(basic_geojson)
for i, feature in enumerate(category_geojson['features']):
    category_geojson['features'][i]['properties']['category'] = random.choice(
        list('abcd')
    )

...

flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletGeoJSON(
            data=category_geojson,
            mode='category',
            featureCategoryToStyles={
                'a': {
                    'color': '#d29200',
                    'fillOpacity': 1,
                    'weight': 1
                },
                'b': {
                    'color': '#ffb900',
                    'fillOpacity': 1,
                    'weight': 1
                },
                'c': {
                    'color': '#fff100',
                    'fillOpacity': 1,
                    'weight': 1
                },
                'd': {
                    'color': '#d83b01',
                    'fillOpacity': 1,
                    'weight': 1
                },
            }
        )
    ],
    zoom=6,
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
                    id='分类设色模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletGeoJSON(
                                    id='geojson-event-demo',
                                    data=basic_geojson,
                                    hoverable=True
                                )
                            ],
                            zoom=6,
                            style={
                                'height': 500
                            }
                        ),
                        html.Pre(id='geojson-event-demo-output'),

                        fac.AntdDivider(
                            '要素交互事件监听',
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
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletGeoJSON(
            id='geojson-event-demo',
            data=basic_geojson,
            hoverable=True
        )
    ],
    zoom=6,
    style={
        'height': 500
    }
),
html.Pre(id='geojson-event-demo-output')

...

app.clientside_callback(
    '''( _clickedFeature, _hoveredFeature ) => JSON.stringify({ _clickedFeature, _hoveredFeature }, null, 4)''',
    Output('geojson-event-demo-output', 'children'),
    [Input('geojson-event-demo', '_clickedFeature'),
     Input('geojson-event-demo', '_hoveredFeature')]
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
                    id='要素交互事件监听',
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
                    {'title': '自定义样式', 'href': '#自定义样式'},
                    {'title': '启用鼠标悬停效果', 'href': '#启用鼠标悬停效果'},
                    {'title': '点击缩放至要素', 'href': '#点击缩放至要素'},
                    {
                        'title': '要素tooltip相关功能',
                        'href': '#要素tooltip相关功能',
                        'children': [
                            {'title': '为要素添加tooltip', 'href': '#为要素添加tooltip'},
                            {'title': '自定义tooltip样式类', 'href': '#自定义tooltip样式类'}
                        ]
                    },
                    {
                        'title': '要素选择相关功能',
                        'href': '#要素选择相关功能',
                        'children': [
                            {'title': '单选模式', 'href': '#单选模式'},
                            {'title': '多选模式', 'href': '#多选模式'},
                            {'title': '套索多选', 'href': '#套索多选'},
                        ]
                    },
                    {'title': '分层设色模式', 'href': '#分层设色模式'},
                    {'title': '分类设色模式', 'href': '#分类设色模式'},
                    {'title': '要素交互事件监听', 'href': '#要素交互事件监听'},
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
            component_name='LeafletGeoJSON'
        )
    ],
    id=str(uuid.uuid4()),
    style={
        'display': 'flex'
    }
)
