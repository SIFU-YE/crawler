页签组件接口对象 

version
    
10.5.8 

since
    
10.5.8
### Hierarchy 层级
  * IPortlet
    * IStaticTabsLinkPortlet


## Index 目录
###  Methods 方法 
  * getActiveTabName
  * getLinksByTabName
  * isMaximized
  * restoreDown
  * setActiveTabName
  * setActiveTabNameChangeHandler


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


###  getActiveTabName 
  * getActiveTabName()string


  * 获取当前聚焦的tab页签下标 

version
    
10.5.8 

since
    
10.5.8
####  Returns 返回值 string


###  get 
  * getId()string


  * 获取组件id 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  getLinksByTabName 
  * getLinksByTabName(tabNamestring)TabsLinksItem[]


  * 根据下标获取页签绑定项列表 

version
    
10.5.8 

siince
    
10.5.8
#### Parameters 参数
    * #####  tabName: string
####  Returns 返回值 TabsLinksItem[]


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


###  setActiveTabName 
  * setActiveTabName(activeTabNamestringnumber)string


  * 聚焦到指定名称或下标的tab函数 

version
    
10.5.8 

since
    
10.5.8
```
// 打开第一个Tab页签
portlet.setActiveTabName(0)
// 打开页签3
portlet.setActiveTabName('页签3')
```

#### Parameters 参数
    * #####  activeTabName: stringnumber
tab页签名称或下标
####  Returns 返回值 string


###  setActiveTabNameChangeHandler 
  * setActiveTabNameChangeHandler(handlersetActiveTabNavitorHandler)string


  * 切换tab页签处理函数 

version
    
10.5.8 

since
    
10.5.8
```
portlet.setActiveTabNameChangeHandler(function (activeTabName) {
  return activeTabName + ''
})
```

#### Parameters 参数
    * #####  handler: setActiveTabNavitorHandler
####  Returns 返回值 string


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


