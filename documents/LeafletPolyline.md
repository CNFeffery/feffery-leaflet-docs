**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**children：** *组件型*

　　用于传入*嵌套的tooltip、popup等额外元素*

**positions：** *list*型，必填

　　用于*设置当前折线对应的坐标串数组数据*，数组中每个元素为*dict*型，可用的键值对参数有：

- **lng：** *int*或*float*型，用于*设置当前坐标点的经度*
- **lat：** *int*或*float*型，用于*设置当前坐标点的纬度*

　　也可以传入元素为*list*型的数组用来表示多部件要素

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

**arrowheads：** *bool*或*dict*型，默认为`False`

　　用于*为当前折线配置箭头相关效果*，可用的键值对参数有：

- **yawn：** *int*或*float*型，默认为`60`，用于*设置箭头的开合角度*
- **fill：** *bool*型，默认为`False`，用于*设置是否绘制实心箭头*
- **size：** *string*、*int*或*float*型，默认为`'15%'`，用于*设置箭头尺寸*，其中：
  - *string*型输入表示以箭头所附着的折线为参照的百分比尺寸
  - *int*或*float*型表示以米为单位的尺寸
- **frequency：** *string*或*int*型，默认为`'allvertices'`，用于*设置箭头在折线上的绘制频率*，其中：
  - `'allvertices'`表示在每个折点处添加箭头，`'endonly'`表示仅在折线尾端添加箭头
  - *int*型输入表示等间距绘制固定数量的箭头
  - 以`'m'`或`'px'`结尾的输入表示固定间隔渲染箭头，如`'100m'`、`'100px'`
- **proportionalToTotal：** *bool*型，默认为`False`，用于针对多部件要素设置是否*利用全部折线要素长度之和进行百分比箭头尺寸的计算*

**arrowheadsPathOptions：** *dict*型

　　用于*配置当前箭头要素的样式*，可用的键值对参数有：

- **stroke：** *bool*型，默认为`True`，用于*设置当前箭头要素是否显示轮廓*
- **color：** *string*型，默认为<font style="color: #3388ff;">#3388ff</font>，用于*设置当前箭头要素的轮廓色*
- **weight：** *int*或*float*型，默认为`3`，用于*设置当前箭头要素的轮廓像素宽度*
- **opacity：** *int*或*float*型，默认为`1`，用于*设置当前箭头要素的轮廓透明度*
- **lineCap：** *string*型，默认为`'round'`，用于*设置当前箭头要素轮廓线的line-cap属性*，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-linecap)
- **lineJoin：** *string*型，默认为`'round'`，用于*设置当前箭头要素轮廓线的line-join属性*，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-linejoin)
- **dashArray：** *string*型，用于*设置当前箭头要素轮廓线的线型dash-array属性*，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-dasharray)
- **dashOffset：** *string*型，用于*设置当前箭头要素轮廓线的dash-offset属性*，[参考资料](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/stroke-dashoffset)
- **fill：** *bool*型，默认为`True`，用于*设置当前箭头要素是否显示填充*
- **fillColor：** *string*型，默认为<font style="color: #3388ff;">#3388ff</font>，用于*设置当前箭头要素的填充色*
- **fillOpacity：** *int*或*float*型，默认为`0.2`，用于*设置当前箭头要素的填充透明度*

**editable：** *bool*型，默认为`False`

　　用于*设置当前折线是否可编辑*，需配合`LeafletMap`的地图编辑功能

**nClicks：** *int*型，默认为`0`

　　用于*监听当前折线要素的累计被点击次数*

**mouseOverCount：** *int*型，默认为`0`

　　用于*监听当前折线要素的累计鼠标移入次数*

