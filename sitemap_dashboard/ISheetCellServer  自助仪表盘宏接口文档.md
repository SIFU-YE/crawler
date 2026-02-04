WEB电子表格单元格接口
### Hierarchy 层级
  * ISheetCellServer


## Index 目录
###  Methods 方法 
  * getCellPosition
  * getDisplayValue
  * getRelativeCells
  * getTemplateCellPosition


##  Methods 方法 
###  getCellPosition 
  * getCellPosition()ICellPosition


  * 获取单元格的位置信息（当前单元格的位置信息） 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 ICellPosition


###  getDisplayValue 
  * getDisplayValue()string


  * 获取单元格格式化过后的显示值 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 string


###  getRelativeCells 
  * getRelativeCells(rowIndexnumber, columnIndexnumber)ISheetCellServer[]
  * getRelativeCells(positionICellPosition)ISheetCellServer[]
  * getRelativeCells(cellstring)ISheetCellServer[]


  * 获取与当前单元格相关联的同一分组内单元格（即同一个分组内的父单元格、子单元格）
注意：这里的参数是模板中原始的单元格，即未进行扩展的单元格
更加详细的注释见`getRelativeCells(cell: string)`方法中的注释 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  rowIndex: number
行索引（从0开始）
    * #####  columnIndex: number
列索引（从0开始）
####  Returns 返回值 ISheetCellServer[]
  * 获取与当前单元格相关联的同一分组内单元格（即同一个分组内的父单元格、子单元格）
注意：这里的参数是模板中原始的单元格，即未进行扩展的单元格
更加详细的注释见`getRelativeCells(cell: string)`方法中的注释 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  position: ICellPosition
单元格位置
####  Returns 返回值 ISheetCellServer[]
  * 获取与当前单元格相关联的同一分组内单元格（即同一个分组内的父单元格、子单元格）
注意：这里的参数是模板中原始的单元格，即未进行扩展的单元格
一般和`ISheetServer.getExpandedPositions`一起使用 

version
    
10.1.0 

since
    
10.1.0
```
let expandedPositions = sheet.getExpandedPositions('B2');
for (let i = 0; i < expandedPositions.length; i++) {
  let cell = sheet.getCell(expandedPositions[i]);
  let relativeCells = cell.getRelativeCells('C2')
}
```

#### Parameters 参数
    * #####  cell: string
单元格名称（例如：B4）
####  Returns 返回值 ISheetCellServer[]


###  getTemplateCellPosition 
  * getTemplateCellPosition()ICellPosition


  * 获取单元格在原始模板中的位置信息（即未进行扩展的单元格位置） 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 ICellPosition


###  getValue 
  * getValue()any


  * 获取单元格的值 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 any
可能的值类型有：null | Boolean | Double | Integer | String


###  setValue 
  * setValue(valueObject)void


  * 设置单元格值 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  value: Object
####  Returns 返回值 void


