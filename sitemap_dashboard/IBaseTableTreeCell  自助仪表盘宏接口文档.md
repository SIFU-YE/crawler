树状表基础单元格对象
### Hierarchy 层级
  * IBaseTableTreeCell


## Index 目录
###  Methods 方法 
  * addEventListener
  * getBackgroundStyle
  * getColumnIndex
  * getDisplayValue
  * getRowIndex
  * getTextStyle
  * removeEventListener
  * resetBackgroundStyle
  * resetTextStyle
  * setBackgroundStyle
  * setTextStyle


##  Methods 方法 
###  addEventListener 
  * addEventListener(eventTableCellEvent, handlerITableCellEventListener)void


  * 添加事件监听器 

version


since

#### Parameters 参数
    * #####  event: TableCellEvent
单元格事件
    * #####  handler: ITableCellEventListener
事件监听器函数
####  Returns 返回值 void


###  getBackgroundStyle 
  * getBackgroundStyle()ITableCellBackgroundStyle


  * 获取背景样式 

version


since

####  Returns 返回值 ITableCellBackgroundStyle
背景样式


###  getColumnIndex 
  * getColumnIndex()number


  * 获取列索引 

version


since

####  Returns 返回值 number
列索引


###  getDisplayValue 
  * getDisplayValue()string


  * 获取显示值 

version


since

####  Returns 返回值 string
显示值


###  getRowIndex 
  * getRowIndex()number


  * 获取行索引 

version


since

####  Returns 返回值 number
行索引


###  getTextStyle 
  * getText


  * 获取文字样式 

version


since

####  Returns 返回值 ITableCellTextStyle
文字样式


###  getValue 
  * getValue()stringnumber


  * 获取真实值 

version


since

####  Returns 返回值 stringnumber
真实值


###  removeEventListener 
  * removeEventListener(eventTableCellEvent, handlerITableCellEventListener)void


  * 移除事件监听器 

version


since

#### Parameters 参数
    * #####  event: TableCellEvent
单元格事件
    * #####  handler: ITableCellEventListener
事件监听器函数
####  Returns 返回值 void


###  resetBackgroundStyle 
  * resetBackgroundStyle()void


  * 重置自定义背景样式 

version


since

####  Returns 返回值 void


###  resetTextStyle 
  * resetTextStyle()void


  * 重置自定义文字样式 

version


since

####  Returns 返回值 void


###  setBackgroundStyle 
  * setBackgroundStyle(styleITableCellBackgroundStyle)void


  * 设置单元格背景样式 

version


since

#### Parameters 参数
    * #####  style: ITableCellBackgroundStyle
单元格背景样式
####  Returns 返回值 void


###  setTextStyle 
  * setTextStyle(styleITableCellTextStyle)void


  * 设置文字样式 

version


since

#### Parameters 参数
    * #####  style: ITableCellTextStyle
####  Returns 返回值 void


