**id：** *str*型

用于定义组件的唯一识别`id`信息

---

**positions：** *list*型

用于定义当前多边形实例的矢量信息，可细分为下列两种情况：

- **单多边形：** `list[dict]`型，结构为字典构成的列表，其中每个字典具有`lng`、`lat`键值对参数用于按顺序定义多边形上对应节点坐标信息
- **有孔单多边形：** `list[list[dict]]`型，结构为若干个**单多边形**结构（仅有一个时等价于**单多边形**）所构成的列表，其中第一个**单多边形**结构表示当前多边形实例的外轮廓，剩余**单多边形**结构代表当前多边形实例内部各孔洞内轮廓线
- **多多边形：** `list[list[list[dict]]]`型，结构为若干个**有孔单多边形**结构所构成的列表

---

**pathOptions：** *dict*型

用于为当前折线实例配置样式相关参数，可用的键值对参数有：

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