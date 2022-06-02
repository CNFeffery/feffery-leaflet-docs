**id：** *str*型

用于定义组件的唯一识别`id`信息

---

**data：** *dict*型

用于定义当前GeoJSON实例对应的矢量数据

---

**mode：** *str*型，默认为`'default'`

用于设置当前GeoJSON图层的绘图模式，可选的有`'default'`、`'selectable'`（选择模式）、`'choropleth'`（分层设色模式）、`'category'`（分类设色模式）

---

**hoverable：** *bool*型，默认为`False`

用于设置是否为当前GeoJSON实例开启要素鼠标悬浮样式区分效果

---

**defaultStyle：** *dict*型

用于为当前GeoJSON实例中的要素设置默认的矢量样式，可用的键值对参数有：

- **stroke：** *bool*型，默认为`True`，用于设置是否绘制轮廓线
- **color：** *str*型，默认为`'#3388ff'`，用于设置轮廓线颜色
- **weight：** *int*型，默认为`3`，用于设置轮廓线像素宽度
- **opacity：** *float*型，默认为`1`，用于设置轮廓线透明度
- **lineCap：** *str*型，默认为`'round'`，对应`css`中的`line-cap`属性，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-linecap)
- **lineJoin：** *str*型，默认为`'round'`，对应`css`中的`line-join`属性，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-linejoin)
- **dashArray：** *str*型，默认为`None`，对应`css`中的`dash-array`属性，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-dasharray)
- **dashOffset：** *str*型，默认为`None`，对应`css`中的`dash-offset`属性，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-dashoffset)
- **fill：** *bool*型，默认为`True`，用于设置是否对当前矢量进行填充
- **fillColor：** *str*型，默认为`'#3388ff'`，用于设置当前矢量的填充色
- **fillOpacity：** *str*型，默认为`0.2`，用于设置当前矢量的填充透明度

---

**hoverStyle：** *dict*型

参数`hoverable=True`时生效，用于为当前GeoJSON实例中的要素设置鼠标悬浮样式，参数格式同**defaultStyle**，默认为：

```json
{
    'fillOpacity': 0.6
}
```

---

**selectedStyle：** *dict*型

参数`mode='selectable'`时生效，用于为当前GeoJSON实例中的要素设置选择状态下的样式，参数格式同**defaultStyle**，默认为：

```json
{
    'color': '#f5222d',
    'fillColor': '#f5222d',
    'fillOpacity': 0.2,
    'opacity': 1,
}
```

---

**fitBounds：** *bool*型，默认为`True`

用于为当前GeoJSON实例设置是否在初次加载时，自适应调整地图视角至恰好容纳要素整体

---

**clickFeatureZoom：** *bool*型，默认为`False`

用于为当前GeoJSON实例设置是否在用户鼠标点击某个要素时，自动调整地图视角至恰好容纳所点击的要素

---

**showTooltip：** *bool*型，默认为`False`

用于为当前GeoJSON实例设置，当鼠标悬浮于要素之上时，是否展示`tooltip`提示框

---

**featureIdField：** *str*型，默认为`'id'`

用于为当前GeoJSON实例设置应当作为唯一识别id字段的属性名称，配合`选择模式`等功能使用

---

**featureValueField：** *str*型，默认为`'value'`

用于为当前GeoJSON实例设置应当作为数值字段的属性名称，配合`分层设色模式`等功能使用

---

**featureCategoryField：** *str*型，默认为`'category'`

用于为当前GeoJSON实例设置应当作为类别字段的属性名称，配合`分类设色模式`等功能使用

---

**featureTooltipField：** *str*型，默认为`'tooltip'`

用于为当前GeoJSON实例设置应当作为`tooltip`字段的属性名称，配合`showTooltip`等参数使用

---

**selectMode：** *str*型，默认为`'single'`

参数`mode='selectable'`时生效，用于为当前GeoJSON实例设置选择功能模式，可选的有`'single'`（单选模式）、`'multiple'`（多选模式）

---

**selectedFeatureIds：** *list*型

参数`mode='selectable'`时生效，用于监听或设置当前GeoJSON实例中处于选择状态的要素`id`信息（与**featureIdField**参数相对应）

---

**disableClickSelect：** *bool*型，默认为`False`

参数`mode='selectable'`时生效，用于为当前GeoJSON实例设置是否允许用户点击要素改变其选中状态，譬如当你的GeoJSON实例中要素的选择状态是由其他外部组件的交互行为所决定的，就可以设置`disableClickSelect=True`从而避免用户点击地图导致已选择结果被篡改

---

**featureValueToStyles：** *dict*型

参数`mode='choropleth'`时生效，根据参数**featureValueField**对应的要素属性字段数值，为当前GeoJSON实例中的每个要素，配置样式映射规则，可用的键值对参数有：

- **bins：** *list*型，传入用于定义每个分层数值区间范围，格式如`[左区间, 右区间]`
- **styles：** *list[dict]*型，传入与参数**bins**按顺序一一对应的要素矢量样式字典，每个字典格式同参数**defaultStyle**
- **closed：** *str*型，默认为`'left'`，用于设置区间的左右开闭情况，可选的有`'left'`（左闭）、`'right'`（右闭）

---

**featureCategoryToStyles：** *dict*型

参数`mode='category'`时生效，根据参数**featureCategoryField**对应的要素类别字段数值，为当前GeoJSON实例中的每个要素，配置样式映射规则，此参数每个键为对应的一个类别值，对应的值格式同参数**defaultStyle**

---

**_clickedFeature：** *dict*型

用于监听记录当前GeoJSON实例中被点击的要素相关信息

---

**_hoveredFeature：** *dict*型

用于监听记录当前GeoJSON实例中被鼠标悬浮的要素相关信息