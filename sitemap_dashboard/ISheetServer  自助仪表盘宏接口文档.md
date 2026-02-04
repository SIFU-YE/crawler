WEB电子表格sheet接口
### Hierarchy 层级
  * ISheetServer


## Index 目录
###  Methods 方法 
  * addRuleLink
  * getExpandedPositions
  * getWorksheet


##  Methods 方法 
###  addRuleLink 
  * addRuleLink(rowIndexnumber, columnIndexnumber, ruleNamestring, parameterValuesobject[])void
  * addRuleLink(cellstring, ruleNamestring, parameterValuesobject[])void
  * addRuleLink(positionICellPosition, ruleNamestring, parameterValuesobject[])void


  * 添加跳转规则 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  rowIndex: number
行索引（从0开始）
    * #####  columnIndex: number
列索引（从0开始）
    * #####  ruleName: string
    * #####  parameterValues: object[]
传递的参数值数组
####  Returns 返回值 void
  * 添加跳转规则 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  cell: string
单元格名称（例如：B4）
    * #####  ruleName: string
    * #####  parameterValues: object[]
传递的参数值数组
####  Returns 返回值 void
  * 添加跳转规则 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  position: ICellPosition
单元格位置
    * #####  ruleName: string
    * #####  parameterValues: object[]
传递的参数值数组
####  Returns 返回值 void


###  getCell 
  * getCell(rowIndexnumber, columnIndexnumber)ISheetCellServer
  * getCell(cellstring)ISheetCellServer
  * getCell(positionICellPosition)ISheetCellServer


  * 获取单元格 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  rowIndex: number
行索引（从0开始）
    * #####  columnIndex: number
列索引（从0开始）
####  Returns 返回值 ISheetCellServer
  * 获取单元格 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  cell: string
单元格名称（例如：B4）
####  Returns 返回值 ISheetCellServer
  * 获取单元格 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  position: ICellPosition
单元格位置
####  Returns 返回值 ISheetCellServer


###  getExpandedPositions 
  * getExpandedPositions(rowIndexnumber, columnIndexnumber)ICellPosition[]
  * getExpandedPositions(cellstring)ICellPosition[]


  * 获取单元格扩展后的位置
注意：这里传入的参数是模板中的单元格位置 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  rowIndex: number
行索引（从0开始）
    * #####  columnIndex: number
列索引（从0开始）
####  Returns 返回值 ICellPosition[]
  * 获取单元格扩展后的位置
注意：这里传入的参数是模板中的单元格位置 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  cell: string
单元格名称（例如：B4）
####  Returns 返回值 ICellPosition[]


###  getName 
  * getName()string


  * 获取sheet页名称 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 string


###  getWorksheet 
  * getWorksheet()IWorksheet


  * 获取Worksheet对象
详细API参考aspose官方文档：https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 IWorksheet


