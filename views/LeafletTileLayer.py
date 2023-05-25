import uuid
from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc
import feffery_markdown_components as fmc

import callbacks.LeafletTileLayer
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
                            'title': '底图'
                        },
                        {
                            'title': 'LeafletTileLayer 瓦片底图'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于为底图实例设置单个或多个瓦片底图。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdFormItem(
                            fac.AntdSelect(
                                id='tile-layer-basic-demo-switch-url',
                                options=[
                                    {
                                        'label': url,
                                        'value': url
                                    }
                                    for url in [
                                        'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
                                        'http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineCommunity/MapServer/tile/{z}/{y}/{x}',
                                        'http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetWarm/MapServer/tile/{z}/{y}/{x}',
                                        'http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetGray/MapServer/tile/{z}/{y}/{x}',
                                        'http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}',
                                        'http://thematic.geoq.cn/arcgis/rest/services/ThematicMaps/administrative_division_boundaryandlabel/MapServer/tile/{z}/{y}/{x}',
                                        'http://thematic.geoq.cn/arcgis/rest/services/ThematicMaps/WorldHydroMap/MapServer/tile/{z}/{y}/{x}',
                                        'http://thematic.geoq.cn/arcgis/rest/services/StreetThematicMaps/Gray_OnlySymbol/MapServer/tile/{z}/{y}/{x}',
                                        'http://thematic.geoq.cn/arcgis/rest/services/StreetThematicMaps/Warm_OnlySymbol/MapServer/tile/{z}/{y}/{x}',
                                        'https://rt0.map.gtimg.com/tile?z={z}&x={x}&y={-y}',
                                        'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7',
                                        'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=8&ltype=11',
                                        'https://webst02.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}',
                                        'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
                                        'https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png',
                                        'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png',
                                        'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                                        'https://tile.openstreetmap.bzh/br/{z}/{x}/{y}.png',
                                        'https://tileserver.memomaps.de/tilegen/{z}/{x}/{y}.png',
                                        'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
                                        'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png',
                                        'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png',
                                        'https://tiles.stadiamaps.com/tiles/osm_bright/{z}/{x}/{y}{r}.png',
                                        'https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png',
                                        'https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png',
                                        'https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.{ext}',
                                        'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-background/{z}/{x}/{y}{r}.{ext}',
                                        'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}{r}.{ext}',
                                        'https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}',
                                        'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.{ext}',
                                        'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}{r}.{ext}',
                                        'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
                                        'https://server.arcgisonline.com/ArcGIS/rest/services/Specialty/DeLorme_World_Base_Map/MapServer/tile/{z}/{y}/{x}',
                                        'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
                                        'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                                        'https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}',
                                        'https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}',
                                        'https://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}',
                                        'https://server.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}',
                                        'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}',
                                        'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
                                        'https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png',
                                        'https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}{r}.png',
                                        'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
                                        'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
                                        'https://{s}.basemaps.cartocdn.com/dark_only_labels/{z}/{x}/{y}{r}.png',
                                        'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png'
                                    ]
                                ],
                                defaultValue='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineCommunity/MapServer/tile/{z}/{y}/{x}',
                                allowClear=False,
                                style={
                                    'width': '100%'
                                }
                            ),
                            label='url',
                            style={
                                'marginBottom': 0
                            }
                        ),

                        fac.AntdParagraph(
                            [
                                '当前选中url: ',
                                fac.AntdText(
                                    id='tile-layer-basic-demo-current-url',
                                    copyable=True
                                )
                            ],
                            style={
                                'marginBottom': 0
                            }
                        ),

                        flc.LeafletMap(
                            [
                                flc.LeafletTileLayer(
                                    id='tile-layer-basic-demo'
                                )
                            ],
                            center={
                                'lng': 106,
                                'lat': 29
                            },
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
                                '这个例子展示了常见的公共开放瓦片底图服务（国内公开应用使用时，请注意甄别所用底图是否符合相关地图规范标准），其中部分国内地图服务如高德地图存在坐标偏移（对应火星坐标系），部分国外地图服务国内不可访问或访问缓慢，具体使用时请注意'
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
fac.AntdFormItem(
    fac.AntdSelect(
        id='tile-layer-basic-demo-switch-url',
        options=[
            {
                'label': url,
                'value': url
            }
            for url in [
                'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
                'http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineCommunity/MapServer/tile/{z}/{y}/{x}',
                'http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetWarm/MapServer/tile/{z}/{y}/{x}',
                'http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetGray/MapServer/tile/{z}/{y}/{x}',
                'http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}',
                'http://thematic.geoq.cn/arcgis/rest/services/ThematicMaps/administrative_division_boundaryandlabel/MapServer/tile/{z}/{y}/{x}',
                'http://thematic.geoq.cn/arcgis/rest/services/ThematicMaps/WorldHydroMap/MapServer/tile/{z}/{y}/{x}',
                'http://thematic.geoq.cn/arcgis/rest/services/StreetThematicMaps/Gray_OnlySymbol/MapServer/tile/{z}/{y}/{x}',
                'http://thematic.geoq.cn/arcgis/rest/services/StreetThematicMaps/Warm_OnlySymbol/MapServer/tile/{z}/{y}/{x}',
                'https://rt0.map.gtimg.com/tile?z={z}&x={x}&y={-y}',
                'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7',
                'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=8&ltype=11',
                'https://webst02.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}',
                'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
                'https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png',
                'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png',
                'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                'https://tile.openstreetmap.bzh/br/{z}/{x}/{y}.png',
                'https://tileserver.memomaps.de/tilegen/{z}/{x}/{y}.png',
                'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
                'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png',
                'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png',
                'https://tiles.stadiamaps.com/tiles/osm_bright/{z}/{x}/{y}{r}.png',
                'https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png',
                'https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png',
                'https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.{ext}',
                'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-background/{z}/{x}/{y}{r}.{ext}',
                'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}{r}.{ext}',
                'https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}',
                'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.{ext}',
                'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}{r}.{ext}',
                'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
                'https://server.arcgisonline.com/ArcGIS/rest/services/Specialty/DeLorme_World_Base_Map/MapServer/tile/{z}/{y}/{x}',
                'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
                'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                'https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}',
                'https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}',
                'https://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}',
                'https://server.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}',
                'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}',
                'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
                'https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png',
                'https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}{r}.png',
                'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
                'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
                'https://{s}.basemaps.cartocdn.com/dark_only_labels/{z}/{x}/{y}{r}.png',
                'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png'
            ]
        ],
        defaultValue='https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
        allowClear=False,
        persistence=True,
        style={
            'width': '100%'
        }
    ),
    label='url',
    style={
        'marginBottom': 0
    }
),

