自助仪表盘工具栏接口对象(浏览状态下)
### Hierarchy 层级
  * IPageToolbar


## Index 目录
###  Methods 方法 
  * getButtons
  * removeButton


##  Methods 方法 
###  addButton 
  * addButton(buttonPageToolBarButton, index?: number)void


  * 添加工具栏按钮 

version
    
9.7.0 

since
    
9.7.0
    * **示例**```
let pageMenu = page.getPageToolbar()
pageMenu.addButton({
 icon: 'sx-icon-liked icon-16',
 tooltip: '弹窗',
 color: '#0f0',
 handler: function ({
   alert('点击了按钮')
 }
}, 1)
```

#### Parameters 参数
    * #####  button: PageToolBarButton
工具栏按钮
    * #####  Optional index: number
按钮序号，不填默认加到末尾（序号从0开始）
####  Returns 返回值 void


###  fold 
  * fold()void


  * 收起工具栏 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 void


###  getButtons 
  * getButtons()ArrayPageToolBarButton


  * 获取所有工具栏按钮 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 ArrayPageToolBarButton


###  isHidden 
  * isHidden()boolean


  * 获取工具栏隐藏状态 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 boolean


###  removeButton 
  * removeButton(indexnumber)void


  * 移除工具栏按钮 

version
    
9.7.0 

since
    
9.7.0
#### Parameters 参数
    * #####  index: number
按钮序号（序号从0开始）
####  Returns 返回值 void


###  setHidden 
  * setHidden(isHiddenboolean)void


  * 设置工具栏隐藏状态 

version
    
9.7.0 

since
    
9.7.0
#### Parameters 参数
    * #####  isHidden: boolean
####  Returns 返回值 void


###  unfold 
  * unfold()void


  * 展开工具栏 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 void


