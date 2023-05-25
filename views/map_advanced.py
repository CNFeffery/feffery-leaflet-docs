import uuid
from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

import callbacks.map_advanced_c
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
                            'title': '基础组件'
                        },
                        {
                            'title': 'LeafletMap 地图容器'
                        },
                        {
                            'title': '进阶功能'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        '地图容器是',
                        fac.AntdText(
                            'flc',
                            strong=True
                        ),
                        '中构建一个地图实例的基础，地图容器通过嵌套其他',
                        fac.AntdText(
                            'flc',
                            strong=True
                        ),
                        '子功能组件来实现更复杂的地图功能。'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                html.Div(
                    id='地图编辑功能'
                ),
                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=13,
                            editToolbar=True,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '基础的地图编辑',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '为',
                                fac.AntdText(
                                    'LeafletMap',
                                    strong=True
                                ),
                                '设置参数',
                                fac.AntdText(
                                    'editToolbar=True',
                                    code=True
                                ),
                                '后，即可开启默认的地图编辑功能，用户可基于地图上放置的编辑工具栏实现相关功能'
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
flc.LeafletMap(
    [
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=13,
    editToolbar=True,
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
                    id='基础的地图编辑',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=13,
                            editToolbar=True,
                            editToolbarControlsOptions={
                                'drawText': True,
                                'cutPolygon': True
                            },
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '开启全部编辑功能',
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
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=13,
    editToolbar=True,
    editToolbarControlsOptions={
        'drawText': True,
        'cutPolygon': True
    },
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
                    id='开启全部编辑功能',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=13,
                            editToolbar=True,
                            editToolbarControlsOptions={
                                'drawText': True,
                                'cutPolygon': True,
                                'oneBlock': True
                            },
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            'oneBlock显示模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '令编辑工具栏全部功能按钮显示在同一容器中'
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
flc.LeafletMap(
    [
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=13,
    editToolbar=True,
    editToolbarControlsOptions={
        'drawText': True,
        'cutPolygon': True,
        'oneBlock': True
    },
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
                    id='oneBlock显示模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=13,
                            editToolbar=True,
                            showMeasurements=True,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '添加测量标注信息',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '当地图编辑功能开启时，设置参数',
                                fac.AntdText(
                                    'showMeasurements=True',
                                    code=True
                                ),
                                '可为部分可测量的矢量绘制过程添加长度、面积标注信息'
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
flc.LeafletMap(
    [
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=13,
    editToolbar=True,
    showMeasurements=True,
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
                    id='添加测量标注信息',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=13,
                            editToolbar=True,
                            maxDrawnShapes=1,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '限制最大可绘制矢量数量',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '通过设置参数',
                                fac.AntdText(
                                    'maxDrawnShapes',
                                    code=True
                                ),
                                '可以限制地图编辑模式下至多可绘制的矢量要素数量，超出限制后新绘制的要素会顶替最早绘制的矢量要素'
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
flc.LeafletMap(
    [
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=13,
    editToolbar=True,
    maxDrawnShapes=1,
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
                    id='限制最大可绘制矢量数量',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            id='leaflet-map-edit-demo',
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=13,
                            editToolbar=True,
                            maxDrawnShapes=3,
                            style={
                                'height': 500
                            }
                        ),

                        html.Pre(
                            id='leaflet-map-edit-demo-output',
                            style={
                                'maxHeight': 300,
                                'overflowY': 'auto',
                                'background': '#f8f9fa'
                            }
                        ),

                        fac.AntdDivider(
                            '回调监听已绘制要素',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '通过监听属性',
                                fac.AntdText(
                                    '_drawnShapes',
                                    code=True
                                ),
                                '的变化可以捕获用户已绘制的部分类型矢量要素数据'
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
        flc.LeafletTileLayer()
    ],
    id='leaflet-map-edit-demo',
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=13,
    editToolbar=True,
    maxDrawnShapes=3,
    style={
        'height': 500
    }
),

html.Pre(
    id='leaflet-map-edit-demo-output',
    style={
        'maxHeight': 300,
        'overflowY': 'auto',
        'background': '#f8f9fa'
    }
)

...

app.clientside_callback(
    '''( _drawnShapes ) => JSON.stringify(_drawnShapes, null, 4)''',
    Output('leaflet-map-edit-demo-output', 'children'),
    Input('leaflet-map-edit-demo', '_drawnShapes'),
    prevent_initial_call=True
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
                    id='回调监听已绘制要素',
                    className='div-highlight'
                ),

                html.Div(id='地图测量功能'),
                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=13,
                            measureControl=True,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '基础的地图测量',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '通过为',
                                fac.AntdText(
                                    'LeafletMap',
                                    strong=True
                                ),
                                '设置参数',
                                fac.AntdText(
                                    'measureControl=True',
                                    code=True
                                ),
                                '可开启长度、面积测量功能'
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
flc.LeafletMap(
    [
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=13,
    measureControl=True,
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
                    id='基础的地图测量',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=13,
                            measureControl=True,
                            measureControlOptions={
                                'activeColor': '#495057',
                                'completedColor': '#1c7ed6'
                            },
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '自定义测量要素颜色',
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
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=13,
    measureControl=True,
    measureControlOptions={
        'activeColor': '#495057',
        'completedColor': '#1c7ed6'
    },
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
                    id='自定义测量要素颜色',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer()
                            ],
                            center={
                                'lng': 106.573344,
                                'lat': 29.560087
                            },
                            zoom=13,
                            viewAutoCorrection=True,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '启用自动地图视角校正',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),
                        fac.AntdParagraph(
                            [
                                '通过为',
                                fac.AntdText(
                                    'LeafletMap',
                                    strong=True
                                ),
                                '设置参数',
                                fac.AntdText(
                                    'viewAutoCorrection=True',
                                    code=True
                                ),
                                '可开启地图视角自动校正功能，从而在地图容器自身尺寸变化时，确保地图更自然的适应新的尺寸，你可以通过折叠左右两侧内容来观察本例与其他例子之间的效果区别'
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
flc.LeafletMap(
    [
        flc.LeafletTileLayer()
    ],
    center={
        'lng': 106.573344,
        'lat': 29.560087
    },
    zoom=13,
    viewAutoCorrection=True,
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
                    id='启用自动地图视角校正',
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
                    {
                        'title': '地图编辑功能',
                        'href': '#地图编辑功能',
                        'children': [
                            {'title': '基础的地图编辑', 'href': '#基础的地图编辑'},
                            {'title': '开启全部编辑功能', 'href': '#开启全部编辑功能'},
                            {'title': 'oneBlock显示模式', 'href': '#oneBlock显示模式'},
                            {'title': '添加测量标注信息', 'href': '#添加测量标注信息'},
                            {'title': '限制最大可绘制矢量数量', 'href': '#限制最大可绘制矢量数量'},
                            {'title': '回调监听已绘制要素', 'href': '#回调监听已绘制要素'},
                        ]
                    },
                    {
                        'title': '地图测量功能',
                        'href': '#地图测量功能',
                        'children': [
                            {'title': '基础的地图测量', 'href': '#基础的地图测量'},
                            {'title': '自定义测量要素颜色', 'href': '#自定义测量要素颜色'}
                        ]
                    },
                    {'title': '启用自动地图视角校正', 'href': '#启用自动地图视角校正'}
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
            component_name='LeafletMap'
        )
    ],
    id=str(uuid.uuid4()),
    style={
        'display': 'flex'
    }
)
