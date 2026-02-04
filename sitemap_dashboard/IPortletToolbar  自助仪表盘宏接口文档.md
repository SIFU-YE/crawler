组件工具栏接口 

version
    
10.5.0 

since
    
10.5.0
### Hierarchy 层级
  * IPortletToolbar


## Index 目录
###  Methods 方法 
  * removeButton


##  Methods 方法 
###  addButton 
  * addButton(buttonIPortletToolbarButton, handler(eventMouseEvent)void, index?: number)void


  * 添加工具栏按钮 

version
    
10.5.0 

since
    
10.5.0
```
toolbar.addButton({
  id: 'DEMO',
  icon: 'sx-icon-ai',
  tip: 'demo button'
}, (event) => {
  alert('click DEMO button');
}, 0);

```

#### Parameters 参数
    * #####  button: IPortletToolbarButton
    * #####  handler: (eventMouseEvent)void
点击按钮的回调函数
      *         * (eventMouseEvent)void
        * #### Parameters 参数
          * #####  event: MouseEvent
####  Returns 返回值 void
    * #####  Optional index: number
按钮序号，不填默认加到末尾（序号从0开始）
####  Returns 返回值 void


###  getButton 
  * getButton(idPortletToolbarIdEnumstring)IPortletToolbarButton


  * 根据id获取工具栏按钮 

version
    
10.5.0 

since
    
10.5.0
```
let aiBtn: IPortletToolbarButton = toolbar.getButton(PortletToolbarIdEnum.AI);

```

#### Parameters 参数
    * #####  id: PortletToolbarIdEnumstring
####  Returns 返回值 IPortletToolbarButton


###  getButtons 
  * getButtons()ArrayIPortletToolbarButton


  * 获取所有工具栏按钮 

version
    
10.5.0 

since
    
10.5.0
```
let buttons: Array<IPortletToolbarButton> = toolbar.getButtons();

```

####  Returns 返回值 ArrayIPortletToolbarButton


###  isHidden 
  * isHidden()boolean


  * 获取工具栏隐藏状态，为true则隐藏，否则显示 

version
    
10.5.0 

since
    
10.5.0
```
let isHidden: boolean = toolbar.isHidden();

```

####  Returns 返回值 boolean
boolean 隐藏状态


###  removeButton 
  * removeButton(idPortletToolbarIdEnumstring)void


  * 移除工具栏按钮 

version
    
10.5.0 

since
    
10.5.0
```
toolbar.removeButton(PortletToolbarIdEnum.MOVE);

```

#### Parameters 参数
    * #####  id: PortletToolbarIdEnumstring
####  Returns 返回值 void


###  setHidden 
  * setHidden(isHiddenboolean)void


  * 设置工具栏隐藏状态，为true则隐藏，否则显示 

version
    
10.5.0 

since
    
10.5.0
```
toolbar.setHidden(true);

```

#### Parameters 参数
    * #####  isHidden: boolean
####  Returns 返回值 void


