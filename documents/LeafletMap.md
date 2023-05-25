**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的其他地图子组件*

**center：** *dict*型，默认为`{'lng': 0, 'lat': 0}`

　　用于*设置初始化时地图的中心经纬度坐标*，格式为`{'lng': 经度, 'lat': 纬度}`

**zoom：** *int*或*float*型，默认为`3`

　　用于*设置初始化时地图的缩放级别*

**doubleClickZoom：** *bool*型，默认为`True`

　　用于*设置是否允许双击地图进行放大*

**dragging：** *bool*型，默认为`True`

　　用于*设置是否允许鼠标拖拽移动地图*

**closePopupOnClick：** *bool*型，默认为`True`

　　用于*设置是否允许通过点击地图空白处的方式关闭已展开的popup卡片*

**minZoom：** *int*或*float*型，默认为`0`

　　用于*设置地图允许的缩放级别下限*

**maxZoom：** *int*或*float*型，默认为`18`

　　用于*设置地图允许的缩放级别上限*

**zoomDelta：** *int*或*float*型，默认为`1`

　　用于*设置地图层级缩放变化的最小单位*

**zoomControl：** *bool*型，默认为`True`

　　用于*设置是否在地图上放置地图放缩控件*

**scrollWheelZoom：** *bool*或*string*型，默认为`True`

　　用于*设置是否允许通过鼠标滑轮控制地图缩放*，当设置为`'center'`时，无论鼠标位置在哪都会以地图中心为缩放中心

**wheelPxPerZoomLevel：** *int*型，默认为`60`

　　用于*设置触发1单位zoomDelta变化对应的鼠标滑轮滚动像素偏移量*

**smoothWheelZoom：** *bool*或*string*型，默认为`False`

　　用于*设置是否允许通过鼠标滑轮控制地图丝滑缩放*，当设置为`'center'`时，无论鼠标位置在哪都会以地图中心为丝滑缩放中心

**maxBounds：** *dict*型

　　用于*为当前地图设置允许移动的坐标范围*，可用的键值对参数有：

- **minx：** *int*或*float*型，用于*设置坐标范围对应的经度下限*
- **miny：** *int*或*float*型，用于*设置坐标范围对应的纬度下限*
- **maxx：** *int*或*float*型，用于*设置坐标范围对应的经度上限*
- **maxy：** *int*或*float*型，用于*设置坐标范围对应的纬度上限*

**editToolbar：** *bool*型，默认为`False`

　　用于*设置是否开启地图编辑功能*，开启后会在地图上放置编辑工具栏

**editToolbarControlsOptions：** *dict*型

　　用于*配置编辑工具栏相关参数*，可用的键值对参数有：

- **position：** *string*型，默认为`'topleft'`，用于*设置编辑模式工具栏的方位*，可选的有`'topleft'`、`'topright'`、`'bottomleft'`、`'bottomright'`
- **drawMarker：** *bool*型，默认为`True`，用于*设置是否开启“添加标记点”功能*
- **drawCircleMarker：** *bool*型，默认为`True`，用于*设置是否开启”圆形标记点“绘制功能*
- **drawPolyline：** *bool*型，默认为`True`，用于*设置是否开启”折线“绘制功能*
- **drawRectangle：** *bool*型，默认为`True`，用于*设置是否开启”矩形“绘制功能*
- **drawPolygon：** *bool*型，默认为`True`，用于*设置是否开启“多边形”绘制功能*
- **drawCircle：** *bool*型，默认为`True`，用于*设置是否开启“圆形”绘制功能*
- **drawText：** *bool*型，默认为`False`，用于*设置是否开启“添加文字”功能*
- **editMode：** *bool*型，默认为`True`，用于*设置是否开启“编辑要素”功能*
- **dragMode：** *bool*型，默认为`True`，用于*设置是否开启“拖拽要素”功能*
- **cutPolygon：** *bool*型，默认为`False`，用于*设置是否开启“剪切要素”功能*
- **removalMode：** *bool*型，默认为`True`，用于*设置是否开启“移除要素”功能*
- **rotateMode：** *bool*型，默认为`True`，用于*设置是否开启“旋转要素”功能*
- **oneBlock：** *bool*型，默认为`False`，用于*设置是否将编辑模式工具栏中的全部按钮置于一个容器内*

**showMeasurements：** *bool*型，默认为`False`

　　用于*设置是否为编辑模式下绘制的要素添加长度、面积标注信息*

**maxDrawnShapes：** *int*型

　　用于*设置编辑模式下最大允许绘制的要素数量*，超出此限制后每新绘制一个要素，都会导致最早绘制的要素被清除

**measureControl：** *bool*型，默认为`False`

　　用于*设置是否开启地图测量功能*，开启后会在地图上放置测量工具栏

**measureControlOptions：** *dict*型

　　用于*配置测量工具栏相关参数*，可用的键值对参数有：

- **position：** *string*型，默认为`'topleft'`，用于*设置测量工具栏的方位*，可选的有`'topleft'`、`'topright'`、`'bottomleft'`、`'bottomright'`
- **activeColor：** *string*型，默认为<font style="color: #f1c40f;">#f1c40f</font>，用于*设置测量工具绘制时的要素颜色*
- **completedColor：** *string*型，默认为<font style="color: #e74c3c;">#e74c3c</font>，用于*设置测量工具绘制完成时的要素颜色*

**viewAutoCorrection：** *bool*型，默认为`False`

　　用于*设置是否为当前地图开启自动视角校正功能*，开启后可能会带来一些性能上的压力

**_drawnShapes：** *list*型

　　用于*监听编辑模式下当前已绘制要素矢量数据所构成的数组*