fac.AntdParagraph(
    [
        '当前选中url: ',
        fac.AntdText(
            id='tile-layer-basic-demo-current-url',
            copyable=True
        )
    ],
    style={
        'marginBottom': 0
    }
),

flc.LeafletMap(
    [
        flc.LeafletTileLayer(
            id='tile-layer-basic-demo'
        )
    ],
    center={
        'lng': 106,
        'lat': 29
    },
    style={
        'height': 500
    }
)

...

@app.callback(
    Output('tile-layer-basic-demo', 'url'),
    Output('tile-layer-basic-demo-current-url', 'children'),
    Input('tile-layer-basic-demo-switch-url', 'value')
)
def tile_layer_basic_demo_update_url(value):

    return value, value
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
                                    url='http://thematic.geoq.cn/arcgis/rest/services/ThematicMaps/administrative_division_boundaryandlabel/MapServer/tile/{z}/{y}/{x}',
                                    zIndex=3
                                ),
                                flc.LeafletTileLayer(
                                    url='https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=8&ltype=11',
                                    zIndex=2
                                ),
                                flc.LeafletTileLayer(
                                    url='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
                                    zIndex=1
                                )
                            ],
                            center={
                                'lng': 106,
                                'lat': 29
                            },
                            maxZoom=14,
                            style={
                                'height': 500
                            }
                        ),

                        fac.AntdDivider(
                            '叠加多个底图服务',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '同一个地图实例可以叠加多个具有不同内容的底图服务，并通过参数',
                                fac.AntdText(
                                    'zIndex',
                                    code=True
                                ),
                                '协调不同底图服务之间的图层顺序'
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
                                codeBlockStyle={
                                    'overflowX': 'auto',
                                    'width': '100%'
                                },
                                codeString='''
flc.LeafletMap(
    [
        flc.LeafletTileLayer(
            url='http://thematic.geoq.cn/arcgis/rest/services/ThematicMaps/administrative_division_boundaryandlabel/MapServer/tile/{z}/{y}/{x}',
            zIndex=3
        ),
        flc.LeafletTileLayer(
            url='https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=8&ltype=11',
            zIndex=2
        ),
        flc.LeafletTileLayer(
            url='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
            zIndex=1
        )
    ],
    center={
        'lng': 106,
        'lat': 29
    },
    maxZoom=14,
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
                    id='叠加多个底图服务',
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
                    {'title': '叠加多个底图服务', 'href': '#叠加多个底图服务'},
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
            component_name='LeafletTileLayer'
        )
    ],
    id=str(uuid.uuid4()),
    style={
        'display': 'flex'
    }
)
