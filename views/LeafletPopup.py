from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

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
                            'title': '附加内容'
                        },
                        {
                            'title': 'LeafletPopup 弹出层'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　用于为矢量图层中各单体要素组件添加额外的弹出层信息内容，通常在用户鼠标点击对应要素后展开。'
                        )
                    ]
                ),

                html.Div(
                    [
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletCircleMarker(
                                    flc.LeafletPopup(
                                        fac.AntdSpace(
                                            [
                                                fac.AntdText(
                                                    'popup示例内容',
                                                    italic=True
                                                ),
                                                fac.AntdProgress(
                                                    percent=80,
                                                    type='circle'
                                                )
                                            ],
                                            direction='vertical'
                                        )
                                    ),
                                    center={
                                        'lng': 0,
                                        'lat': 0
                                    },
                                    radius=25
                                )
                            ],
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
                                '将',
                                fac.AntdText(
                                    'LeafletPopup',
                                    strong=True
                                ),
                                '置于矢量组件中',
                                fac.AntdText(
                                    'LeafletCircleMarker',
                                    strong=True
                                ),
                                '、',
                                fac.AntdText(
                                    'LeafletMarker',
                                    strong=True
                                ),
                                '、',
                                fac.AntdText(
                                    'LeafletPolyline',
                                    strong=True
                                ),
                                '、',
                                fac.AntdText(
                                    'LeafletRectangle',
                                    strong=True
                                ),
                                '、',
                                fac.AntdText(
                                    'LeafletCircle',
                                    strong=True
                                ),
                                '、',
                                fac.AntdText(
                                    'LeafletPolygon',
                                    strong=True
                                ),
                                '的',
                                fac.AntdText(
                                    'children',
                                    strong=True
                                ),
                                '中即可为对应要素组件添加额外的弹出层信息框'
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
        flc.LeafletTileLayer(),
        flc.LeafletCircleMarker(
            flc.LeafletPopup(
                fac.AntdSpace(
                    [
                        fac.AntdText(
                            'popup示例内容',
                            italic=True
                        ),
                        fac.AntdProgress(
                            percent=80,
                            type='circle'
                        )
                    ],
                    direction='vertical'
                )
            ),
            center={
                'lng': 0,
                'lat': 0
            },
            radius=25
        )
    ],
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
                                flc.LeafletCircleMarker(
                                    flc.LeafletPopup(
                                        fac.AntdSpace(
                                            [
                                                fac.AntdText(
                                                    'popup示例内容',
                                                    italic=True
                                                ),
                                                fac.AntdProgress(
                                                    percent=80,
                                                    type='circle'
                                                )
                                            ],
                                            direction='vertical'
                                        ),
                                        closeButton=True
                                    ),
                                    center={
                                        'lng': 0,
                                        'lat': 0
                                    },
                                    radius=25
                                )
                            ],
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '添加关闭按钮',
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
        flc.LeafletCircleMarker(
            flc.LeafletPopup(
                fac.AntdSpace(
                    [
                        fac.AntdText(
                            'popup示例内容',
                            italic=True
                        ),
                        fac.AntdProgress(
                            percent=80,
                            type='circle'
                        )
                    ],
                    direction='vertical'
                ),
                closeButton=True
            ),
            center={
                'lng': 0,
                'lat': 0
            },
            radius=25
        )
    ],
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
                    id='添加关闭按钮',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fuc.FefferyStyle(
                            rawStyle='''
.custom-popup-demo .leaflet-popup-content-wrapper {
    background: linear-gradient(135deg,#abdcff,#0396ff);
    border-radius: 4px;
    opacity: 0.8;
    font-size: 16px;
    white-space: break-spaces;
}

/*隐藏小箭头*/
.custom-popup-demo .leaflet-popup-tip-container {
    display: none;
}
'''
                        ),
                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(),
                                flc.LeafletCircleMarker(
                                    flc.LeafletPopup(
                                        fac.AntdParagraph(
                                            '''君不见黄河之水天上来，奔流到海不复回。
君不见高堂明镜悲白发，朝如青丝暮成雪。
人生得意须尽欢，莫使金樽空对月。
天生我材必有用，千金散尽还复来。
''',
                                            strong=True,
                                            style={
                                                'width': 305,
                                                'color': 'white'
                                            }
                                        ),
                                        className='custom-popup-demo'
                                    ),
                                    center={
                                        'lng': 0,
                                        'lat': 0
                                    },
                                    radius=25
                                )
                            ],
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '自定义容器样式',
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
fuc.FefferyStyle(
    rawStyle='''
.custom-popup-demo .leaflet-popup-content-wrapper {
    background: linear-gradient(135deg,#abdcff,#0396ff);
    border-radius: 4px;
    opacity: 0.8;
    font-size: 16px;
    white-space: break-spaces;
}

/*隐藏小箭头*/
.custom-popup-demo .leaflet-popup-tip-container {
    display: none;
}
'''
),
flc.LeafletMap(
    [
        flc.LeafletTileLayer(),
        flc.LeafletCircleMarker(
            flc.LeafletPopup(
                fac.AntdParagraph(
                    '''君不见黄河之水天上来，奔流到海不复回。
君不见高堂明镜悲白发，朝如青丝暮成雪。
人生得意须尽欢，莫使金樽空对月。
天生我材必有用，千金散尽还复来。
''',
                    strong=True,
                    style={
                        'width': 305,
                        'color': 'white'
                    }
                ),
                className='custom-popup-demo'
            ),
            center={
                'lng': 0,
                'lat': 0
            },
            radius=25
        )
    ],
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
                    id='自定义容器样式',
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
                    {'title': '添加关闭按钮', 'href': '#添加关闭按钮'},
                    {'title': '自定义容器样式', 'href': '#自定义容器样式'},
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
            component_name='LeafletPopup'
        )
    ],
    style={
        'display': 'flex'
    }
)
