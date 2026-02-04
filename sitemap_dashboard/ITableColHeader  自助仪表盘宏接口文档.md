### Hierarchy 层级
  * ITableColHeader


## Index 目录
###  Methods 方法 
  * addEventListener
  * addPrefixIcon
  * addSuffixIcon
  * getBackgroundStyle
  * getColumnIndex
  * getDisplayValue
  * getRowIndex
  * getTextStyle
  * removeEventListener
  * resetBackgroundStyle
  * resetTextStyle
  * setBackgroundStyle
  * setColBorderStyle
  * setDisplayValue
  * setTextStyle


##  Methods 方法 
###  addEventListener 
  * addEventListener(eventTableCellEvent, handlerITableCellEventListener)void


  * 添加事件监听器 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
const handler: ITableCellEventListener = () => {
  alert('clicked');
}
colHeader.addEventListener(TableCellEvent.CLICK, handler);
```

#### Parameters 参数
    * #####  event: TableCellEvent
    * #####  handler: ITableCellEventListener
列头事件监听器
####  Returns 返回值 void


###  addPrefixIcon 
  * addPrefixIcon(imagestringIconName, options?: ICustomIconOptions)string


  * 在文字前面添加自定义图标 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
const icon: string = 'base64内容或内置图标名称'
colHeader.addPrefixIcon(icon);
```

#### Parameters 参数
    * #####  image: stringIconName
图片base64或内置图标名称
    * #####  Optional options: ICustomIconOptions
####  Returns 返回值 string
图标id，可用于移除图标


###  addSuffixIcon 
  * addSuffixIcon(imagestringIconName, options?: ICustomIconOptions)string


  * 在文字后面添加自定义图标 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
const icon: string = 'base64内容或内置图标名称'
colHeader.addSuffixIcon(icon);
```

#### Parameters 参数
    * #####  image: stringIconName
图片base64或内置图标名称
    * #####  Optional options: ICustomIconOptions
####  Returns 返回值 string
图标id，可用于移除图标


###  getBackgroundStyle 
  * getBackgroundStyle()ITableCellBackgroundStyle


  * 获取单元格背景样式 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
const backgroundStyle: ITableCellBackgroundStyle = colHeader.getBackgroundStyle();
```

####  Returns 返回值 ITableCellBackgroundStyle
单元格背景样式


###  getColumnIndex 
  * getColumnIndex()number


  * 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
const columnIndex: number = colHeader.getColumnIndex();
```

####  Returns 返回值 number
列号，从0开始


###  getDisplayValue 
  * getDisplayValue()string


  * 获取列头内容 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
const label: string = colHeader.getDisplayValue();
```

####  Returns 返回值 string
列头内容


###  getRowIndex 
  * getRowIndex()number


  * ####  Returns 返回值 number


###  getTextStyle 
  * getText


  * 获取文字样式 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
const textStyle: ITableCellTextStyle = colHeader.getTextStyle();
```

####  Returns 返回值 ITableCellTextStyle
文字样式


###  removeEventListener 
  * removeEventListener(eventTableCellEvent, handlerITableCellEventListener)void


  * 移除事件监听器 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
const handler: TableCellEvent = () => {
  alert('clicked');
}
colHeader.addEventListener(TableCellEvent.CLICK, handler);
colHeader.removeEventListener(TableCellEvent.CLICK, handler);
```

#### Parameters 参数
    * #####  event: TableCellEvent
    * #####  handler: ITableCellEventListener
列头事件监听器
####  Returns 返回值 void


###  removeIcon 
  * removeIcon(iconIdstringIconName)void


  * 移除自定义图标 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
const icon: string = 'base64内容或内置图标名称'
const iconId: string = colHeader.addSuffixIcon(icon);
colHeader.removeIcon(iconId);
```

#### Parameters 参数
    * #####  iconId: stringIconName
图标id或内置图标名称
####  Returns 返回值 void


###  resetBackgroundStyle 
  * resetBackgroundStyle()void


  * 重置自定义背景样式 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
colHeader.resetBackgroundStyle();
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
const colHeader: ITableColHeader = portlet.getColHeader(0);
colHeader.resetTextStyle();
```

####  Returns 返回值 void


###  setBackgroundStyle 
  * setBackgroundStyle(styleITableCellBackgroundStyle)void


  * 设置单元格背景样式 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
const backgroundStyle: ITableCellBackgroundStyle = {
    backgroundColor: '#333',
    backgroundColorOpacity: 0.8
}
colHeader.setBackgroundStyle(backgroundStyle);
```

#### Parameters 参数
    * #####  style: ITableCellBackgroundStyle
单元格背景样式
####  Returns 返回值 void


###  setColBorderStyle 
  * setColBorderStyle(styleITableCellBorder)void


  * 设置列头单元格边框线样式 

version


since
    
11 (2024-11)
```
const cell: ITableColHeader = portlet.getColHeader(1)
const borderStyle: ITableCellBorder = {
    // 按照顺序 依次是上、右、下、左边框的样式
    borderColor: ['rgb(2, 23, 51)', 'rgb(2, 23, 51)', 'rgb(2, 23, 51)', 'rgb(2, 23, 51)'],
    // 对应下标位置没有值则默认取第一个值
    borderColorOpacity: [1],
    borderWidth: [10, 20, 10, 30]
}
cell.setColBorderStyle(borderStyle);
```

#### Parameters 参数
    * #####  style: ITableCellBorder
单元格边框线样式
####  Returns 返回值 void


###  setDisplayValue 
  * setDisplayValue(labelstring)void


  * 设置列头内容 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
colHeader.setDisplayValue('TEST_LABEL');
```

#### Parameters 参数
    * #####  label: string
####  Returns 返回值 void


###  setTextStyle 
  * setTextStyle(styleITableCellTextStyle)void


  * 设置文字样式 

version
    
10.5.12 

since
    
10.5.12
```
const colHeader: ITableColHeader = portlet.getColHeader(0);
const textStyle: ITableCellTextStyle = {
    fontSize: 16,
    textAlign: AlignType.CENTER,
    textBaseline: BaselineType.BOTTOM,
    fontFamily: 'Microsoft Yahei',
    fontWeight: FontWeightType.BOLDER,
    fill: '#00FE00',
    opacity: 0.8
}
colHeader.setTextStyle(textStyle);
```

#### Parameters 参数
    * #####  style: ITableCellTextStyle
####  Returns 返回值 void


