**id：** *str*型

用于定义组件的唯一识别`id`信息

---

**children：** *list*型

用于定义当前地图实例下属的单个或多个图层元素

---

**className：** *str*型

用于定义当前地图实例容器的`css`类名

---

**style：** *dict*型

用于定义当前地图实例容器的`css`属性键值对

---

**center：** *dict*型

用于为当前地图实例设置初始化中心坐标，可用的键值对参数有：

- **lng：** *int*或*float*型，默认为`0`，用于设置地图中心点经度
- **lat：** *int*或*float*型，默认为`0`，用于设置地图中心点纬度

---

**zoom：** *int*或*float*型，默认为`1`

用于为当前地图实例设置初始化缩放级别

---

**doubleClickZoom：** *bool*型，默认为`True`

用于设置是否允许双击地图进行放大

---

**dragging：** *bool*型，默认为`True`

用于设置是否允许拖拽挪动地图

---

**closePopupOnClick：** *bool*型，默认为`True`

用于设置是否允许用户鼠标点击地图空白处来关闭处于打开状态的**popup**卡片

---

**minZoom：** *int*或*float*型

用于设置地图缩放级别下限

---

**maxZoom：** *int*或*float*型

用于设置地图缩放级别上限

---

**zoomDelta：** *int*或*float*型，默认为`1`

用于设置地图缩放级别变化的最小步长单位

---

**zoomControl：** *bool*型，默认为`True`

用于设置是否显示地图缩放控件

---

**scrollWheelZoom：** *bool*或*str*型，默认为`True`

用于设置鼠标滚轮缩放地图的行为，`True`代表允许滚轮缩放，`False`代表不允许滚轮缩放，`'center'`表示滚轮缩放时无视鼠标具体位置，强制以当前地图中心作为缩放的参考中心

---

**wheelPxPerZoomLevel：** *int*或*float*型，默认为`60`

用于设置当鼠标滚轮滚动多少像素后，会触发1单位的缩放行为

---

**editToolbar：** *bool*型，默认为`False`

用于设置是否显示编辑模式工具栏

---

**editToolbarControlsOptions：** *dict*型

用于进一步配置编辑模式相关功能，可用的键值对参数有：

- **position：** *str*型，默认为`'topleft'`，用于设置编辑模式工具栏在地图上的方位，而可选的有`'topleft'`、`'topright'`、`'bottomleft'`和`'bottomright'`
- **drawMarker：** *bool*型，默认为`True`，用于设置是否在工具栏中显示**添加标记**按钮
- **drawCircleMarker：** *bool*型，默认为`True`，用于设置是否在工具栏中显示**添加圆形标记**按钮
- **drawPolyline：** *bool*型，默认为`True`，用于设置是否在工具栏中显示**添加折线**按钮
- **drawRectangle：** *bool*型，默认为`True`，用于设置是否在工具栏中显示**添加矩形**按钮
- **drawPolygon：** *bool*型，默认为`True`，用于设置是否在工具栏中显示**添加多边形**按钮
- **drawCircle：** *bool*型，默认为`True`，用于设置是否在工具栏中显示**添加圆形**按钮
- **drawText：** *bool*型，默认为`False`，用于设置是否在工具栏中显示**添加文字**按钮
- **editMode：** *bool*型，默认为`True`，用于设置是否在工具栏中显示**编辑要素**按钮
- **dragMode：** *bool*型，默认为`True`，用于设置是否在工具栏中显示**平移要素**按钮
- **cutPolygon：** *bool*型，默认为`False`，用于设置是否在工具栏中显示**剪切要素**按钮
- **removalMode：** *bool*型，默认为`True`，用于设置是否在工具栏中显示**移除要素**按钮
- **rotateMode：** *bool*型，默认为`True`，用于设置是否在工具栏中显示**旋转要素**按钮
- **oneBlock：** *bool*型，默认为`False`，用于设置是否将所有工具栏按钮放置于同一个容器中

---

**showMeasurements：** *bool*型，默认为`True`

用于设置是否为编辑模式下绘制出的矢量添加额外的长度、面积标注信息

---

**maxDrawnShapes：** *int*型，默认为`None`

用于设置编辑模式下，地图上同时允许存在的要素最大数量，超出限制时，新绘制的要素会导致当前最早绘制的要素自动被移除

---

**_drawnShapes：** *list*型

用于记录编辑模式下，地图上可见的所有已绘制矢量要素相关属性信息