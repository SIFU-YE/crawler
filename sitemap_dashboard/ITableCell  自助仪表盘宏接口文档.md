### Hierarchy 层级
  * ITableCell


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
  * removeIcon
  * resetBackgroundStyle
  * resetTextStyle
  * setBackgroundStyle
  * setBorderStyle
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
const cell: ITableCell = portlet.getCell(2, 0);
const handler: ITableCellEventListener = () => {
  alert('clicked');
};
cell.addEventListener(TableCellEvent.CLICK, handler);
```

#### Parameters 参数
    * #####  event: TableCellEvent
单元格事件
    * #####  handler: ITableCellEventListener
单元格事件监听器
####  Returns 返回值 void


###  addPrefixIcon 
  * addPrefixIcon(imagestringIconName, options?: ICustomIconOptions)string


  * 在文字前面添加自定义图标 

version
    
10.5.12 

since
    
10.5.12
```
const cell: ITableCell = portlet.getCell(2, 0);
const icon: string = 'base64内容或内置图标名称';
cell.addPrefixIcon(icon);
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
const cell: ITableCell = portlet.getCell(2, 0);
const icon: string = 'base64内容或内置图标名称';
cell.addSuffixIcon(icon);
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
####  Returns 返回值 ITableCellBackgroundStyle
单元格背景样式
```
const cell: ITableCell = portlet.getCell(0, 0);
const backgroudStyle: ITableCellBackgroundStyle = cell.getBackgroundStyle();
```



###  getColumnIndex 
  * getColumnIndex()number


  * 

version
    
10.5.12 

since
    
10.5.12
```
const cell: ITableCell = portlet.getCell(2, 0);
const columnIndex: number = cell.getColumnIndex();
```

####  Returns 返回值 number
列号，从0开始


###  getDisplayValue 
  * getDisplayValue()string


  * 获取单元格显示值 

version
    
10.5.12 

since
    
10.5.12
```
const cell: ITableCell = portlet.getCell(0, 0);
const displayValue: string = cell.getDisplayValue();
```

####  Returns 返回值 string
显示值


###  getRowIndex 
  * getRowIndex()number


  * 

version
    
10.5.12 

since
    
10.5.12
```
const cell: ITableCell = portlet.getCell(2, 0);
const rowIndex: number = cell.getRowIndex();
```

####  Returns 返回值 number
行号，从0开始


###  getTextStyle 
  * getText


  * 获取文字样式 

version
    
10.5.12 

since
    
10.5.12
####  Returns 返回值 ITableCellTextStyle
文字样式
```
const cell: ITableCell = portlet.getCell(2, 0);
const textStyle: ITableCellTextStyle = cell.getTextStyle();
```



###  getValue 
  * getValue()stringnumber


  * 获取单元格真实值 

version
    
10.5.12 

since
    
10.5.12
```
const cell: ITableCell = portlet.getCell(2, 0);
const value: number | string  = cell.getValue();
```

####  Returns 返回值 stringnumber
真实值


###  removeEventListener 
  * removeEventListener(eventTableCellEvent, handlerITableCellEventListener)void


  * 移除事件监听器 

version
    
10.5.12 

since
    
10.5.12
```
const cell: ITableCell = portlet.getCell(2, 0);
const handler: ITableCellEventListener = () => {
    alert('clicked');
};
cell.addEventListener(TableCellEvent.CLICK, handler);
cell.removeEventListener(TableCellEvent.CLICK, handler);
```

#### Parameters 参数
    * #####  event: TableCellEvent
单元格事件
    * #####  handler: ITableCellEventListener
单元格事件监听器
####  Returns 返回值 void


###  removeIcon 
  * removeIcon(iconIdstringIconName)void


  * 移除自定义图标 

version
    
10.5.12 

since
    
10.5.12
```
const cell: ITableCell = portlet.getCell(0, 0);
const icon: string = 'base64内容或内置图标名称';
const iconId: string = cell.addSuffixIcon(icon);
cell.removeIcon(iconId);
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
const cell: ITableCell = portlet.getCell(2, 0);
cell.resetBackgroundStyle();
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
const cell: ITableCell = portlet.getCell(2, 0);
cell.resetTextStyle();
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
const cell: ITableCell = portlet.getCell(2, 0);
const backgroundStyle: ITableCellBackgroundStyle = {
    backgroundColor: '#ee00ee',
    backgroundColorOpacity: 0.7
}
cell.setBackgroundStyle(backgroundStyle);
```

#### Parameters 参数
    * #####  style: ITableCellBackgroundStyle
单元格背景样式
####  Returns 返回值 void


###  setBorderStyle 
  * setBorderStyle(styleITableCellBorder)void


  * 设置单元格边框线样式 

version


since
    
11 (2024-07)
```
const cell: ITableCell = portlet.getCell(2, 0);
const borderStyle: ITableCellBorder = {
    // 按照顺序 依次是上、右、下、左边框的样式
    borderColor: ['rgb(2, 23, 51)', 'rgb(2, 23, 51)', 'rgb(2, 23, 51)', 'rgb(2, 23, 51)'],
    // 对应下标位置没有值则默认取第一个值
    borderColorOpacity: [1],
    borderWidth: [10, 20, 10, 30]
}
cell.setBorderStyle(borderStyle);
```

#### Parameters 参数
    * #####  style: ITableCellBorder
单元格边框线样式
####  Returns 返回值 void


###  setDisplayValue 
  * setDisplayValue(displayValuestring)void


  * 设置单元格显示值 

version
    
10.5.12 

since
    
10.5.12
```
const cell: ITableCell = portlet.getCell(2, 0);
cell.setDisplayValue('displayValue');
```

#### Parameters 参数
    * #####  displayValue: string
显示值内容
####  Returns 返回值 void


###  setTextStyle 
  * setTextStyle(styleITableCellTextStyle)void


  * 设置文字样式 

version
    
10.5.12 

since
    
10.5.12
```
const cell: ITableCell = portlet.getCell(2, 0);
const textStyle: ITableCellTextStyle = {
    fontSize: 16,
    textAlign: AlignType.CENTER,
    textBaseline: BaselineType.BOTTOM,
    fontFamily: 'Microsoft Yahei',
    fontWeight: FontWeightType.BOLDER,
    fill: '#BE0000',
    opacity: 0.8
}
cell.setTextStyle(textStyle);
```

#### Parameters 参数
    * #####  style: ITableCellTextStyle
####  Returns 返回值 void


###  setValue 
  * setValue(valuestringnumber)void


  * 设置单元格真实值 

version
    
10.5.12 

since
    
10.5.12
```
const cell: ITableCell = portlet.getCell(2, 0);
cell.setValue('value');
```

#### Parameters 参数
    * #####  value: stringnumber
####  Returns 返回值 void


