**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**children：** *组件型*

　　用于传入*嵌套的tooltip、popup等额外元素*

**position：** *dict*型，必填

　　用于*设置当前标记坐标*，可用的键值对参数有：

- **lng：** *int*或*float*型，用于*设置标记经度*
- **lat：** *int*或*float*型，用于*设置标记纬度*

**draggable：** *bool*型，默认为`False`

　　用于*设置当前标记是否可直接进行拖拽*，无需配合`LeafletMap`的地图编辑功能

**iconOptions：** *dict*型

　　用于*配置标记图标相关参数*，可用的键值对参数有：

- **iconUrl：** *string*型，用于*设置自定义图标url地址*
- **iconSize：** *list*型，用于*设置图标尺寸*，格式为`[像素宽度, 像素高度]`
- **iconAnchor：** *list*型，用于*设置图标锚点坐标*，以图标左上角作为参考系原点
- **popupAnchor：** *list*型，用于*设置嵌套的popup元素展开位置*，以`iconAnchor`作为参考系原点
- **tooltipAnchor：** *list*型，用于*设置嵌套的tooltip元素展开位置*，以`iconAnchor`作为参考系原点
- **shadowUrl：** *string*型，用于*设置图标阴影图片url地址*
- **shadowSize：** *list*型，用于*设置阴影图片尺寸*，格式为`[像素宽度, 像素高度]`
- **shadowAnchor：** *list*型，用于*设置阴影图片锚点坐标*，以图标左上角作为参考系原点
- **className：** *string*型，用于*设置图标的css类*

**opacity：** *int*或*float*型，默认为`1`

　　用于*设置当前标记的透明度*

**editable：** *bool*型，默认为`False`

　　用于*设置当前标记是否可编辑*，需配合`LeafletMap`的地图编辑功能

**zIndexOffset：** *int*型

　　用于*为当前标记设置图层顺序偏移量*

**riseOnHover：** *bool*型，默认为`False`

　　用于*设置当前标记是否在鼠标移入后自动调整图层顺序至顶层*

**autoPan：** *bool*型，默认为`False`

　　用于*设置当前标记是否在被移动至地图边缘时自动移动地图以自适应显示*

**nClicks：** *int*型，默认为`0`

　　用于*监听当前标记要素的累计被点击次数*

**mouseOverCount：** *int*型，默认为`0`

　　用于*监听当前标记要素的累计鼠标移入次数*