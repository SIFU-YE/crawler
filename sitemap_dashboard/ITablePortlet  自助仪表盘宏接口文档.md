旧表格组件接口对象
### Hierarchy 层级
  * IPortlet
    * ITablePortlet


## Index 目录
###  Methods 方法 
  * cancelAsFilter
  * getCellDisplayValue
  * getCellValue
  * getToolbar
  * isAsFilter
  * isMaximized
  * resetLinkage
  * restoreDown
  * setAsFilter
  * setCellStyleHandler
  * setRenderCellHandler
  * setRenderHeaderHandler
  * setRowStyleHandler


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


###  getCellDisplayValue 
  * getCellDisplayValue(rowIndexnumber, columnIndexnumber)string


  * 获取单元格显示值 

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


  * 获取单元格真实值 

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


###  setCellStyleHandler 
  * setCellStyleHandler(handlerTableCellStyleHandler)void


  * 单元格样式处理函数（适用于组件渲染前）
可以对单元格添加CSS样式，当需要改变某个单元格样式的时候可以使用该方法。 

version
    
9.7.0 

since
    
9.7.0
```
portlet.setCellStyleHandler(function (row, column, rowIndex, columnIndex) {
   if (columnIndex !== 0) return null
   let value = row.getCellValue(columnIndex)
   if (value > 1000) {
        return {
            background: 'red'
        }
    }
   return null
})
```

#### Parameters 参数
    * #####  handler: TableCellStyleHandler
单元格样式处理函数
####  Returns 返回值 void


###  setRenderCellHandler 
  * setRenderCellHandler(handlerTableRenderCellHandler)HtmlString


  * 单元格节点处理函数（适用于组件渲染前）
可以改变单元格的结构，当需要改变单元格结构（如添加图标、自定义格式化等）的时候可以使用该方法。 

version
    
9.7.0 

since
    
9.7.0
```
portlet.setRenderCellHandler(function (row, column, rowIndex, columnIndex) {
    if (columnIndex != 1) return null
    let value = row.getCellValue(columnIndex)
    let displayValue = row.getCellDisplayValue(columnIndex)
    if (value < 500) {
        return '<span style="color: red;"><i class="SmartbixIcons sx-icon-descending"/>' + displayValue + '</span>'
    }
    if (value > 1500) {
        return '<span style="color: blue;"><i class="SmartbixIcons sx-icon-ascending"/>' + displayValue + '</span>'
    }
    return null
})
```

#### Parameters 参数
    * #####  handler: TableRenderCellHandler
样式处理函数
####  Returns 返回值 HtmlString


###  setRenderHeaderHandler 
  * setRenderHeaderHandler(handlerTableRenderHeaderHandler)HtmlString


  * 表头节点处理函数（适用于组件渲染前）
可以改变表头的结构，当需要改变表头结构（如添加图标、自定义格式化等）的时候可以使用该方法。 

version
    
10.1.0 

since
    
10.1.0
```
portlet.setRenderHeaderHandler(function (header, rowIndex, columnIndex, value) {
    if (columnIndex % 2 === 0) {
        return '<span style="color: red;">' + value + '</span>'
    } else {
        return '<span style="color: blue;">' + value + '</span>'
    }
})
```

#### Parameters 参数
    * #####  handler: TableRenderHeaderHandler
表头处理函数
####  Returns 返回值 HtmlString


###  setRowStyleHandler 
  * setRowStyleHandler(handlerTableRowStyleHandler)void


  * 表格行样式处理函数（适用于组件渲染前）
可以对表格行添加CSS样式，当需要改变一整行样式的时候可以使用该方法。 

version
    
9.7.0 

since
    
9.7.0
```
portlet.setRowStyleHandler(function (row, rowIndex) {
   let value1 = row.getCellValue(1)
   if (value > 1000) {
        return {
            background: 'red'
        }
    }
   return null
})
```

#### Parameters 参数
    * #####  handler: TableRowStyleHandler
表格行样式处理函数
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


