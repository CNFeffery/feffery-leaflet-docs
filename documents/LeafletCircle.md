**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**children：** *组件型*

　　用于传入*嵌套的tooltip、popup等额外元素*

**center：** *dict*型，必填

　　用于*设置当前圆形的中心坐标*，可用的键值对参数有：

- **lng：** *int*或*float*型，用于*设置中心经度*
- **lat：** *int*或*float*型，用于*设置中心纬度*

**radius：** *int*或*float*型，必填

　　用于*设置当前圆形的半径*，单位：米

**pathOptions：** *dict*型

　　用于*配置当前矢量的样式*，可用的键值对参数有：

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

**editable：** *bool*型，默认为`False`

　　用于*设置当前圆形是否可编辑*，需配合`LeafletMap`的地图编辑功能

**nClicks：** *int*型，默认为`0`

　　用于*监听当前圆形的累计被点击次数*

**mouseOverCount：** *int*型，默认为`0`

　　用于*监听当前圆形的累计鼠标移入次数*