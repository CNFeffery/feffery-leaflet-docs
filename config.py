class Config:
    # 侧边菜单树状结构数据
    side_menu_items = [
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
                        'href': '/what-is-flc',
                        'title': 'flc是什么？'
                    }
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': '/getting-started',
                        'href': '/getting-started',
                        'title': 'flc快速上手'
                    }
                }
            ]
        },
        *[
            {
                'component': 'SubMenu',
                'props': {
                    'key': '基础组件',
                    'href': '基础组件',
                    'title': '基础组件'
                },
                'children': [
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletMap',
                            'title': 'LeafletMap 地图容器',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletMap/basic',
                                    'href': '/LeafletMap/basic',
                                    'title': '基础地图容器',
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletMap/custom-center-zoom',
                                    'href': '/LeafletMap/custom-center-zoom',
                                    'title': '设置地图中心与缩放级别',
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletMap/custom-zoom-delta',
                                    'href': '/LeafletMap/custom-zoom-delta',
                                    'title': '自定义地图缩放粒度',
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletMap/edit-mode',
                                    'href': '/LeafletMap/edit-mode',
                                    'title': '编辑模式',
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletMap/edit-mode-callback',
                                    'href': '/LeafletMap/edit-mode-callback',
                                    'title': '编辑模式回调示例',
                                }
                            }
                        ]
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletMapListener',
                            'title': 'LeafletMapListener 地图事件监听',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletMapListener/basic-callback',
                                    'href': '/LeafletMapListener/basic-callback',
                                    'title': '监听常用地图事件',
                                }
                            }
                        ]
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletMapAction',
                            'title': 'LeafletMapAction 地图动作执行',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletMapAction/basic-callback',
                                    'href': '/LeafletMapAction/basic-callback',
                                    'title': '常用地图动作',
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletMapAction/resize',
                                    'href': '/LeafletMapAction/resize',
                                    'title': '容器resize后校正地图视角',
                                }
                            }
                        ]
                    }
                ]
            },
            {
                'component': 'SubMenu',
                'props': {
                    'key': '栅格类图层',
                    'href': '栅格类图层',
                    'title': '栅格类图层'
                },
                'children': [
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletTileLayer',
                            'title': 'LeafletTileLayer 瓦片地图图层',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletTileLayer/basic',
                                    'href': '/LeafletTileLayer/basic',
                                    'title': '使用不同的瓦片底图源',
                                }
                            }
                        ]
                    }
                ]
            },
            {
                'component': 'SubMenu',
                'props': {
                    'key': '矢量类图层',
                    'href': '矢量类图层',
                    'title': '矢量类图层'
                },
                'children': [
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletCircleMarker',
                            'title': 'LeafletCircleMarker 圆形标记图层',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletCircleMarker/basic',
                                    'href': '/LeafletCircleMarker/basic',
                                    'title': '基础圆形标记'
                                }
                            }
                        ]
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletPolyline',
                            'title': 'LeafletPolyline 折线图层',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletPolyline/basic',
                                    'href': '/LeafletPolyline/basic',
                                    'title': '基础折线'
                                }
                            }
                        ]
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletRectangle',
                            'title': 'LeafletRectangle 矩形图层',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletRectangle/basic',
                                    'href': '/LeafletRectangle/basic',
                                    'title': '基础矩形'
                                }
                            }
                        ]
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletCircle',
                            'href': '/LeafletCircle',
                            'title': 'LeafletCircle 圆形图层',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletCircle/basic',
                                    'href': '/LeafletCircle/basic',
                                    'title': '基础圆形'
                                }
                            }
                        ]
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletPolygon',
                            'href': '/LeafletPolygon',
                            'title': 'LeafletPolygon 多边形图层',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletPolygon/basic',
                                    'href': '/LeafletPolygon/basic',
                                    'title': '基础多边形'
                                }
                            }
                        ]
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletGeoJSON',
                            'href': '/LeafletGeoJSON',
                            'title': 'LeafletGeoJSON GeoJSON图层',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletGeoJSON/basic',
                                    'href': '/LeafletGeoJSON/basic',
                                    'title': '基础GeoJSON'
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletGeoJSON/click-feature-zoom',
                                    'href': '/LeafletGeoJSON/click-feature-zoom',
                                    'title': '点击要素自适应缩放'
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletGeoJSON/show-feature-tooltip',
                                    'href': '/LeafletGeoJSON/show-feature-tooltip',
                                    'title': '鼠标悬浮展示信息卡片'
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletGeoJSON/selectable-single',
                                    'href': '/LeafletGeoJSON/selectable-single',
                                    'title': '单选模式'
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletGeoJSON/selectable-multiple',
                                    'href': '/LeafletGeoJSON/selectable-multiple',
                                    'title': '多选模式'
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletGeoJSON/basic-choropleth',
                                    'href': '/LeafletGeoJSON/basic-choropleth',
                                    'title': '基础分层设色'
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletGeoJSON/basic-category',
                                    'href': '/LeafletGeoJSON/basic-category',
                                    'title': '基础分类设色'
                                }
                            }
                        ]
                    },
                ]
            },
            {
                'component': 'SubMenu',
                'props': {
                    'key': '特殊图层',
                    'href': '特殊图层',
                    'title': '特殊图层'
                },
                'children': [
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletHeatMap',
                            'title': 'LeafletHeatMap 热力图层',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletHeatMap/basic',
                                    'href': '/LeafletHeatMap/basic',
                                    'title': '基础热力图层'
                                }
                            }
                        ]
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/LeafletFlowLayer',
                            'title': 'LeafletFlowLayer 流线图层',
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/LeafletFlowLayer/basic',
                                    'href': '/LeafletFlowLayer/basic',
                                    'title': '基础流线图层'
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    ]
