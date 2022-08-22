import re
import dash
import random
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
                            flc.LeafletMapAction(
                                id='action-callback',
                            )
                        ],
                        style={
                            'height': '100%'
                        }
                    ),
                    fac.AntdSpace(
                        [
                            fac.AntdButton(
                                '随机set-zoom',
                                id='action-set-zoom',
                                type='primary',
                                block=True,
                                size='small'
                            ),
                            fac.AntdButton(
                                'zoom-in一单位',
                                id='action-zoom-in',
                                type='primary',
                                block=True,
                                size='small'
                            ),
                            fac.AntdButton(
                                'zoom-out一单位',
                                id='action-zoom-out',
                                type='primary',
                                block=True,
                                size='small'
                            ),
                            fac.AntdButton(
                                '随机fly-to',
                                id='action-fly-to',
                                type='primary',
                                block=True,
                                size='small'
                            ),
                            fac.AntdButton(
                                'fly-to-bounds',
                                id='action-fly-to-bounds',
                                type='primary',
                                block=True,
                                size='small'
                            )
                        ],
                        direction='vertical',
                        style={
                            'position': 'absolute',
                            'bottom': '25px',
                            'right': '25px',
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
                                    'LeafletMapAction参数说明',
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
                                    open('documents/LeafletMapAction.md', encoding='utf-8')
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
import dash
import random
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
                                
html.Div(
    [
        flc.LeafletMap(
            [
                flc.LeafletTileLayer(),
                flc.LeafletMapAction(
                    id='action-callback',
                )
            ],
            style={
                'height': '100%'
            }
        ),
        fac.AntdSpace(
            [
                fac.AntdButton(
                    '随机set-zoom',
                    id='action-set-zoom',
                    type='primary',
                    block=True,
                    size='small'
                ),
                fac.AntdButton(
                    'zoom-in一单位',
                    id='action-zoom-in',
                    type='primary',
                    block=True,
                    size='small'
                ),
                fac.AntdButton(
                    'zoom-out一单位',
                    id='action-zoom-out',
                    type='primary',
                    block=True,
                    size='small'
                ),
                fac.AntdButton(
                    '随机fly-to',
                    id='action-fly-to',
                    type='primary',
                    block=True,
                    size='small'
                ),
                fac.AntdButton(
                    'fly-to-bounds',
                    id='action-fly-to-bounds',
                    type='primary',
                    block=True,
                    size='small'
                )
            ],
            direction='vertical',
            style={
                'position': 'absolute',
                'bottom': '25px',
                'right': '25px',
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
    Output('action-callback', 'mapActionConfig'),
    [Input('action-set-zoom', 'nClicks'),
     Input('action-zoom-in', 'nClicks'),
     Input('action-zoom-out', 'nClicks'),
     Input('action-fly-to', 'nClicks'),
     Input('action-fly-to-bounds', 'nClicks')],
    prevent_initiall_call=True
)
def action_callback(*nClicks):
    # 请保证dash版本 >= 2.4.0
    trigger_id = dash.ctx.triggered_id

    if trigger_id == 'action-set-zoom':
        return {
            'type': 'set-zoom',
            'zoom': random.randint(0, 18)
        }

    elif trigger_id == 'action-zoom-in':
        return {
            'type': 'zoom-in',
            'zoomInOffset': 1
        }

    elif trigger_id == 'action-zoom-out':
        return {
            'type': 'zoom-out',
            'zoomOutOffset': 1
        }

    elif trigger_id == 'action-fly-to':
        return {
            'type': 'fly-to',
            'zoom': random.randint(0, 18),
            'center': {
                'lng': random.uniform(-180, 180),
                'lat': random.uniform(-90, 90)
            }
        }

    elif trigger_id == 'action-fly-to-bounds':

        return {
            'type': 'fly-to-bounds',
            'bounds': {
                'minx': 103.5,
                'miny': 29.5,
                'maxx': 109,
                'maxy': 31.5,
            }
        }
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
    id='LeafletMapAction-basic-callback-container',
    sizes=[60, 40],
    gutterSize=10,
    style={
        'height': '100%'
    }
)


@app.callback(
    Output('action-callback', 'mapActionConfig'),
    [Input('action-set-zoom', 'nClicks'),
     Input('action-zoom-in', 'nClicks'),
     Input('action-zoom-out', 'nClicks'),
     Input('action-fly-to', 'nClicks'),
     Input('action-fly-to-bounds', 'nClicks')],
    prevent_initiall_call=True
)
def action_callback(*nClicks):
    trigger_id = dash.ctx.triggered_id

    if trigger_id == 'action-set-zoom':
        return {
            'type': 'set-zoom',
            'zoom': random.randint(0, 18)
        }

    elif trigger_id == 'action-zoom-in':
        return {
            'type': 'zoom-in',
            'zoomInOffset': 1
        }

    elif trigger_id == 'action-zoom-out':
        return {
            'type': 'zoom-out',
            'zoomOutOffset': 1
        }

    elif trigger_id == 'action-fly-to':
        return {
            'type': 'fly-to',
            'zoom': random.randint(0, 18),
            'center': {
                'lng': random.uniform(-180, 180),
                'lat': random.uniform(-90, 90)
            }
        }

    elif trigger_id == 'action-fly-to-bounds':

        return {
            'type': 'fly-to-bounds',
            'bounds': {
                'minx': 103.5,
                'miny': 29.5,
                'maxx': 109,
                'maxy': 31.5,
            }
        }
