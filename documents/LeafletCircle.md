**id：** *str*型

用于定义组件的唯一识别`id`信息

---

**center：** *dict*型

用于为当前圆形实例设置中心坐标，可用的键值对参数有：

- **lng：** *int*或*float*型，默认为`0`，用于设置当前圆形中心点经度
- **lat：** *int*或*float*型，默认为`0`，用于设置当前圆形中心点纬度

---

**radius：** *int*或*float*型

用于为当前圆形实例设置半径大小（单位：米）

---

**pathOptions：** *dict*型

用于为当前圆形实例配置样式相关参数，可用的键值对参数有：

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