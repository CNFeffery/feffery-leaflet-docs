class Config:

    # 顶端进度条需要纳入的监听目标
    include_props = [
        'docs-content.children'
    ]

    # 定义侧边菜单树状结构数据
    menuItems = [
        {
            'component': 'ItemGroup',
            'props': {
                'key': '/',
                'title': '快速入门'
            },
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': '/what-is-flc',
                        'name': '/what-is-flc',
                        'href': '/what-is-flc',
                        'title': 'flc是什么？'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/getting-started',
                        'name': '/getting-started',
                        'href': '/getting-started',
                        'title': 'flc快速上手'
                    }
                }
            ]
        },
        {
            'component': 'Divider',
            'props': {
                'dashed': True
            }
        },
        {
            'component': 'ItemGroup',
            'props': {
                'key': '组件介绍',
                'title': '组件介绍'
            },
            'children': [
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '基础组件',
                        'title': '基础组件'
                    },
                    'children': [
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '基础组件/地图容器',
                                'title': 'LeafletMap 地图容器'
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/LeafletMap-basic',
                                        'name': '/LeafletMap-basic',
                                        'title': '基础功能',
                                        'href': '/LeafletMap-basic'
                                    }
                                },
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '/LeafletMap-advanced',
                                        'name': '/LeafletMap-advanced',
                                        'title': '进阶功能',
                                        'href': '/LeafletMap-advanced'
                                    }
                                },
                            ]
                        }
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '底图',
                        'title': '底图'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletTileLayer',
                                'name': '/LeafletTileLayer',
                                'title': 'LeafletTileLayer 瓦片底图',
                                'href': '/LeafletTileLayer'
                            }
                        },
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '矢量',
                        'title': '矢量'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletCircleMarker',
                                'name': '/LeafletCircleMarker',
                                'title': 'LeafletCircleMarker 圆形标记',
                                'href': '/LeafletCircleMarker'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletMarker',
                                'name': '/LeafletMarker',
                                'title': 'LeafletMarker 标记',
                                'href': '/LeafletMarker'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletPolyline',
                                'name': '/LeafletPolyline',
                                'title': 'LeafletPolyline 折线',
                                'href': '/LeafletPolyline'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletRectangle',
                                'name': '/LeafletRectangle',
                                'title': 'LeafletRectangle 矩形',
                                'href': '/LeafletRectangle'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletCircle',
                                'name': '/LeafletCircle',
                                'title': 'LeafletCircle 圆形',
                                'href': '/LeafletCircle'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletPolygon',
                                'name': '/LeafletPolygon',
                                'title': 'LeafletPolygon 多边形',
                                'href': '/LeafletPolygon'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletGeoJSON',
                                'name': '/LeafletGeoJSON',
                                'title': 'LeafletGeoJSON GeoJSON要素',
                                'href': '/LeafletGeoJSON'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletVectorTile',
                                'name': '/LeafletVectorTile',
                                'title': 'LeafletVectorTile 矢量切片',
                                'href': '/LeafletVectorTile',
                                'disabled': True
                            }
                        },
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '附加内容',
                        'title': '附加内容'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletTooltip',
                                'name': '/LeafletTooltip',
                                'title': 'LeafletTooltip 提示框',
                                'href': '/LeafletTooltip'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletPopup',
                                'name': '/LeafletPopup',
                                'title': 'LeafletPopup 弹出层',
                                'href': '/LeafletPopup'
                            }
                        },
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '容器',
                        'title': '容器'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletFeatureGroup',
                                'name': '/LeafletFeatureGroup',
                                'title': 'LeafletFeatureGroup 要素组',
                                'href': '/LeafletFeatureGroup'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletLayerGroup',
                                'name': '/LeafletLayerGroup',
                                'title': 'LeafletLayerGroup 图层组',
                                'href': '/LeafletLayerGroup',
                                'disabled': True
                            }
                        },
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '特殊图层',
                        'title': '特殊图层'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletAntPath',
                                'name': '/LeafletAntPath',
                                'title': 'LeafletAntPath 蚂蚁路径',
                                'href': '/LeafletAntPath',
                                'disabled': True
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletFlowLayer',
                                'name': '/LeafletFlowLayer',
                                'title': 'LeafletFlowLayer 流线图',
                                'href': '/LeafletFlowLayer',
                                'disabled': True
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletHeatMap',
                                'name': '/LeafletHeatMap',
                                'title': 'LeafletHeatMap 热力图',
                                'href': '/LeafletHeatMap'
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletStaticHeatMap',
                                'name': '/LeafletStaticHeatMap',
                                'title': 'LeafletStaticHeatMap 静态热力图',
                                'href': '/LeafletStaticHeatMap',
                                'disabled': True
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletSuperCluster',
                                'name': '/LeafletSuperCluster',
                                'title': 'LeafletSuperCluster 巨量标记聚类',
                                'href': '/LeafletSuperCluster',
                                'disabled': True
                            }
                        },
                    ]
                },
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '特殊功能',
                        'title': '特殊功能'
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletExport',
                                'name': '/LeafletExport',
                                'title': 'LeafletExport 图片导出',
                                'href': '/LeafletExport',
                                'disabled': True
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletFullscreenControl',
                                'name': '/LeafletFullscreenControl',
                                'title': 'LeafletFullscreenControl 全屏化',
                                'href': '/LeafletFullscreenControl',
                                'disabled': True
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletMapAction',
                                'name': '/LeafletMapAction',
                                'title': 'LeafletMapAction 地图动作执行',
                                'href': '/LeafletMapAction',
                                'disabled': True
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletMapListener',
                                'name': '/LeafletMapListener',
                                'title': 'LeafletMapListener 地图事件监听',
                                'href': '/LeafletMapListener',
                                'disabled': True
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletMiniMap',
                                'name': '/LeafletMiniMap',
                                'title': 'LeafletMiniMap 缩略地图',
                                'href': '/LeafletMiniMap',
                                'disabled': True
                            }
                        },
                        {
                            'component': 'Item',
                            'props': {
                                'key': '/LeafletTileSelect',
                                'name': '/LeafletTileSelect',
                                'title': 'LeafletTileSelect 底图选择器',
                                'href': '/LeafletTileSelect',
                                'disabled': True
                            }
                        }
                    ]
                }
            ]
        },
        # {
        #     'component': 'Divider',
        #     'props': {
        #         'dashed': True
        #     }
        # },
        # {
        #     'component': 'ItemGroup',
        #     'props': {
        #         'key': '进阶使用',
        #         'title': '进阶使用'
        #     },
        #     'children': [
        #         {
        #             'component': 'Item',
        #             'props': {
        #                 'key': '/advanced-classname',
        #                 'name': '/advanced-classname',
        #                 'title': '进阶className的使用',
        #                 'href': '/advanced-classname'
        #             }
        #         }
        #     ]
        # },
        # {
        #     'component': 'ItemGroup',
        #     'props': {
        #         'key': '更新日志',
        #         'title': '更新日志'
        #     },
        #     'children': [
        #         {
        #             'component': 'SubMenu',
        #             'props': {
        #                 'key': 'v0.1.x',
        #                 'title': 'v0.1.x'
        #             },
        #             'children': [
        #                 {
        #                     'component': 'Item',
        #                     'props': {
        #                         'key': '/change-log-v0.1.0',
        #                         'title': 'v0.1.0',
        #                         'href': '/change-log-v0.1.0'
        #                     }
        #                 }
        #             ]
        #         }
        #     ]
        # }
    ]

    # 定义位于折叠菜单中的菜单项默认需展开菜单key值列表
    key2open_keys = {
        '/LeafletMap-basic': ['基础组件', '基础组件/地图容器'],
        '/LeafletMap-advanced': ['基础组件', '基础组件/地图容器'],
        '/LeafletTileLayer': ['底图'],
        '/LeafletCircleMarker': ['矢量'],
        '/LeafletMarker': ['矢量'],
        '/LeafletPolyline': ['矢量'],
        '/LeafletRectangle': ['矢量'],
        '/LeafletCircle': ['矢量'],
        '/LeafletPolygon': ['矢量'],
        '/LeafletGeoJSON': ['矢量'],
        '/LeafletTooltip': ['附加内容'],
        '/LeafletPopup': ['附加内容'],
        '/LeafletFeatureGroup': ['容器'],
        '/LeafletLayerGroup': ['容器'],
        '/LeafletAntPath': ['特殊图层'],
        '/LeafletFlowLayer': ['特殊图层'],
        '/LeafletHeatMap': ['特殊图层'],
        '/LeafletStaticHeatMap': ['特殊图层'],
        '/LeafletSuperCluster': ['特殊图层'],
        '/LeafletExport': ['特殊功能'],
        '/LeafletFullscreenControl': ['特殊功能'],
        '/LeafletMapAction': ['特殊功能'],
        '/LeafletMapListener': ['特殊功能'],
        '/LeafletMiniMap': ['特殊功能'],
        '/LeafletTileSelect': ['特殊功能'],
    }

    # 注入侧边菜单栏默认展开子菜单
    side_menu_open_keys = [
    ]
