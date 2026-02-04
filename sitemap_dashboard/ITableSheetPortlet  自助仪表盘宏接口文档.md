WEB电子表格组件接口对象
### Hierarchy 层级
  * IPortlet
    * ITableSheetPortlet


## Index 目录
###  Methods 方法 
  * cancelAsFilter
  * getActiveSheet
  * getAllSheets
  * getColumnCount
  * getCustomProperty
  * getExpandedPositions
  * getRowCount
  * getVisibleSheets
  * isMaximized
  * resetLinkage
  * restoreDown
  * setActiveSheet
  * setAsFilter
  * setSheetVisible


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


###  doRefresh 
  * doRefresh()void


  * 刷新当前sheet页 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 void


###  getActiveSheet 
  * getActiveSheet()string


  * 获取当前激活的sheet页名称 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  getAllSheets 
  * getAllSheets()string[]


  * 获取所有的sheet页名称 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 string[]


###  getCell 
  * getCell(rowIndexnumber, columnIndexnumber)ISheetCell
  * getCell(cellstring)ISheetCell


  * 获取web电子表格单元格（适用于组件渲染后） 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  rowIndex: number
行索引（从0开始）
    * #####  columnIndex: number
列索引（从0开始）
####  Returns 返回值 ISheetCell
  * 获取web电子表格单元格（适用于组件渲染后） 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  cell: string
单元格名称（例如：B4）
####  Returns 返回值 ISheetCell


###  getColumn 
  * getColumn(columnnumberstring)ISheetColumn


  * 

version
    
10.1.0 

since
    
10.1.0
```
// 获取B列
let columnB = portlet.getColumn("B");
//下面这种方式也行
columnB = portlet.getColumn(1);
```

#### Parameters 参数
    * #####  column: numberstring
列索引（从0开始）或者列名（例如B）
####  Returns 返回值 ISheetColumn


###  getColumnCount 
  * getColumnCount()number


  * 获取当前页面的总列数（适用于组件渲染后） 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 number


###  getCustomProperty 
  * getCustomProperty(keystring)Object


  * 获取自定义的属性值
需要先在`onBeforeOutput`事件中设置自定义的属性，代码如下：
```
portletServer.setCustomProperty({{ key }}， {{ value }});
```


version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  key: string
####  Returns 返回值 Object


###  getExpandedPositions 
  * getExpandedPositions(rowIndexnumber, columnIndexnumber)string[]
  * getExpandedPositions(cellstring)string[]


  * 获取单元格扩展后的位置
需要先在`onBeforeOutput`事件中将展开后的所有单元格输出到客户端，代码如下：
```
portletServer.printExpandedPositions();
```


version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  rowIndex: number
行索引（从0开始）
    * #####  columnIndex: number
列索引（从0开始）
####  Returns 返回值 string[]
单元格扩展后的位置（例如：['B1', 'B2'...,'B100']）
  * 获取单元格扩展后的位置
需要先在`onBeforeOutput`事件中将展开后的所有单元格输出到客户端，代码如下：
```
portletServer.printExpandedPositions();
```


version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  cell: string
单元格名称（例如B1）
####  Returns 返回值 string[]
单元格扩展后的位置（例如：['B1', 'B2'...,'B100']）


###  get 
  * getId()string


  * 获取组件id 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  get 
  * getRow(rowIndexnumber)ISheetRow


  * 获取行（适用于组件渲染后） 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  rowIndex: number
行索引（从0开始）
####  Returns 返回值 ISheetRow


###  getRowCount 
  * getRowCount()number


  * 获取当前页面的总行数（适用于组件渲染后） 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 number


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


###  getVisibleSheets 
  * getVisibleSheets()string[]


  * 获取可见的sheet页名称 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 string[]


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


###  marquee 
  * marquee(cellstringnumber[], options?: MarqueeOptions)void


  * 跑马灯（适用于组件渲染后） 

version
    
10.1.0 

since
    
10.1.0
    1. 单元格F8添加跑马灯，默认取单元格F8中的文本：
```
portlet.marquee("F8");
```

    1. 单元格F8添加跑马灯，添加自定义文本：
```
portlet.marquee("F8", {
   data: "单元格F8添加跑马灯，添加自定义文本",
   speed: 5000
});
```

#### Parameters 参数
    * #####  cell: stringnumber[]
单元格名称（例如：F8）或者单元格位置[行索引，列索引]（例如：[7, 5]）
    * #####  Optional options: MarqueeOptions
跑马灯配置项，可选
####  Returns 返回值 void


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


###  setActiveSheet 
  * setActiveSheet(sheetstringnumber)void


  * 设置激活的sheet页（适用于组件渲染后） 

version
    
9.7.0 

since
    
9.7.0
#### Parameters 参数
    * #####  sheet: stringnumber
sheet页名称或sheet页索引（从0开始）
####  Returns 返回值 void
**示例代码**
```
// 激活Sheet2
portlet.setActiveSheet("Sheet2");
```



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


###  setSheetVisible 
  * setSheetVisible(sheetstringnumber, visible?: boolean)void


  * 设置sheet页是否显示 

version
    
10.1.0 

since
    
10.1.0
**示例代码**
```
// 隐藏Sheet2
portlet.setSheetVisible("Sheet2", false);

// 显示Sheet3
portlet.setSheetVisible("Sheet3", true);
```

#### Parameters 参数
    * #####  sheet: stringnumber
sheet页名称或者sheet页索引（从0开始）
    * #####  Optional visible: boolean
sheet页是显示还是隐藏
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


