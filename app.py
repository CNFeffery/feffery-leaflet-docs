import dash
from dash import html, dcc
import feffery_antd_components as fac
import feffery_leaflet_components as flc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

import views
from server import app, server
from config import Config

app.layout = fuc.FefferyTopProgress(
    html.Div(
        [
            # 注入url监听
            dcc.Location(id='url'),

            # 页面结构
            fac.AntdRow(
                [
                    fac.AntdCol(
                        html.Img(
                            src=app.get_asset_url(
                                'imgs/flc-logo.svg'),
                            style={
                                'height': '50px',
                                'padding': '0 10px',
                                'marginTop': '7px'
                            }
                        ),
                    ),
                    fac.AntdCol(
                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    'feffery-leaflet-components',
                                    strong=True,
                                    style={
                                        'fontSize': '35px'
                                    }
                                ),
                                fac.AntdText(
                                    f'v{flc.__version__}',
                                    style={
                                        'fontSize': '10px',
                                        'paddingLeft': '2px'
                                    }
                                )
                            ]
                        )
                    ),

                    fac.AntdCol(
                        html.Div(
                            [
                                html.A(
                                    fac.AntdImage(
                                        alt='flc源码仓库，欢迎star',
                                        src='https://img.shields.io/github/stars/CNFeffery/feffery-leaflet-components?style=social',
                                        preview=False,
                                        fallback=None,
                                        style={
                                            'transform': 'translateY(0px) scale(1.25)'
                                        }
                                    ),
                                    href='https://github.com/CNFeffery/feffery-leaflet-components',
                                    target='_blank',
                                    style={
                                        'cursor': 'pointer'
                                    }
                                ),

                                html.A(
                                    '皖ICP备2021012734号-1',
                                    href='https://beian.miit.gov.cn/',
                                    target='_blank',
                                    style={
                                        'fontSize': '10px',
                                        'marginLeft': '50px',
                                        'color': '#494f54'
                                    }
                                )
                            ],
                            style={
                                'float': 'right',
                                'paddingRight': '20px',
                                'marginTop': '20.5px'
                            }
                        ),
                        flex='auto'
                    )
                ],
                align="middle",
                style={
                    'height': '64px',
                    'boxShadow': 'rgb(240 241 242) 0px 2px 14px',
                    'background': 'white',
                    'marginBottom': '5px',
                }
            ),

            fac.AntdRow(
                [
                    fac.AntdCol(
                        html.Div(
                            fac.AntdMenu(
                                id='router-menu',
                                menuItems=Config.side_menu_items,
                                mode='inline',
                                defaultSelectedKey='/LeafletMap/basic',
                                defaultOpenKeys=[
                                    '基础组件', '栅格类图层', '矢量类图层', '特殊图层'
                                ],
                                style={
                                    'height': '100%',
                                    'overflow': 'hidden auto',
                                    'paddingBottom': '50px'
                                }
                            ),
                            id='side-menu',
                            style={
                                'width': '300px',
                                'height': '100%',
                                'overflowY': 'auto'
                            }
                        ),
                        flex='none',
                        style={
                            'height': '100%'
                        }
                    ),

                    fac.AntdCol(
                        id='docs-content',
                        flex='auto',
                        style={
                            'height': '100%'
                        }
                    )
                ],
                wrap=False,
                style={
                    'height': 'calc(100vh - 69px)'
                }
            )
        ]
    ),
    listenPropsMode='include',
    includeProps=[
        'docs-content.children'
    ],
    minimum=0.33,
    speed=800,
    debug=True
)


