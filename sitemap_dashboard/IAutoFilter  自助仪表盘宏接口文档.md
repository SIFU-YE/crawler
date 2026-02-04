com.aspose.cells.AutoFilter
### Hierarchy 层级
  * IAutoFilter


## Index 目录
###  Methods 方法 
  * addDateFilter
  * addFillColorFilter
  * addFontColorFilter
  * addIconFilter
  * dynamicFilter
  * filterTop10
  * getFilterColumns
  * matchBlanks
  * matchNonBlanks
  * removeDateFilter
  * removeFilter


##  Methods 方法 
###  addDateFilter 
  * addDateFilter(fieldIndexnumber, dateTimeGroupingTypenumber, yearnumber, monthnumber, daynumber, hournumber, minutenumber, secondnumber)void


  * void addDateFilter(int, int, int, int, int, int, int, int)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  dateTimeGroupingType: number
    * #####  year: number
    * #####  month: number
    * #####  day: number
    * #####  hour: number
    * #####  minute: number
    * #####  second: number
####  Returns 返回值 void


###  addFillColorFilter 
  * addFillColorFilter(fieldIndexnumber, patternnumber, foregroundColorICellsColor, backgroundColorICellsColor)void


  * void addFillColorFilter(int, int, com.aspose.cells.CellsColor, com.aspose.cells.CellsColor)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  pattern: number
    * #####  foregroundColor: ICellsColor
    * #####  backgroundColor: ICellsColor
####  Returns 返回值 void


###  addFilter 
  * addFilter(fieldIndexnumber, criteriastring)void


  * void addFilter(int, java.lang.String)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  criteria: string
####  Returns 返回值 void


###  addFontColorFilter 
  * addFontColorFilter(fieldIndexnumber, colorICellsColor)void


  * void addFontColorFilter(int, com.aspose.cells.CellsColor)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  color: ICellsColor
####  Returns 返回值 void


###  addIconFilter 
  * addIconFilter(fieldIndexnumber, iconSetTypenumber, iconIdnumber)void


  * void addIconFilter(int, int, int)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  iconSetType: number
    * #####  iconId: number
####  Returns 返回值 void


###  custom 
  * custom(fieldIndexnumber, operatorType1number, criteria1any)void
  * custom(fieldIndexnumber, operatorType1number, criteria1any, isAndboolean, operatorType2number, criteria2any)void


  * void custom(int, int, java.lang.Object)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  operatorType1: number
    * #####  criteria1: any
####  Returns 返回值 void
  * void custom(int, int, java.lang.Object, boolean, int, java.lang.Object)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  operatorType1: number
    * #####  criteria1: any
    * #####  isAnd: boolean
    * #####  operatorType2: number
    * #####  criteria2: any
####  Returns 返回值 void


###  dynamicFilter 
  * dynamicFilter(fieldIndexnumber, dynamicFilterTypenumber)void


  * void dynamicFilter(int, int)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  dynamicFilterType: number
####  Returns 返回值 void


###  filter 
  * filter(fieldIndexnumber, criteriastring)void


  * void filter(int, java.lang.String)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  criteria: string
####  Returns 返回值 void


###  filterTop10 
  * filterTop10(fieldIndexnumber, isTopboolean, isPercentboolean, itemCountnumber)void


  * void filterTop10(int, boolean, boolean, int)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  isTop: boolean
    * #####  isPercent: boolean
    * #####  itemCount: number
####  Returns 返回值 void


###  getFilterColumns 
  * getFilterColumns()IFilterColumnCollection


  * com.aspose.cells.FilterColumnCollection getFilterColumns()
####  Returns 返回值 IFilterColumnCollection


###  getRange 
  * getRange()string


  * java.lang.String getRange()
####  Returns 返回值 string


###  getSorter 
  * get 


  * com.aspose.cells.DataSorter getSorter()
####  Returns 返回值 IDataSorter


###  matchBlanks 
  * matchBlanks(fieldIndexnumber)void


  * void matchBlanks(int)
#### Parameters 参数
    * #####  fieldIndex: number
####  Returns 返回值 void


###  matchNonBlanks 
  * matchNonBlanks(fieldIndexnumber)void


  * void matchNonBlanks(int)
#### Parameters 参数
    * #####  fieldIndex: number
####  Returns 返回值 void


###  refresh 
  * refresh()number[]
  * refresh(hideRowsboolean)number[]


  * int[] refresh()
####  Returns 返回值 number[]
  * int[] refresh(boolean)
#### Parameters 参数
    * #####  hideRows: boolean
####  Returns 返回值 number[]


###  removeDateFilter 
  * removeDateFilter(fieldIndexnumber, dateTimeGroupingTypenumber, yearnumber, monthnumber, daynumber, hournumber, minutenumber, secondnumber)void


  * void removeDateFilter(int, int, int, int, int, int, int, int)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  dateTimeGroupingType: number
    * #####  year: number
    * #####  month: number
    * #####  day: number
    * #####  hour: number
    * #####  minute: number
    * #####  second: number
####  Returns 返回值 void


###  removeFilter 
  * removeFilter(fieldIndexnumber)void
  * removeFilter(fieldIndexnumber, criteriastring)void


  * void removeFilter(int)
#### Parameters 参数
    * #####  fieldIndex: number
####  Returns 返回值 void
  * void removeFilter(int, java.lang.String)
#### Parameters 参数
    * #####  fieldIndex: number
    * #####  criteria: string
####  Returns 返回值 void


###  setRange 
  * setRange(rownumber, startColumnnumber, endColumnnumber)void
  * setRange(valuestring)void


  * void setRange(int, int, int)
#### Parameters 参数
    * #####  row: number
    * #####  startColumn: number
    * #####  endColumn: number
####  Returns 返回值 void
  * void setRange(java.lang.String)
#### Parameters 参数
    * #####  value: string
####  Returns 返回值 void


###  show 
  * showAll()void


  * void showAll()
####  Returns 返回值 void


