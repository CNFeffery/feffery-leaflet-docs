**id：** *str*型

用于定义组件的唯一识别`id`信息

---

**flowData：** `list[dict]`型

用于为当前流线图层设置流线数据，其中每个字典可用的键值对参数有：

- **from：** *dict*型，用于定义当前流线的起点坐标，可用的键值对参数有：
  - **lng：** *int*或*float*型，用于定义起点经度坐标
  - **lat：** *int*或*float*型，用于定义起点纬度坐标
- **to：** *dict*型，格式同参数**from**
- **labels：** *dict*型，用于分别定义起点和终点的文字标签内容，可用的键值对参数有：
  - **from：** *str*型，用于定义起点文字标签内容，传入`None`则不绘制标签
  - **to：** *str*型，用于定义终点文字标签内容，传入`None`则不绘制标签
- **color：** *str*型，默认为`'#3498db'`，用于设置当前流线的色彩，接受`css`中的rgb及16进制格式色彩值
- **value：** *int*或*float*型，默认为`1`，用于为当前流线设置权重值，会影响流线的宽度

---

**pulseRadius：** *int*型，默认为`30`

用于为当前流线图层实例设置终点扩散圆圈动画的像素半径

---

**pulseBorderWidth：** *int*型，默认为`3`

用于为当前流线图层实例设置终点扩散圆圈动画的边框像素半径

---

**arcWidth：** *int*型，默认为`1`

用于为当前流线图层实例设置默认最小的流线像素宽度

---

**maxWidth：** *int*型，默认为`10`

用于为当前流线图层实例设置默认最大的流线像素宽度

---

**arcLabel：** *bool*型，默认为`True`

用于为当前流线图层实例设置是否显示起点、终点文字标签

---

**arcLabelFontSize：** *str*型，默认为`'10px'`

用于为当前流线图层实例设置起点、终点文字标签的字体大小

---

**arcLabelFontFamily：** *str*型，默认为`'sans-serif'`

用于为当前流线图层实例设置起点、终点文字标签的字体族