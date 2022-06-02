**id：** *str*型

用于定义组件的唯一识别`id`信息

---

**mapActionConfig：** *dict*型

用于为当前地图实例编排地图动作，可用的键值对参数有：

- **type：** *str*型，用于指定动作类型，可选的有`'set-zoom'`（缩放到指定级别）、`'zoom-in'`（在当前缩放级别基础上放大一定级别）、`'zoom-out'`（在当前缩放级别基础上缩小一定级别）、`'fly-to'`（以飞行动画模式移动地图视角）、`'fly-to-bounds'`（以飞行动画模式移动地图以适应设定的范围）、`'invalidate-size'`（强制校正地图视角）
- **center：** *dict*型，`'fly-to'`模式下使用，用于设定目标视角对应的中心点坐标，可用的键值对参数有：
  - **lng：** *int*或*float*型，用于设置目标视角中心点经度
  - **lat：** *int*或*float*型，用于设置目标视角中心点纬度
- **zoom：** *int*或*float*型，`'set-zoom'`、`'fly-to'`模式下使用，用于设定目标视角对应的缩放级别
- **zoomInOffset：** *int*或*float*型，`'zoom-in'`模式下可用，用于设定地图放大级别的变化量
- **zoomOutOffset：** *int*或*float*型，`'zoom-out'`模式下可用，用于设定地图缩小级别的变化量
- **bounds：** *dict*型，`'fly-to-bounds'`模式下可用，用于设定目标视角的范围，可用的键值对参数有：
  - **minx：** *int*或*number*型，用于设定目标视角左下角经度
  - **miny：** *int*或*number*型，用于设定目标视角左下角纬度
  - **maxx：** *int*或*number*型，用于设定目标视角右上角经度
  - **maxy：** *int*或*number*型，用于设定目标视角右上角纬度
- **flyToDuration：** *str*型，`'fly-to'`、`'fly-to-bounds'`模式下可用，用于设定飞行动画的速度水平，从快到慢可选的有`'instant'`、`'fast'`、`'normal'`、`'slow'`，当设置为`'auto'`时会自动根据当前视角到目标视角的距离自动调整动画速度

