筛选器及参数组件接口对象 

version
    
9.7.0 

since
    
9.7.0
### Hierarchy 层级
  * IPortlet
    * IFilterPortlet


## Index 目录
###  Methods 方法 
  * getDisplayValue
  * getStandByValues
  * getToolbar
  * isMaximized
  * pauseCarousel
  * restoreDown
  * setFilterValueChangeHandler
  * setRenderOptionHandler
  * turnOffCarousel
  * turnOnCarousel


##  Methods 方法 
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


###  getDisplayValue 
  * getDisplayValue()Arraystring


  * 获取参数显示值 

version
    
10.5.8 

since
    
10.5.8
```
let value = portlet.getDisplayValue()
```

####  Returns 返回值 Arraystring
Array


###  get 
  * getId()string


  * 获取组件id 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  getStandByValues 
  * getStandByValues()ArrayIStandByValue


  * 获取筛选器备选值 

version
    
10.1.0 

since
    
10.1.0
```
let standByValues: Array<IStandByValue> = portlet.getStandByValues();
```

**注意** 目前只有列表、下拉类型的筛选器可以获取到备选值
####  Returns 返回值 ArrayIStandByValue
备选值，包含显示值与真实值 仅下拉筛选器和列表筛选器有备选值


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


###  getType 
  * getType()string


  * 获取组件类型 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  getValue 
  * getValue()Arraystring


  * 获取参数真实值 

version
    
9.7.0 

since
    
9.7.0
```
let value = portlet.getValue()
```

####  Returns 返回值 Arraystring
Array


###  hide 
  * hide()void


  * 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 void


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


###  pauseCarousel 
  * pauseCarousel()void


  * 暂停筛选器备选值轮播，可以通过调用`turnOnCarousel`恢复轮播 

version
    
10.1.0 

since
    
10.1.0
```
portlet.pauseCarousel();
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


###  setFilterValueChangeHandler 
  * setFilterValueChangeHandler(handlerFilterValueChangeHandler)void


  * 设置筛选器输入值处理函数
可以动态改变筛选器的值 

version
    
9.7.0 

since
    
9.7.0
```
portlet.setFilterValueChangeHandler(function (value: Array) {
  // 可以对value做处理
  return value
})
```

#### Parameters 参数
    * #####  handler: FilterValueChangeHandler
筛选器输入值处理函数
####  Returns 返回值 void


###  setRenderOptionHandler 
  * setRenderOptionHandler(handlerIFilterTableHandler)void


  * 设置筛选器备选项处理函数 

version
    
9.7.0 

since
    
9.7.0
```
portlet.setRenderOptionHandler(function (row: IFilterRow, column: IFilterColumn, rowIndex: number, columnIndex: number) {})
```

目前只支持列表单选、列表多选类型的筛选器，不支持其他类型的筛选器
#### Parameters 参数
    * #####  handler: IFilterTableHandler
####  Returns 返回值 void
备选值分页列表


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


###  setValue 
  * setValue(valuestring[])void


  * 设置参数值 

version
    
9.7.0 

since
    
9.7.0
```
portlet.setValue(['海鲜'])
```

#### Parameters 参数
    * #####  value: string[]
####  Returns 返回值 void


###  show 
  * show()void


  * 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 void


###  turnOffCarousel 
  * turnOffCarousel()void


  * 停止筛选器备选值轮播，再调用`turnOnCarousel`的时候会从第一个备选值开始 

version
    
10.1.0 

since
    
10.1.0
```
portlet.turnOffCarousel();
```

####  Returns 返回值 void


###  turnOnCarousel 
  * turnOnCarousel(options?: ICarouselOptions)void


  * 启动\恢复筛选器备选值轮播 

version
    
10.1.0 

since
    
10.1.0
```
portlet.turnOnCarousel();

```

**注意** 不传参数的时候将使用默认配置
#### Parameters 参数
    * #####  Optional options: ICarouselOptions
轮播选项，如果不传递则使用默认选项
####  Returns 返回值 void