@app.callback(
    [Output('docs-content', 'children'),
     Output('router-menu', 'currentKey'),
     Output('router-menu', 'openKeys')],
    Input('url', 'pathname'),
    State('router-menu', 'openKeys')
)
def router(pathname, openKeys):
    '''
    路由回调
    '''

    if pathname in ['/what-is-flc', '/']:
        return fac.AntdResult(status='403', title='当前页面建设中...'), '/what-is-flc', openKeys

    elif pathname == '/getting-started':
        return fac.AntdResult(status='403', title='当前页面建设中...'), pathname, openKeys

    elif pathname.startswith('/LeafletMap/'):

        if pathname == '/LeafletMap/basic':
            return views.LeafletMap.basic.docs_content, pathname, ['/LeafletMap'] + openKeys

        elif pathname == '/LeafletMap/custom-center-zoom':
            return views.LeafletMap.custom_center_zoom.docs_content, pathname, ['/LeafletMap'] + openKeys

        elif pathname == '/LeafletMap/custom-zoom-delta':
            return views.LeafletMap.custom_zoom_delta.docs_content, pathname, ['/LeafletMap'] + openKeys

        elif pathname == '/LeafletMap/edit-mode':
            return views.LeafletMap.edit_mode.docs_content, pathname, ['/LeafletMap'] + openKeys

        elif pathname == '/LeafletMap/edit-mode-callback':
            return views.LeafletMap.edit_mode_callback.docs_content, pathname, ['/LeafletMap'] + openKeys

    elif pathname.startswith('/LeafletMapListener/'):

        if pathname == '/LeafletMapListener/basic-callback':
            return views.LeafletMapListener.basic_callback.docs_content, pathname, ['/LeafletMapListener'] + openKeys

    elif pathname.startswith('/LeafletMapAction/'):

        if pathname == '/LeafletMapAction/basic-callback':
            return views.LeafletMapAction.basic_callback.docs_content, pathname, ['/LeafletMapAction'] + openKeys

        elif pathname == '/LeafletMapAction/resize':
            return views.LeafletMapAction.resize.docs_content, pathname, ['/LeafletMapAction'] + openKeys

    elif pathname.startswith('/LeafletTileLayer/'):

        if pathname == '/LeafletTileLayer/basic':
            return views.LeafletTileLayer.basic_callback.docs_content, pathname, ['/LeafletTileLayer'] + openKeys

    elif pathname.startswith('/LeafletCircleMarker/'):

        if pathname == '/LeafletCircleMarker/basic':
            return views.LeafletCircleMarker.basic.docs_content, pathname, ['/LeafletCircleMarker'] + openKeys

    elif pathname.startswith('/LeafletPolyline/'):

        if pathname == '/LeafletPolyline/basic':
            return views.LeafletPolyline.basic.docs_content, pathname, ['/LeafletPolyline'] + openKeys

    elif pathname.startswith('/LeafletRectangle/'):

        if pathname == '/LeafletRectangle/basic':
            return views.LeafletRectangle.basic.docs_content, pathname, ['/LeafletRectangle'] + openKeys

    elif pathname.startswith('/LeafletCircle/'):

        if pathname == '/LeafletCircle/basic':
            return views.LeafletCircle.basic.docs_content, pathname, ['/LeafletCircle'] + openKeys

    elif pathname.startswith('/LeafletPolygon/'):

        if pathname == '/LeafletPolygon/basic':
            return views.LeafletPolygon.basic.docs_content, pathname, ['/LeafletPolygon'] + openKeys

    elif pathname.startswith('/LeafletGeoJSON/'):

        if pathname == '/LeafletGeoJSON/basic':
            return views.LeafletGeoJSON.basic.docs_content, pathname, ['/LeafletGeoJSON'] + openKeys
        elif pathname == '/LeafletGeoJSON/click-feature-zoom':
            return views.LeafletGeoJSON.click_feature_zoom.docs_content, pathname, ['/LeafletGeoJSON'] + openKeys
        elif pathname == '/LeafletGeoJSON/show-feature-tooltip':
            return views.LeafletGeoJSON.show_feature_tooltip.docs_content, pathname, ['/LeafletGeoJSON'] + openKeys
        elif pathname == '/LeafletGeoJSON/selectable-single':
            return views.LeafletGeoJSON.selectable_single.docs_content, pathname, ['/LeafletGeoJSON'] + openKeys
        elif pathname == '/LeafletGeoJSON/selectable-multiple':
            return views.LeafletGeoJSON.selectable_multiple.docs_content, pathname, ['/LeafletGeoJSON'] + openKeys
        elif pathname == '/LeafletGeoJSON/basic-choropleth':
            return views.LeafletGeoJSON.basic_choropleth.docs_content, pathname, ['/LeafletGeoJSON'] + openKeys
        elif pathname == '/LeafletGeoJSON/basic-category':
            return views.LeafletGeoJSON.basic_category.docs_content, pathname, ['/LeafletGeoJSON'] + openKeys

    elif pathname.startswith('/LeafletHeatMap/'):

        if pathname == '/LeafletHeatMap/basic':
            return views.LeafletHeatMap.basic.docs_content, pathname, ['/LeafletHeatMap'] + openKeys

    elif pathname.startswith('/LeafletFlowLayer/'):

        if pathname == '/LeafletFlowLayer/basic':
            return views.LeafletFlowLayer.basic.docs_content, pathname, ['/LeafletFlowLayer'] + openKeys

    return fac.AntdResult(status='404', title='您访问的页面不存在！'), pathname, dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
