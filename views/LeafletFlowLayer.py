from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

import callbacks.LeafletFlowLayer
from .side_props import render_side_props_layout

demo_colors = ['#2f54eb', '#597ef7', '#85a5ff', '#adc6ff']

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
                            'title': 'LeafletFlowLayer 流线图层'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在轻量化数据场景下渲染动态流线地图。')
                    ]
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(
                                    url='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}'
                                ),
                                flc.LeafletFlowLayer(
                                    flowData=[
                                        {
                                            'from': {
                                                'lng': source['lng'],
                                                'lat': source['lat']
                                            },
                                            'to': {
                                                'lat': 29.53,
                                                'lng': 106.53
                                            }
                                        }
                                        for source in [
                                            {
                                                'name': '北京',
                                                'lat': 39.91,
                                                'lng': 116.41
                                            },
                                            {
                                                'name': '上海',
                                                'lat': 31.23,
                                                'lng': 121.45
                                            },
                                            {
                                                'name': '昆明',
                                                'lat': 24.89,
                                                'lng': 102.83
                                            },
                                            {
                                                'name': '金边',
                                                'lat': 11.54,
                                                'lng': 104.87
                                            }
                                        ]
                                    ]
                                )
                            ],
                            center={
                                'lat': 26.53,
                                'lng': 106.53
                            },
                            zoom=4,
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
        flc.LeafletTileLayer(
            url='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}'
        ),
        flc.LeafletFlowLayer(
            flowData=[
                {
                    'from': {
                        'lng': source['lng'],
                        'lat': source['lat']
                    },
                    'to': {
                        'lat': 29.53,
                        'lng': 106.53
                    }
                }
                for source in [
                    {
                        'name': '北京',
                        'lat': 39.91,
                        'lng': 116.41
                    },
                    {
                        'name': '上海',
                        'lat': 31.23,
                        'lng': 121.45
                    },
                    {
                        'name': '昆明',
                        'lat': 24.89,
                        'lng': 102.83
                    },
                    {
                        'name': '金边',
                        'lat': 11.54,
                        'lng': 104.87
                    }
                ]
            ]
        )
    ],
    center={
        'lat': 26.53,
        'lng': 106.53
    },
    zoom=4,
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
                                flc.LeafletTileLayer(
                                    url='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}'
                                ),
                                flc.LeafletFlowLayer(
                                    arcLabelFontSize='18px',
                                    flowData=[
                                        {
                                            'from': {
                                                'lng': source['lng'],
                                                'lat': source['lat']
                                            },
                                            'to': {
                                                'lat': 29.53,
                                                'lng': 106.53
                                            },
                                            'labels': {
                                                'from': source['name'],
                                                'to': '重庆'
                                            }
                                        }
                                        for source in [
                                            {
                                                'name': '北京',
                                                'lat': 39.91,
                                                'lng': 116.41
                                            },
                                            {
                                                'name': '上海',
                                                'lat': 31.23,
                                                'lng': 121.45
                                            },
                                            {
                                                'name': '昆明',
                                                'lat': 24.89,
                                                'lng': 102.83
                                            },
                                            {
                                                'name': '金边',
                                                'lat': 11.54,
                                                'lng': 104.87
                                            }
                                        ]
                                    ]
                                )
                            ],
                            center={
                                'lat': 26.53,
                                'lng': 106.53
                            },
                            zoom=4,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '添加文字标签',
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
        flc.LeafletTileLayer(
            url='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}'
        ),
        flc.LeafletFlowLayer(
            arcLabelFontSize='18px',
            flowData=[
                {
                    'from': {
                        'lng': source['lng'],
                        'lat': source['lat']
                    },
                    'to': {
                        'lat': 29.53,
                        'lng': 106.53
                    },
                    'labels': {
                        'from': source['name'],
                        'to': '重庆'
                    }
                }
                for source in [
                    {
                        'name': '北京',
                        'lat': 39.91,
                        'lng': 116.41
                    },
                    {
                        'name': '上海',
                        'lat': 31.23,
                        'lng': 121.45
                    },
                    {
                        'name': '昆明',
                        'lat': 24.89,
                        'lng': 102.83
                    },
                    {
                        'name': '金边',
                        'lat': 11.54,
                        'lng': 104.87
                    }
                ]
            ]
        )
    ],
    center={
        'lat': 26.53,
        'lng': 106.53
    },
    zoom=4,
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
                    id='添加文字标签',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '更新数据',
                                    id='flow-layer-data-update-demo-trigger',
                                    type='primary'
                                ),
                                flc.LeafletMap(
                                    [
                                        flc.LeafletTileLayer(
                                            url='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}'
                                        ),
                                        flc.LeafletFlowLayer(
                                            id='flow-layer-data-update-demo'
                                        )
                                    ],
                                    center={
                                        'lat': 23.114191,
                                        'lng': 113.265564
                                    },
                                    zoom=4,
                                    style={
                                        'height': 500
                                    }
                                )
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            '动态更新数据',
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
fac.AntdSpace(
    [
        fac.AntdButton(
            '更新数据',
            id='flow-layer-data-update-demo-trigger',
            type='primary'
        ),
        flc.LeafletMap(
            [
                flc.LeafletTileLayer(
                    url='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}'
                ),
                flc.LeafletFlowLayer(
                    id='flow-layer-data-update-demo'
                )
            ],
            center={
                'lat': 23.114191,
                'lng': 113.265564
            },
            zoom=4,
            style={
                'height': 500
            }
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)

...

import random

...

@app.callback(
    Output('flow-layer-data-update-demo', 'flowData'),
    Input('flow-layer-data-update-demo-trigger', 'nClicks')
)
def flow_layer_update_data_demo(nClicks):

    random_points = [
        (random.uniform(90, 130), random.uniform(20, 40))
        for i in range(5)
    ]

    return [
        {
            'from': {
                'lng': point1[0],
                'lat': point1[1]
            },
            'to': {
                'lng': point2[0],
                'lat': point2[1]
            },
            'labels': {
                'from': f'地点{idx1}',
                'to': f'地点{idx2}'
            }
        }
        for idx2, point2 in enumerate(random_points)
        for idx1, point1 in enumerate(random_points)
        if idx1 != idx2
    ]
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
                    id='动态更新数据',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(
                                    url='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}'
                                ),
                                flc.LeafletFlowLayer(
                                    keepUniqueLabels=True,
                                    arcLabelFontSize='20px',
                                    flowData=[
                                        {
                                            'from': {
                                                'lng': source['lng'],
                                                'lat': source['lat']
                                            },
                                            'to': {
                                                'lng': target['lng'],
                                                'lat': target['lat']
                                            },
                                            'labels': {
                                                'from': source['name'],
                                                'to': target['name']
                                            }
                                        }
                                        for source in [
                                            {
                                                'name': '重庆',
                                                'lat': 29.53,
                                                'lng': 106.53
                                            },
                                            {
                                                'name': '北京',
                                                'lat': 39.91,
                                                'lng': 116.41
                                            },
                                            {
                                                'name': '上海',
                                                'lat': 31.23,
                                                'lng': 121.45
                                            }
                                        ]
                                        for target in [
                                            {
                                                'name': '重庆',
                                                'lat': 29.53,
                                                'lng': 106.53
                                            },
                                            {
                                                'name': '北京',
                                                'lat': 39.91,
                                                'lng': 116.41
                                            },
                                            {
                                                'name': '上海',
                                                'lat': 31.23,
                                                'lng': 121.45
                                            }
                                        ]
                                        if source['name'] != target['name']
                                    ]
                                )
                            ],
                            center={
                                'lat': 33.89,
                                'lng': 113.42
                            },
                            zoom=5,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '消除重复标签叠加',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '设置',
                                fac.AntdText(
                                    'keepUniqueLabels=True',
                                    code=True
                                ),
                                '后，地图上的节点标签将会自动移除重复的内容'
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
                    id='消除重复标签叠加',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(
                                    url='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}'
                                ),
                                flc.LeafletFlowLayer(
                                    flowData=[
                                        {
                                            'from': {
                                                'lng': source['lng'],
                                                'lat': source['lat']
                                            },
                                            'to': {
                                                'lat': 29.53,
                                                'lng': 106.53
                                            },
                                            'value': 1 + 0.5 * i
                                        }
                                        for i, source in enumerate(
                                            [
                                                {
                                                    'name': '北京',
                                                    'lat': 39.91,
                                                    'lng': 116.41
                                                },
                                                {
                                                    'name': '上海',
                                                    'lat': 31.23,
                                                    'lng': 121.45
                                                },
                                                {
                                                    'name': '昆明',
                                                    'lat': 24.89,
                                                    'lng': 102.83
                                                },
                                                {
                                                    'name': '金边',
                                                    'lat': 11.54,
                                                    'lng': 104.87
                                                }
                                            ]
                                        )
                                    ]
                                )
                            ],
                            center={
                                'lat': 26.53,
                                'lng': 106.53
                            },
                            zoom=4,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '数值映射宽度',
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
        flc.LeafletTileLayer(
            url='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}'
        ),
        flc.LeafletFlowLayer(
            flowData=[
                {
                    'from': {
                        'lng': source['lng'],
                        'lat': source['lat']
                    },
                    'to': {
                        'lat': 29.53,
                        'lng': 106.53
                    },
                    'value': 1 + 0.5 * i
                }
                for i, source in enumerate(
                    [
                        {
                            'name': '北京',
                            'lat': 39.91,
                            'lng': 116.41
                        },
                        {
                            'name': '上海',
                            'lat': 31.23,
                            'lng': 121.45
                        },
                        {
                            'name': '昆明',
                            'lat': 24.89,
                            'lng': 102.83
                        },
                        {
                            'name': '金边',
                            'lat': 11.54,
                            'lng': 104.87
                        }
                    ]
                )
            ]
        )
    ],
    center={
        'lat': 26.53,
        'lng': 106.53
    },
    zoom=4,
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
                    id='数值映射宽度',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(
                                    url='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}'
                                ),
                                flc.LeafletFlowLayer(
                                    flowData=[
                                        {
                                            'from': {
                                                'lng': source['lng'],
                                                'lat': source['lat']
                                            },
                                            'to': {
                                                'lat': 29.53,
                                                'lng': 106.53
                                            },
                                            'value': 1 + 0.5 * i,
                                            'color': demo_colors[i]
                                        }
                                        for i, source in enumerate(
                                            [
                                                {
                                                    'name': '北京',
                                                    'lat': 39.91,
                                                    'lng': 116.41
                                                },
                                                {
                                                    'name': '上海',
                                                    'lat': 31.23,
                                                    'lng': 121.45
                                                },
                                                {
                                                    'name': '昆明',
                                                    'lat': 24.89,
                                                    'lng': 102.83
                                                },
                                                {
                                                    'name': '金边',
                                                    'lat': 11.54,
                                                    'lng': 104.87
                                                }
                                            ]
                                        )
                                    ]
                                )
                            ],
                            center={
                                'lat': 26.53,
                                'lng': 106.53
                            },
                            zoom=4,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '自定义颜色',
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
demo_colors = ['#2f54eb', '#597ef7', '#85a5ff', '#adc6ff']

