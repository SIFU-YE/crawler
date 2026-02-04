交叉表组件接口对象
### Hierarchy 层级
  * IPortlet
    * ITableCrossPortlet


## Index 目录
###  Methods 方法 
  * cancelAsFilter
  * getCellDisplayValue
  * getCellValue
  * getColHeader
  * getCornerHeader
  * getRowHeader
  * isMaximized
  * resetLinkage
  * restoreDown
  * setAsFilter
  * setRenderCellHandler
  * setRenderColHeaderHandler
  * setRenderCornerHeaderHandler
  * setRenderRowHeaderHandler


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


###  getCell 
  * getCell(rowIndexnumber, columnIndexnumber)ITableCell


  * 获取单元格对象 

version
    
10.5.15 

since
    
10.5.15
```
const cell: ITableCell = portlet.getCell(0, 0);
```

#### Parameters 参数
    * #####  rowIndex: number
行号，从0开始
    * #####  columnIndex: number
列号，从0开始
####  Returns 返回值 ITableCell
单元格对象


###  getCellDisplayValue 
  * getCellDisplayValue(rowIndexnumber, columnIndexnumber)string


  * 获取单元格显示值 

version
    
9.7.0 

since
    
9.7.0
```
portlet.getCellDisplayValue(0, 0);
```

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
```
portlet.getCellValue(0, 0);
```

#### Parameters 参数
    * #####  rowIndex: number
行序号（序号从0开始）
    * #####  columnIndex: number
列序号（序号从0开始）
####  Returns 返回值 string


###  getColHeader 
  * getColHeader(rowIndexnumber, columnIndexnumber)ITableColHeader


  * 获取列头对象 

version
    
10.5.15 

since
    
10.5.15
```
const colHeader: ITableColHeader = portlet.getColHeader(0, 0);
```

#### Parameters 参数
    * #####  rowIndex: number
行号，从0开始
    * #####  columnIndex: number
列号，从0开始
####  Returns 返回值 ITableColHeader
列头对象


###  getCornerHeader 
  * getCornerHeader(columnIndexnumber)ITableCornerHeader


  * 获取角头对象 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
```

#### Parameters 参数
    * #####  columnIndex: number
列号，从0开始
####  Returns 返回值 ITableCornerHeader


###  get 
  * getId()string


  * 获取组件id 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  get 
  * getRow(rowIndexnumber)ITableDataRow


  * 获取行对象 

version
    
10.5.15 

since
    
10.5.15
```
const row: ITableDataRow = portlet.getRow(0);
```

#### Parameters 参数
    * #####  rowIndex: number
行号，从0开始
####  Returns 返回值 ITableDataRow
行对象


###  getRowHeader 
  * getRowHeader(rowIndexnumber, columnIndexnumber)ITableRowHeader


  * 获取行头对象 

version
    
10.5.15 

since
    
10.5.15
```
const rowHeader: ITableRowHeader = portlet.getRowHeader(0, 0);
```

#### Parameters 参数
    * #####  rowIndex: number
行号，从0开始
    * #####  columnIndex: number
列号，从0开始
####  Returns 返回值 ITableRowHeader


###  getRows 
  * get 


  * 获取所有行，onAfterRender时可用 

version
    
10.5.15 

since
    
10.5.15
```
const rows: ITableDataRow[] = portlet.getRows();
```

####  Returns 返回值 ITableDataRow[]
所有行


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


###  setCursor 
  * setCursor(cursorCursorstring)void


  * 设置鼠标指针 

version
    
10.5.15 

since
    
10.5.15
```
portlet.setRenderCellHandler((cell) => {
  cell.addEventListener(TableCellEvent.HOVER, () => {
    portlet.setCursor(Cursor.POINTER);
  });
  cell.addEventListener(TableCellEvent.HOVER_OFF, () => {
    portlet.setCursor(Cursor.DEFAULT);
  });
});
```

#### Parameters 参数
    * #####  cursor: Cursorstring
####  Returns 返回值 void


###  setRenderCellHandler 
  * setRenderCellHandler(handlerIRenderCellHandler)void


  * 设置单元格渲染handler 

version
    
10.5.15 

since
    
10.5.15
```
portlet.setRenderCellHandler((cell, row, rowIndex, columnIndex) => {
    if (cell.getValue() > 5000) {
        const textStyle: ITableCellTextStyle = {
            fontSize: 14,
            textAlign: AlignType.CENTER,
            textBaseline: BaselineType.TOP,
            fontFamily: 'Microsoft Yahei',
            fontWeight: FontWeightType.BOLDER,
            fill: '#0E0EFE',
            opacity: 0.8
        }
        cell.setTextStyle(textStyle);
    } else if (cell.getValue() < 3000) {
        const textStyle: ITableCellTextStyle = {
            fontSize: 14,
            textAlign: AlignType.CENTER,
            textBaseline: BaselineType.BOTTOM,
            fontFamily: 'Microsoft Yahei',
            fontWeight: FontWeightType.BOLDER,
            fill: '#FE0E0E',
            opacity: 0.8
        }
        cell.setTextStyle(textStyle);
    }
});
```

#### Parameters 参数
    * #####  handler: IRenderCellHandler
单元格渲染handler，入参为ITableCell, ITableDataRow, rowIndex, columnIndex
####  Returns 返回值 void


###  setRenderColHeaderHandler 
  * setRenderColHeaderHandler(handlerIRenderColHeaderHandler)void


  * 设置列头渲染handler 

version
    
10.5.15 

since
    
10.5.15
```
portlet.setRenderColHeaderHandler((colHeader, rowIndex, columnIndex) => {
    if (columnIndex === 1) {
        const backgroundStyle: ITableCellBackgroundStyle = {
            backgroundColor: 'green',
            backgroundColorOpacity: 0.5
        }
        colHeader.setBackgroundStyle(backgroundStyle)
    }
});
```

#### Parameters 参数
    * #####  handler: IRenderColHeaderHandler
列头渲染handler，入参为ITableColHeader, rowIndex, columnIndex
####  Returns 返回值 void


###  setRenderCornerHeaderHandler 
  * setRenderCornerHeaderHandler(handlerIRenderCornerHeaderHandler)void


  * 设置角头渲染handler 

version
    
10.5.15 

since
    
10.5.15
```
portlet.setRenderCornerHeaderHandler((cornerHeader, columnIndex) => {
    if (columnIndex === 1) {
        const backgroundStyle: ITableCellBackgroundStyle = {
            backgroundColor: 'green',
            backgroundColorOpacity: 0.5
        }
        cornerHeader.setBackgroundStyle(backgroundStyle)
    }
});
```

#### Parameters 参数
    * #####  handler: IRenderCornerHeaderHandler
角头渲染handler，入参为ITableCornerHeader, columnIndex
####  Returns 返回值 void


###  setRenderRowHeaderHandler 
  * setRenderRowHeaderHandler(handlerIRenderRowHeaderHandler)void


  * 设置行头渲染handler 

version
    
10.5.15 

since
    
10.5.15
```
portlet.setRenderRowHeaderHandler((rowHeader, rowIndex, columnIndex) => {
    if (rowIndex === 1) {
        const backgroundStyle: ITableCellBackgroundStyle = {
            backgroundColor: 'green',
            backgroundColorOpacity: 0.5
        }
        rowHeader.setBackgroundStyle(backgroundStyle)
    }
});
```

#### Parameters 参数
    * #####  handler: IRenderRowHeaderHandler
行头渲染handler，入参为ITableRowHeader, rowIndex, columnIndex
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


