**id：** *str*型

用于定义组件的唯一识别`id`信息

---

**points：** `list[dict]`型

用于为当前热力图层实例定义所需的热力数据点信息，其中每个字典可用的键值对有：

- **lng：** *int*或*float*型，用于定义当前数据点的经度坐标
- **lng：** *int*或*float*型，用于定义当前数据点的纬度坐标
- **weight：** *int*或*float*型，可选，用于定义当前数据点的权重值

---

**minOpacity：** *float*型

用于为当前热力图层实例设置最小透明度，取值应当在0~1之间

---

**max：** *int*或*float*型

用于手动为当前热力图层实例设置权重上限

---

**radius：** *int*型，默认为`25`

用于为当前热力图层实例设置每个热力点的像素半径大小

---

**blur：** *int*型，默认为`15`

用于为当前热力图层实例设置每个热力点的渐变衰减外轮廓像素半径

---

**gradient：** *dict*型

用于手动为当前热力图层实例设置色彩映射断点，例如`{0.4: 'blue', 0.65: 'lime', 1: 'red'}`