...

flc.LeafletMap(
    [
        flc.LeafletTileLayer(
            url='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}'
        ),
        flc.LeafletFlowLayer(
            flowData=[
                {
                    'from': {
                        'lng': source['lng'],
                        'lat': source['lat']
                    },
                    'to': {
                        'lat': 29.53,
                        'lng': 106.53
                    },
                    'value': 1 + 0.5 * i,
                    'color': demo_colors[i]
                }
                for i, source in enumerate(
                    [
                        {
                            'name': '北京',
                            'lat': 39.91,
                            'lng': 116.41
                        },
                        {
                            'name': '上海',
                            'lat': 31.23,
                            'lng': 121.45
                        },
                        {
                            'name': '昆明',
                            'lat': 24.89,
                            'lng': 102.83
                        },
                        {
                            'name': '金边',
                            'lat': 11.54,
                            'lng': 104.87
                        }
                    ]
                )
            ]
        )
    ],
    center={
        'lat': 26.53,
        'lng': 106.53
    },
    zoom=4,
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
                    id='自定义颜色',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'padding': '25px',
                'width': 0
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '基础使用', 'href': '#基础使用'},
                    {'title': '添加文字标签', 'href': '#添加文字标签'},
                    {'title': '动态更新数据', 'href': '#动态更新数据'},
                    {'title': '消除重复标签叠加', 'href': '#消除重复标签叠加'},
                    {'title': '数值映射宽度', 'href': '#数值映射宽度'},
                    {'title': '自定义颜色', 'href': '#自定义颜色'},
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
            component_name='LeafletFlowLayer'
        )
    ],
    id='flow-layer-container',
    style={
        'display': 'flex'
    }
)
