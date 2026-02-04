web电子表格行接口
### Hierarchy 层级


## Index 目录
###  Methods 方法 
  * addEventListener
  * getAttribute
  * getRowIndex
  * removeEventListener
  * setAttribute
  * setVisible


##  Methods 方法 
###  addEventListener 
  * addEventListener(typestring, listenerSheetEventListener)void


  * 添加事件监听 

version
    
10.1.0 

since
    
10.1.0
```
ele.addEventListener("click",  {
// code...
});
```

#### Parameters 参数
    * #####  type: string
表示监听事件类型的字符串，例如"click"
    * #####  listener: SheetEventListener
事件触发时的回调函数
####  Returns 返回值 void


###  getAttribute 
  * getAttribute(attributestring)string


  * 获取元素的属性 

version
    
10.1.0 

since
    
10.1.0
```
// 获取title顺序
let title = ele.getAttribute('title');
```

#### Parameters 参数
    * #####  attribute: string
####  Returns 返回值 string


###  getCell 
  * getCell(columnnumberstring)ISheetCell


  * 获取单元格 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  column: numberstring
列索引（从0开始）或者列名（例如B）
####  Returns 返回值 ISheetCell


###  getRowIndex 
  * getRowIndex()number


  * ####  Returns 返回值 number


###  getStyle 
  * getStyle(styleNamestring)string


  * 

version
    
10.1.0 

since
    
10.1.0
```
// 获取背景色
let backgroundColor = ele.getStyle('background-color');
```

#### Parameters 参数
    * #####  styleName: string
####  Returns 返回值 string


###  isVisible 
  * isVisible()boolean


  * 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 boolean


###  removeEventListener 
  * removeEventListener(typestring, listenerSheetEventListener)void


  * 删除使用addEventListener添加的事件 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  type: string
表示需要移除的事件类型，如 "click"
    * #####  listener: SheetEventListener
需要从目标事件移除的回调函数
####  Returns 返回值 void


###  setAttribute 
  * setAttribute(attributestring, valuestring)void


  * 设置元素的属性 

version
    
10.1.0 

since
    
10.1.0
```
ele.setAttribute('title', 'test');
```

#### Parameters 参数
    * #####  attribute: string
    * #####  value: string
####  Returns 返回值 void


###  setStyle 
  * setStyle(styleCssObject)void


  * 设置行样式 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  style: CssObject
####  Returns 返回值 void


###  setVisible 
  * setVisible(visibleboolean)void


  * 设置是否显示 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  visible: boolean
####  Returns 返回值 void


