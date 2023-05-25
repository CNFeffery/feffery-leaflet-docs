**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**data：** *dict*型，必填

　　用于*设置当前组件要渲染的GeoJSON格式数据*

**mode：** *string*型，默认为`'default'`

　　用于*设置当前GeoJSON组件的功能模式*，可选的有`'default'`（默认模式）、`'selectable'`（选择模式）、`'choropleth'`（分层设色模式）、`'category'`（分类设色模式）

**hoverable：** *bool*型，默认为`False`

　　用于*设置是否开启要素鼠标悬停效果*，开启后，可配合参数`hoverStyle`进行鼠标悬浮时的额外样式设定

**defaultStyle：** *dict*型

　　用于*设置要素的默认样式*，可用的键值对参数有：

- **stroke：** *bool*型，默认为`True`，用于*设置当前要素是否显示轮廓*
- **color：** *string*型，默认为<font style="color: #3388ff;">#3388ff</font>，用于*设置当前要素的轮廓色*
- **weight：** *int*或*float*型，默认为`3`，用于*设置当前要素的轮廓像素宽度*
- **opacity：** *int*或*float*型，默认为`1`，用于*设置当前要素的轮廓透明度*
- **lineCap：** *string*型，默认为`'round'`，用于*设置当前要素轮廓线的line-cap属性*，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-linecap)
- **lineJoin：** *string*型，默认为`'round'`，用于*设置当前要素轮廓线的line-join属性*，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-linejoin)
- **dashArray：** *string*型，用于*设置当前要素轮廓线的线型dash-array属性*，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-dasharray)
- **dashOffset：** *string*型，用于*设置当前要素轮廓线的dash-offset属性*，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-dashoffset)
- **fill：** *bool*型，默认为`True`，用于*设置当前要素是否显示填充*
- **fillColor：** *string*型，默认为<font style="color: #3388ff;">#3388ff</font>，用于*设置当前要素的填充色*
- **fillOpacity：** *int*或*float*型，默认为`0.2`，用于*设置当前要素的填充透明度*

**hoverStyle：** *dict*型

　　用于*设置要素在被鼠标悬停时的额外样式*，可用的键值对参数同`defaultStyle`

**selectedStyle：** *dict*型

　　当`mode='selectable'`，用于*设置要素在被选中时的样式*，可用的键值对参数同`defaultStyle`

**fitBounds：** *bool*型，默认为`True`

　　用于*设置当前组件初始化时是否自动调整地图缩放范围以适应GeoJSON数据范围大小*

**clickFeatureZoom：** *bool*型，默认为`False`

　　用于*设置是否允许点击要素后自动调整地图范围以适应对应要素大小*

**showTooltip：** *bool*型，默认为`False`

　　用于*设置是否为要素开启鼠标悬停tooltip展示效果*

**featureIdField：** *string*型，默认为`'id'`

　　用于*设置要素属性中作为唯一识别id的字段名*，用于在要素选择模式中监听已选中要素

**featureValueField：** *string*型，默认为`'value'`

　　用于*设置要素属性中作为数值的字段名*，用于在分层设色模式中作为色彩映射依赖值

**featureCategoryField：** *string*型，默认为`'category'`

　　用于*设置要素属性中作为类别的字段名*，用于在分类设色模式中作为色彩映射依赖值

**featureTooltipField：** *string*型，默认为`'tooltip'`

　　用于*设置要素属性中存储tooltip信息的字段名*，用于在`showTooltip=True`时作为对应要素的tooltip信息

**selectMode：** *string*型，默认为`'single'`

　　当`mode='selectable'`时，用于*设置选择模式类型*，可选的有`'single'`（单选模式）、`'multiple'`（多选模式）

**disableClickSelect：** *bool*型，默认为`False`

　　用于*设置是否禁用主动点击选择要素功能*

**selectedFeatureIds：** *list*型

　　当`mode='selectable'`时，用于*监听或设置处于选中状态下的要素唯一识别id字段数组*

**featureValueToStyles：** *dict*型

　　当`mode='choropleth'`时，用于*配置分层设色相关规则*，可用的键值对参数有：

- **bins：** *list*型，用于*为分层设色定义每段区间范围*，格式为`[左区间值, 右区间值]`
- **styles：** `list[dict]`型，用于*设置与bins一一对应的样式参数字典*，每个样式参数字典可用的键值对参数同`defaultStyle`
- **closed：** *string*型，默认`'left'`，用于*设置区间的闭合状态*，可选的有`'left'`（左闭）、`'right'`（右闭）

**featureCategoryToStyles：** *dict*型

　　当`mode='category'`时，用于*为不同分类设置对应的样式*，其中键为对应类别值，值可用的键值对参数同`defaultStyle`

**tooltipDirection：** *string*型，默认为`'auto'`

　　当`showTooltip=True`，用于*设置要素tooltip的展开方位*，可选的有`'auto'`、`'left'`、`'right'`、`'top'`、`'bottom'`、`'center'`

**tooltipPermanent：** *string*型，默认为`False`

　　用于*设置是否保持要素的tooltip处于展开状态而无需鼠标悬停触发*

**tooltipSticky：** *bool*型，默认为`False`

　　用于*设置要素tooltip在显示时是否跟随鼠标位置而移动*

**tooltipClassName：** *string*型

　　用于*设置要素tooltip对应的css类名*

**lassoSelect：** *bool*型，默认为`False`

　　当` mode='selectable'`且`selectMode='multiple'`时，用于*设置是否开启套圈选择模式*

**lassoType：** *string*型，默认为`'intersect'`

　　当开启套圈选择模式后，用于*设置套圈选择的判定规则类型*，可选的有`'contain'`（完全包含）、`'intersect'`（相交）

**lassoResetSelectedFeatureIds：** *bool*型，默认为`False`

　　当开启套圈选择模式后，用于*设置每次点击套圈选择功能按钮后是否自动清除先前的已选要素*

**lassoButtonPosition：** *string*型，默认为`'topleft'`

　　用于*设置套圈选择功能按钮的展示方位*，可选的有`'topleft'`、`'topright'`、`'bottomleft'`、`'bottomright'`

**lassoStyle：** *dict*型

　　用于*设置套圈选择对应套圈的矢量样式*，可用的键值对参数同`defaultStyle`

**pointRenderMode：** *string*型，默认为`'circle-marker'`

　　用于*设置针对GeoJSON数据中的点要素的渲染方式*，可选的有`'circle-marker'`（圆形标记）、`'marker'`（标记）

**circleMarkerRadius：** *int*型，默认为`10`

　　当`pointRenderMode='circle-marker'`时，用于*设置圆形标记的像素半径*

**_clickedFeature：** *dict*型

　　用于*监听要素点击事件*，事件返回的键值对信息有：

- **featureId：** 对应*事件发生要素的唯一识别id*
- **feature：** 对应*事件发生要素的属性字典*
- **timestamp：** 对应*事件发生的时间戳信息*

**_hoveredFeature：** *dict*型

　　用于*监听要素鼠标悬停事件*，事件返回的键值对信息有：

- **featureId：** 对应*事件发生要素的唯一识别id*
- **feature：** 对应*事件发生要素的属性字典*
- **timestamp：** 对应*事件发生的时间戳信息*

