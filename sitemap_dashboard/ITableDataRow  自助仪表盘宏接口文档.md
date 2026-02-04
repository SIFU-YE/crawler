### Hierarchy 层级
  * ITableDataRow


## Index 目录
###  Methods 方法 
  * getRowIndex
  * resetBackgroundStyle
  * resetTextStyle
  * setBackgroundStyle
  * setTextStyle


##  Methods 方法 
###  getCell 
  * getCell(columnIndexnumber)ITableCell


  * 获取指定列的单元格 

version
    
10.5.12 

since
    
10.5.12
```
const row: ITableDataRow = portlet.getRow(0);
const cell: ITableCell = row.getCell(0);
```

#### Parameters 参数
    * #####  columnIndex: number
列号，从0开始
####  Returns 返回值 ITableCell
单元格对象


###  getCells 
  * get 


  * 获取本行所有单元格 

version
    
10.5.12 

since
    
10.5.12
```
const row: ITableDataRow = portlet.getRow(0);
const cells: ITableCell[] = row.getCells();
```

####  Returns 返回值 ITableCell[]
本行所有单元格


###  getRowIndex 
  * getRowIndex()number


  * 

version
    
10.5.12 

since
    
10.5.12
```
const row: ITableDataRow = portlet.getRow(0);
const rowIndex: number = row.getRowIndex();
```

####  Returns 返回值 number
行号


###  resetBackgroundStyle 
  * resetBackgroundStyle()void


  * 重置自定义背景样式 

version
    
10.5.12 

since
    
10.5.12
```
const row: ITableDataRow = portlet.getRow(0);
row.resetBackgroundStyle();
```

####  Returns 返回值 void


###  resetTextStyle 
  * resetTextStyle()void


  * 重置自定义文字样式 

version
    
10.5.12 

since
    
10.5.12
```
const row: ITableDataRow = portlet.getRow(0);
row.resetTextStyle();
```

####  Returns 返回值 void


###  setBackgroundStyle 
  * setBackgroundStyle(styleITableCellBackgroundStyle)void


  * 设置行背景样式 

version
    
10.5.12 

since
    
10.5.12
```
const row: ITableDataRow = portlet.getRow(0);
const backgroundStyle: ITableCellBackgroundStyle = {
  backgroundColor: '#ee5',
  backgroundColorOpacity: 0.8
}
row.setBackgroundStyle(backgroundStyle);
```

#### Parameters 参数
    * #####  style: ITableCellBackgroundStyle
####  Returns 返回值 void


###  setTextStyle 
  * setTextStyle(styleITableCellTextStyle)void


  * 设置行的文字样式 

version
    
10.5.12 

since
    
10.5.12
```
const row: ITableDataRow = portlet.getRow(2);
const textStyle: ITableCellTextStyle = {
    fontSize: 16,
    textAlign: AlignType.CENTER,
    textBaseline: BaselineType.MIDDLE,
    fontFamily: 'Microsoft Yahei',
    fontWeight: FontWeightType.BOLDER,
    fill: '#5E105E',
    opacity: 0.8
}
row.setTextStyle(textStyle);
```

#### Parameters 参数
    * #####  style: ITableCellTextStyle
####  Returns 返回值 void


