WEB电子表格服务端组件接口对象
### Hierarchy 层级
  * IPortletServer
    * ITableSheetPortletServer


## Index 目录
###  Methods 方法 
  * getSheetByName
  * getWorkbook
  * printExpandedPositions
  * setCacheable
  * setCustomProperty


##  Methods 方法 
###  get 
  * getId()string


  * 获取组件id 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 string


###  getSheetByName 
  * getSheetByName(sheetNamestring)ISheetServer


  * 根据sheet页名称来获取sheet页 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  sheetName: string
sheet页名称
####  Returns 返回值 ISheetServer


###  getSheets 
  * get 


  * 获取所有的sheet页 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 ISheetServer[]


###  getTitle 
  * getTitle()string


  * 获取组件标题 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 string


###  getType 
  * getType()string


  * 获取组件类型 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 string


###  getWorkbook 
  * get 


  * 获取Workbook对象
详细API参考aspose官方文档：https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 IWorkbook


###  printExpandedPositions 
  * printExpandedPositions()void


  * 将扩展后的单元格位置信息输出到客户端
可以在客户端调用`portlet.getExpandedPositions`方法来获取单元格的扩展位置信息 

version
    
10.1.0 

since
    
10.1.0
####  Returns 返回值 void


###  setCacheable 
  * setCacheable(cacheableboolean)void


  * WEB电子表格是否启用缓存 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  cacheable: boolean
是否启用缓存
####  Returns 返回值 void


###  setCustomProperty 
  * setCustomProperty(keystring, valueobject)void


  * 设置自定义的属性信息
可以在客户端调用`portlet.getCustomProperty`方法来获取自定义的属性信息 

version
    
10.1.0 

since
    
10.1.0
#### Parameters 参数
    * #####  key: string
    * #####  value: object
####  Returns 返回值 void


