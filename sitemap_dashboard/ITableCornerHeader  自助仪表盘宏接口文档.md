交叉表角头对象
### Hierarchy 层级
  * ITableCornerHeader


## Index 目录
###  Methods 方法 
  * addEventListener
  * addPrefixIcon
  * addSuffixIcon
  * getBackgroundStyle
  * getColumnIndex
  * getDisplayValue
  * getTextStyle
  * removeEventListener
  * resetBackgroundStyle
  * resetTextStyle
  * setBackgroundStyle
  * setDisplayValue
  * setTextStyle


##  Methods 方法 
###  addEventListener 
  * addEventListener(eventTableCellEvent, handlerITableCellEventListener)void


  * 添加事件监听器 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
const handler: ITableCellEventListener = () => {
  alert('clicked');
}
cornerHeader.addEventListener(TableCellEvent.CLICK, handler);
```

#### Parameters 参数
    * #####  event: TableCellEvent
    * #####  handler: ITableCellEventListener
角头事件监听器
####  Returns 返回值 void


###  addPrefixIcon 
  * addPrefixIcon(imagestringIconName, options?: ICustomIconOptions)string


  * 在文字前面添加自定义图标 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
const icon: string = 'base64内容或内置图标名称'
cornerHeader.addPrefixIcon(icon);
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
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
const icon: string = 'base64内容或内置图标名称'
cornerHeader.addSuffixIcon(icon);
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
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
const backgroundStyle: ITableCellBackgroundStyle = cornerHeader.getBackgroundStyle();
```

####  Returns 返回值 ITableCellBackgroundStyle
单元格背景样式


###  getColumnIndex 
  * getColumnIndex()number


  * 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
const columnIndex: number = cornerHeader.getColumnIndex();
```

####  Returns 返回值 number
列号，从0开始


###  getDisplayValue 
  * getDisplayValue()string


  * 获取角头内容 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
const label: string = cornerHeader.getDisplayValue();
```

####  Returns 返回值 string
角头内容


###  getTextStyle 
  * getText


  * 获取文字样式 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
const textStyle: ITableCellTextStyle = cornerHeader.getTextStyle();
```

####  Returns 返回值 ITableCellTextStyle
文字样式


###  removeEventListener 
  * removeEventListener(eventTableCellEvent, handlerITableCellEventListener)void


  * 移除事件监听器 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
const handler: TableCellEvent = () => {
  alert('clicked');
}
cornerHeader.addEventListener(TableCellEvent.CLICK, handler);
cornerHeader.removeEventListener(TableCellEvent.CLICK, handler);
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
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
const icon: string = 'base64内容或内置图标名称'
const iconId: string = cornerHeader.addSuffixIcon(icon);
cornerHeader.removeIcon(iconId);
```

#### Parameters 参数
    * #####  iconId: stringIconName
图标id或内置图标名称
####  Returns 返回值 void


###  resetBackgroundStyle 
  * resetBackgroundStyle()void


  * 重置自定义背景样式 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
cornerHeader.resetBackgroundStyle();
```

####  Returns 返回值 void


###  resetTextStyle 
  * resetTextStyle()void


  * 重置自定义文字样式 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
cornerHeader.resetTextStyle();
```

####  Returns 返回值 void


###  setBackgroundStyle 
  * setBackgroundStyle(styleITableCellBackgroundStyle)void


  * 设置单元格背景样式 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
const backgroundStyle: ITableCellBackgroundStyle = {
    backgroundColor: '#999',
    backgroundColorOpacity: 0.8
}
cornerHeader.setBackgroundStyle(backgroundStyle);
```

#### Parameters 参数
    * #####  style: ITableCellBackgroundStyle
单元格背景样式
####  Returns 返回值 void


###  setDisplayValue 
  * setDisplayValue(labelstring)void


  * 设置角头内容 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
cornerHeader.setDisplayValue('TEST_LABEL');
```

#### Parameters 参数
    * #####  label: string
####  Returns 返回值 void


###  setTextStyle 
  * setTextStyle(styleITableCellTextStyle)void


  * 设置文字样式 

version
    
10.5.15 

since
    
10.5.15
```
const cornerHeader: ITableCornerHeader = portlet.getCornerHeader(0);
const textStyle: ITableCellTextStyle = {
    fontSize: 16,
    textAlign: AlignType.CENTER,
    textBaseline: BaselineType.MIDDLE,
    fontFamily: 'Microsoft Yahei',
    fontWeight: FontWeightType.BOLDER,
    fill: '#00FE00',
    opacity: 0.8
}
cornerHeader.setTextStyle(textStyle);
```

#### Parameters 参数
    * #####  style: ITableCellTextStyle
####  Returns 返回值 void


