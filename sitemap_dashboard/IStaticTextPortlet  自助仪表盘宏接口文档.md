富文本组件接口对象
### Hierarchy 层级
  * IPortlet
    * IStaticTextPortlet


## Index 目录
###  Methods 方法 
  * getCellDisplayValue
  * getCellValue
  * getHtmlContent
  * isMaximized
  * restoreDown
  * setContentHandler


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


###  getCellDisplayValue 
  * getCellDisplayValue(rowIndexnumber, columnIndexnumber)string


  * 获取单元格显示值（仅适用于组件渲染后） 

version
    
9.7.0 

since
    
9.7.0
#### Parameters 参数
    * #####  rowIndex: number
行序号（序号从0开始）
    * #####  columnIndex: number
列序号（序号从0开始）
####  Returns 返回值 string


###  getCellValue 
  * getCellValue(rowIndexnumber, columnIndexnumber)string


  * 获取单元格真实值（仅适用于组件渲染后） 

version
    
9.7.0 

since
    
9.7.0
#### Parameters 参数
    * #####  rowIndex: number
行序号（序号从0开始）
    * #####  columnIndex: number
列序号（序号从0开始）
####  Returns 返回值 string


###  getHtmlContent 
  * getHtmlContent()HTMLElement


  * 获取富文本内容 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 HTMLElement
HTMLElement


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


###  setContentHandler 
  * setContentHandler(handlerStaticTextContentHandler)void


  * 富文本内容处理函数
可以对富文本的内容进行处理，当需要改变富文本内容的时候可以使用该方法。 

version
    
9.7.0 

since
    
9.7.0
```
function main(page: IPage, portlet: IStaticTextPortlet) {
    portlet.setContentHandler(function (rawHtmlContent, processedHtmlContent) {
        let html = processedHtmlContent + '<span style="color: red;">' + '通过宏增加的文本' + '<\span>'
        return html
    })
}
```

#### Parameters 参数
    * #####  handler: StaticTextContentHandler
单元格样式处理函数
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


