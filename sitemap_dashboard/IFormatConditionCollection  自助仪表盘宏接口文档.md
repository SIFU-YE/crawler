com.aspose.cells.FormatConditionCollection
### Hierarchy 层级
  * IFormatConditionCollection


## Index 目录
###  Methods 方法 
  * addCondition
  * getRangeCount
  * removeCondition


##  Methods 方法 
###  add 
  * add(cellAreaICellArea, typenumber, operatorTypenumber, formula1string, formula2string)number[]


  * int[] add(com.aspose.cells.CellArea, int, int, java.lang.String, java.lang.String)
#### Parameters 参数
    * #####  cellArea: ICellArea
    * #####  type: number
    * #####  operatorType: number
    * #####  formula1: string
    * #####  formula2: string
####  Returns 返回值 number[]


###  addArea 
  * addArea(cellAreaICellArea)number


  * int addArea(com.aspose.cells.CellArea)
#### Parameters 参数
    * #####  cellArea: ICellArea
####  Returns 返回值 number


###  addCondition 
  * addCondition(typenumber)number
  * addCondition(typenumber, operatorTypenumber, formula1string, formula2string)number


  * int addCondition(int)
#### Parameters 参数
    * #####  type: number
####  Returns 返回值 number
  * int addCondition(int, int, java.lang.String, java.lang.String)
#### Parameters 参数
    * #####  type: number
    * #####  operatorType: number
    * #####  formula1: string
    * #####  formula2: string
####  Returns 返回值 number


###  get 
  * get(indexnumber)IFormatCondition


  * com.aspose.cells.FormatCondition get(int)
#### Parameters 参数
    * #####  index: number
####  Returns 返回值 IFormatCondition


###  getCellArea 
  * getCellArea(indexnumber)ICellArea


  * com.aspose.cells.CellArea getCellArea(int)
#### Parameters 参数
    * #####  index: number
####  Returns 返回值 ICellArea


###  getCount 
  * getCount()number


  * int getCount()
####  Returns 返回值 number


###  getRangeCount 
  * getRangeCount()number


  * int getRangeCount()
####  Returns 返回值 number


###  removeArea 
  * removeArea(startRownumber, startColumnnumber, totalRowsnumber, totalColumnsnumber)boolean
  * removeArea(indexnumber)void


  * boolean removeArea(int, int, int, int)
#### Parameters 参数
    * #####  startRow: number
    * #####  startColumn: number
    * #####  totalRows: number
    * #####  totalColumns: number
####  Returns 返回值 boolean
  * void removeArea(int)
#### Parameters 参数
    * #####  index: number
####  Returns 返回值 void


###  removeCondition 
  * removeCondition(indexnumber)void


  * void removeCondition(int)
#### Parameters 参数
    * #####  index: number
####  Returns 返回值 void


