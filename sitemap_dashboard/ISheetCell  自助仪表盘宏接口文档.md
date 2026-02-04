web电子表格单元格接口
### Hierarchy 层级
  * ISheetEditableElement
    * ISheetCell


## Index 目录
###  Methods 方法 
  * addEventListener
  * appendChild
  * getAttribute
  * getColumnIndex
  * getRowIndex
  * removeEventListener
  * setAttribute


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


###  appendChild 
  * appendChild(nodeText)void
  * appendChild(nodeElement)ISheetCustomElement


  * 追加文本子节点（会对文本节点进行拷贝） 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  node: Text
文本节点对象
####  Returns 返回值 void
  * 追加元素子节点（会对元素节点进行深度拷贝，但是不会拷贝节点上的事件） 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  node: Element
元素节点对象
####  Returns 返回值 ISheetCustomElement


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


###  getColumnIndex 
  * getColumnIndex()number


  * 获取列索引 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 number


###  getHtml 
  * getHtml()string


  * 获取元素的html 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 string


###  getRowIndex 
  * getRowIndex()number


  * 获取行索引 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 number


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


###  getText 
  * getText()string


  * 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 string


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


###  setHtml 
  * setHtml(htmlstring)void


  * 设置html 

version
    
10.1.0 

since
    
10.1.0
```
ele.html({{ html }});
```

#### Parameters 参数
    * #####  html: string
html字符串
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


###  setText 
  * setText(textstring)void


  * 

version
    
10.1.0 

since
    
10.1.0
```
// 设置文本值
ele.setText({{ text }});
```

#### Parameters 参数
    * #####  text: string
####  Returns 返回值 void


