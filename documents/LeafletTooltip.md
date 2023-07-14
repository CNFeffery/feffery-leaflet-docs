**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**children：** *组件型*

　　用于传入*当前提示框内需要嵌套的内部元素*

**className：** *string*型

　　用于*为当前提示框容器设置css类*

**direction：** *string*型，默认为`'auto'`

　　用于*为当前提示框设置展开方位*，可选的有`'right'`、`'left'`、`'top'`、`'bottom'`、`'center'`、`'auto'`

**permanent：** *bool*型，默认为`False`

　　用于*设置当前提示框是否保持展开状态*

**sticky：** *bool*型，默认为`False`

　　用于*设置当前提示框是否在要素内跟随鼠标位置实时移动*

**opacity：** *float*型，默认为`0.9`

　　用于*设置当前提示框整体透明度*

**interactive：** *bool*型，默认为`False`

　　用于*设置当前提示框内部点击事件是否触发地图容器相关事件*