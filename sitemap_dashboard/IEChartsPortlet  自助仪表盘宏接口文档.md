ECharts组件接口对象 

version
    
9.7.0 

since
    
9.7.0
### Hierarchy 层级
  * IPortlet
    * IEChartsPortlet


## Index 目录
###  Methods 方法 
  * addChartsListener
  * cancelAsFilter
  * getChartInstance
  * getChartOptions
  * getTooltipHandler
  * isMaximized
  * resetLinkage
  * restoreDown
  * setAsFilter
  * setChartOptions


##  Methods 方法 
###  addChartsListener 
  * addChartsListener(eventEChartEvent, callback(paramsEChartEventParams)void)void


  * 监听EChart事件 

version
    
9.7.0 

since
    
9.7.0
```
 portlet.addChartsListener('click', function (params) {
   alert('点击了')
 })
```

#### Parameters 参数
    * #####  event: EChartEvent
EChart事件
    * #####  callback: (paramsEChartEventParams)void
事件回调函数
      *         * (paramsEChartEventParams)void
        * #### Parameters 参数
          * #####  params: EChartEventParams
####  Returns 返回值 void
####  Returns 返回值 void


###  append 
  * appendCss(selectorCssSelector, styleCssObjectstring)void


  * 增加自定义CSS样式（样式只对当前组件生效） 

version
    
9.7.0 

since
    
9.7.0
    * **示例** 给标题栏加CSS,改变标题栏颜色
```
portlet.appendCss('.portlet-title-text-default', {
'color': '#fff',
'background': 'rgb(0,0,255)',
'font-size': '16px'
})
```

**示例代码2** 给静态文本组件内容加CSS,改变文本样式(注意只在静态文本组件中生效)
```
portlet.appendCss('.text-object__processedContent', {
   'color': '#f00',
   'background': 'rgb(0,255,0)',
})
```

#### Parameters 参数
    * #####  selector: CssSelector
css选择器
    * #####  style: CssObjectstring
css样式对象
####  Returns 返回值 void


###  cancelAsFilter 
  * cancelAsFilter()void


  * 取消作为筛选器 

version
    
10.5.0 

since
    
10.5.0
```
portlet.cancelAsFilter();
```

####  Returns 返回值 void


###  doExport 
  * doExport(exportTypeExportType)void


  * 

version
    
10.5.0 

since
    
10.5.0
```
portlet.doExport(ExportType.EXCEL);
```

#### Parameters 参数
    * #####  exportType: ExportType
####  Returns 返回值 void


###  getChartInstance 
  * getChartInstance()EChartInstance


  * 获取EChart实例
需要等组件渲染完成，也就是在`onAfterRender`（组件渲染后事件）中才能获取到EChart示例。
####  Returns 返回值 EChartInstance


###  getChartOptions 
  * getChart


  * 获取EChart配置项 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 EChartOptions


###  get 
  * getId()string


  * 获取组件id 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  getTitle 
  * getTitle()string


  * 获取组件标题 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  getToolbar 
  * getToolbar()IPortletToolbar


  * 获取组件工具栏 

version
    
10.5.0 

since
    
10.5.0
```
let toolbar: IPortletToolbar = portlet.getToolbar();

```

####  Returns 返回值 IPortletToolbar


###  getTooltipHandler 
  * getTooltipHandler(handlerTooltipHandler)void


  * 获取tooltip信息处理函数 

version
    
9.7.0 

since
    
9.7.0
```
function main(page: IPage, portlet: IEChartsPortlet) {
  let fields = getFields(portlet)
}
// 获取字段
function getFields(portlet: IEChartsPortlet) {
  let fields: any = {}; // 所有字段
  if (!portlet.getTooltipHandler) {
      return fields;
  }
  // 调用宏接口getTooltipHandler，通过tooltip获取字段信息
  portlet.getTooltipHandler((
      row: ITooltipRow, column: ITooltipColumn,
      rowIndex: number, columnIndex: number, fieldIndex: number
  ) => {
      let field = column.getField()
      let value = column.getValue()
      let { label } = field; // 字段的名称（最终显示到图形上的值
      let { fieldGroupType } = value; // 字段所在区域
      if (!fields[fieldGroupType]) {
          fields[fieldGroupType] = {}
      }
      fields[fieldGroupType][label] = field
  })
  return fields
}
```

#### Parameters 参数
    * #####  handler: TooltipHandler
单个tooltip的字段信息回调函数
####  Returns 返回值 void


###  getType 
  * getType()string


  * 获取组件类型 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  hide 
  * hide()void


  * 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 void


###  isAsFilter 
  * isAsFilter()boolean


  * 当前组件是否作为筛选器 

version
    
10.5.0 

since
    
10.5.0
```
let isAsFilter: boolean = portlet.isAsFilter();
```

####  Returns 返回值 boolean


###  isMaximized 
  * isMaximized()boolean


  * 当前组件是否是最大化状态 

version
    
10.5.0 

since
    
10.5.0
```
let isMaximized: boolean = portlet.isMaximized();

```

####  Returns 返回值 boolean


###  maximize 
  * maximize()void


  * 最大化组件，目前仅支持图形、表格、web电子表格、tab组件以及URL组件调用 

version
    
10.5.0 

since
    
10.5.0
```
portlet.maximize();

```

####  Returns 返回值 void


###  remove 
  * removeCss()void


  * 移除自定义CSS 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 void


###  resetLinkage 
  * resetLinkage()void


  * 

version
    
10.5.0 

since
    
10.5.0
```
portlet.resetLinkage();
```

####  Returns 返回值 void


###  restoreDown 
  * restoreDown()void


  * 还原最大化 

version
    
10.5.0 

since
    
10.5.0
```
portlet.restoreDown();

```

####  Returns 返回值 void


###  setAsFilter 
  * setAsFilter()void


  * 设置当前组件作为筛选器 

version
    
10.5.0 

since
    
10.5.0
```
portlet.setAsFilter();
```

####  Returns 返回值 void


###  setChartOptions 
  * setChartOptions(optionsEChartOptions)void


  * 设置EChart配置项
通常需要先调用`getChartOptions`获得到`options`后，再做改动，如果直接new新的`options`原配置将失效。
建议在`onBeforeRender`(组件渲染前事件)中进行设置，可以有效避免图表多次刷新。 

version
    
9.7.0 

since
    
9.7.0
```
let options = portlet.getChartOptions()
options.yAxis.min = 200
portlet.setChartOptions(options)
```

#### Parameters 参数
    * #####  options: EChartOptions
EChart配置项
####  Returns 返回值 void


###  setTitle 
  * setTitle(titlestring)void


  * 设置组件标题 

version
    
9.7.0 

since
    
9.7.0
#### Parameters 参数
    * #####  title: string
####  Returns 返回值 void


###  show 
  * show()void


  * 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 void


