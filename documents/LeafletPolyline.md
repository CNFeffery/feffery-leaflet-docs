**id：** *str*型

用于定义组件的唯一识别`id`信息

---

**positions：** *list*型

用于定义当前折线图层的折线矢量信息，可细分为下列两种情况：

- **单折线：** `list[dict]`型，结构为字典构成的列表，其中每个字典具有`lng`、`lat`键值对参数用于按顺序定义折线上对应折点坐标信息
- **多折线：** `list[list[dict]]`型，结构为若干个**单折线**结构所构成的列表

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