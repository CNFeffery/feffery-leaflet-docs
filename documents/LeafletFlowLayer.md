**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**flowData：** `list[dict]`型

　　用于*设置当前流线图层对应流线数据*，每个字典元素代表一条流线，可用的键值对参数有：

- **from：** *dict*型，用于*定义当前流线起点坐标*，可用的键值对参数有：
  - **lng：** *int*或*float*型，用于*定义当前流线起点坐标经度*
  - **lat：** *int*或*float*型，用于*定义当前流线起点坐标纬度*
- **to：** *dict*型，用于*定义当前流线终点坐标*，可用的键值对参数有：
  - **lng：** *int*或*float*型，用于*定义当前流线终点坐标经度*
  - **lat：** *int*或*float*型，用于*定义当前流线终点坐标纬度*
- **labels：** *dict*型，可选，用于*定义当前流线起终点文字标签*，可用的键值对参数有：
  - **from：** *string*型，用于*定义当前流线起点文字标签*
  - **to：** *string*型，用于*定义当前流线终点文字标签*
- **color：** *string*型，用于*自定义当前流线颜色*
- **value：** *int*或*float*型，用于*定义当前流线对应数值*，会影响流线的宽度

**pulseRadius：** *int*或*float*型，默认为`30`

　　用于*定义起终点扩散圈最大像素半径*

**pulseBorderWidth：** *int*型或*float*型，默认为`3`

　　用于*定义起终点扩散圈轮廓像素款度*

**arcWidth：** *int*或*float*型，默认为`1`

　　用于*定义流线像素宽度*

**maxWidth：** *int*或*float*型，默认为`10`

　　用于*定义流线最大像素宽度*

**arcLabel：** *bool*型，默认为`True`

　　用于*设置是否展示起终点文字标签*

**arcLabelFontSize：** *string*型，默认为`'10px'`

　　用于*设置起终点文字标签字体大小*

**arcLabelFontFamily：** *string*型，默认为`'sans-serif'`

　　用于*设置起终点文字标签字体*

**keepUniqueLabels：** *bool*型，默认为`False`

　　用于*设置是否自动消除相同文字标签的重复叠加显示情况*