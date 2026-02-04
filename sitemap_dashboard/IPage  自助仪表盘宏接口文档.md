自助仪表盘页面接口对象
### Hierarchy 层级
## Index 目录
###  Methods 方法 
  * doPortletRendered
  * getPageToolbar
  * getPortletById
  * getPortletIds
  * getPortletsByTitle
  * openLinkByType
  * openResourceByType
  * openResourceInTab


##  Methods 方法 
###  append 
  * appendCss(selectorCssSelector, styleCssObjectstring)void


  * 增加自定义CSS样式（样式只对当前仪表盘生效） 

version
    
9.7.0 

since
    
9.7.0
#### Parameters 参数
    * #####  selector: CssSelector
css选择器
    * #####  style: CssObjectstring
css样式对象
####  Returns 返回值 void


###  doExport 
  * doExport(exportTypeExportType)void


  * 导出仪表盘 

version
    
10.5.0 

since
    
10.5.0
```
page.doExport(ExportType.EXCEL)

```

#### Parameters 参数
    * #####  exportType: ExportType
导出格式，仅支持EXCEL、PNG、PDF格式
####  Returns 返回值 void


###  doPortletRendered 
  * doPortletRendered(idstringstring[], handlerPortletRendered)void


  * 监听指定组件是否渲染完成的回调函数 

version
    
9.7.0 

since
    
9.7.0
#### Parameters 参数
    * #####  id: stringstring[]
    * #####  handler: PortletRendered
####  Returns 返回值 void


###  doRefresh 
  * doRefresh()void


  * 刷新仪表盘 

version
    
10.5.0 

since
    
10.5.0
####  Returns 返回值 void


###  getAlias 
  * getAlias()string


  * 获取自助仪表盘页面别名 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  get 
  * getId()string


  * 获取自助仪表盘id 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  getName 
  * getName()string


  * 获取自助仪表盘页面名称 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string


###  getPageToolbar 
  * getPage


  * 获取自助仪表盘工具栏接口对象 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 IPageToolbar


###  getPortletById 
  * getPortletById<T>(idstring)T


  * 根据组件id获取组件接口对象 

version
    
9.7.0 

since
    
9.7.0
```
let portlet = page.getPortletById('{portletId}')
```

#### Type parameters
#### Parameters 参数
    * #####  id: string
####  Returns 返回值 T


###  getPortlet
  * getPortletIds()string[]


  * 获取自助仪表盘下所有组件id 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 string[]


###  getPortletsByTitle 
  * getPortletsByTitle<T>(titlestring)T


  * 根据组件标题获取组件接口对象，标题相同将返回多个接口对象 

version
    
9.7.0 

since
    
9.7.0
```
let portlets = page.getPortletsByTitle('{title}')
```

#### Type parameters
#### Parameters 参数
    * #####  title: string
####  Returns 返回值 T


###  openLinkByType 
  * openLinkByType(queryOpenLinkQuery, type?: OpenTypestring)void


  * 指定URL链接及打开方式打开页面 

version
    
10.1.0 

since
    
10.1.0
```
// 传参给资源页面
let query = {
  targetInfo: {
    url: 'URL链接',
    method: 'GET',
    params: [{name: '名称', alias: '别名', value: ['真实值'], displayValue: ['显示值']}]
  }
}
// 新窗口打开
page.openLinkByType(query)
page.openLinkByType(query, 'NEW_WIN')
// 新Tab页打开
page.openLinkByType(query, 'NEW_TAB')
// 浮动框打开
page.openLinkByType(query, 'DIALOG')
// 替换源页面打开（替换当前仪表盘页面）
page.openLinkByType(query, 'COVER_SELF')
// 替换源页面打开（替换当前浏览器窗口）
query.targetInfo.coverWindow = true // 将coverWindow的状态设置为true即可
page.openResourceByType(query, 'COVER_SELF')

```

#### Parameters 参数
    * #####  query: OpenLinkQuery
    * #####  Optional type: OpenTypestring
打开方式（默认值：新窗口NEW_WIN）
####  Returns 返回值 void


###  openResourceByType 
  * openResourceByType(idstring, query?: OpenResourceQuery, type?: OpenTypestring)void


  * 指定资源id和打开方式打开页面 

version
    
10.1.0 

since
    
10.1.0
```
【不传参给资源页面】
page.openResourceByType('内部资源id')
page.openResourceByType('内部资源id', null)
page.openResourceByType('内部资源id', null, 'DIALOG')

【传参给资源页面】
let query = {
  paramInfo: [{name: '名称', alias: '别名', value: ['真实值'], displayValue: ['显示值']}]
}
// 新窗口打开
page.openResourceByType('内部资源id', query)
page.openResourceByType('内部资源id', query, 'NEW_WIN')
// 新Tab页打开
page.openResourceByType('内部资源id', query, 'NEW_TAB')
// 浮动框打开
page.openResourceByType('内部资源id', query, 'DIALOG')
// 替换源页面打开（替换当前仪表盘页面）
page.openResourceByType('内部资源id', query, 'COVER_SELF')
// 替换源页面打开（替换当前浏览器窗口）
query.targetInfo = {
  coverWindow: true // 将coverWindow的状态设置为true即可
}
page.openResourceByType('内部资源id', query, 'COVER_SELF')

```

#### Parameters 参数
    * #####  id: string
目标资源id
    * #####  Optional query: OpenResourceQuery
    * #####  Optional type: OpenTypestring
打开方式（默认值：新窗口NEW_WIN）
####  Returns 返回值 void


###  openResourceInTab 
  * openResourceInTab(idstring, paramInfoArraystringobject)void


  * 新tab页打开 

version
    
9.7.0 

since
    
9.7.0
```
// V模块资源
paramInfo = [{name: '名称', alias: '别名', value: '真实值', displayValue: '显示值'}]
// 自助仪表盘
paramInfo = {'名称': { values: ['真实值'] }, '名称2': { values: ['真实值'] }}
```

#### Parameters 参数
    * #####  id: string
目标资源id
    * #####  paramInfo: Arraystringobject
####  Returns 返回值 void


###  remove 
  * removeCss()void


  * 移除自定义CSS 

version
    
9.7.0 

since
    
9.7.0
####  Returns 返回值 void


