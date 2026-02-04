
  *   *   * 

Smartbi 提供三种形式的二次开发接口，以便实现更高要求的系统集成开发：
  1. 服务器端SDK：提供JAVA API 供外部系统调用实现集成要求。
  2. 浏览器端SDK：提供JavaScript API 供外部系统调用，满足非J2EE平台的客户环境（如.Net平台）实现与Smartbi 的集成要求。
  3. WebService服务接口：通过 WebService 调用Smartbi API，满足非J2EE平台的客户环境（如.Net平台）实现与Smartbi 的集成要求。


### 说明
服务器端 SDK 通过JAVA API 提供以下服务接口：
AnalysisReportService | 提供相关操作功能。  
---|---  
BusinessViewService |  提供相关操作功能。  
CatalogService | 提供资源目录树的访问功能等。  
SystemConfigService | 提供系统设置相关操作功能。  
OperationLogService | 提供操作日志相关操作功能。  
UserManagerService | 提供用户相关功能，主要包括：读取/维护用户、组、角色等信息、为用户和组分配角色等。  
ManageReportService | 提供复杂报表相关操作功能（Deprecated）。  
### **实现步骤**
  1. 假设Smartbi 服务器已经部署到应用服务器中，访问地址为：http://localhost:18080/smartbi。
  2. 打开服务器部署文件smartbi.war，解压后将smartbi.war\WEB-INF\lib\目录下的 **smartbi-DAO.jar、smartbi-Framework.jar、smartbi-FreeQuery.jar、smartbi-UserManager.jar（V10.5.15及以上的版本由于打包方式的调整，jar包需要修改为Smartbi-DAO.Implement.jar、Smartbi-DAO.Interface.jar、Smartbi-Framework.Implement.jar、Smartbi-Framework.Interface.jar、Smartbi-FreeQuery.Implement.jar、Smartbi-FreeQuery.Interface.jar、Smartbi-UserManager.Implement.jar、Smartbi-UserManager.Interface.jar）以及**接口依赖Jar包清单内的jar包加入到您的 Java 项目的 classpath 中去。


```
String Smartbi_URL = "http://localhost:18080/smartbi";
ClientConnector conn = new ClientConnector(Smartbi_URL);
try {
    // 第一次调用必须建立一个连接，后续调用则不必再建连接
    boolean ret = conn.open("admin", "manager");
    if (ret) {
        // 资源目录树
        CatalogService catalogService = new CatalogService(conn);
        String elementId = "I2c9490741d4647ab011d4b92363f2061";
        String elementType = "SIMPLE_REPORT";
        boolean result = catalogService.isCatalogElementAccessible(elementId, elementType);
        System.out.println(result);
 
        // 灵活报表
        SimpleReportService simpleReportService = new SimpleReportService(conn);
        String reportId = "I2c9490741d2370a8011d2df3b1fd1fa0";
        Report report = simpleReportService.openReport(reportId);
        System.out.println(report.getCurrentReportName());
 
        // 用户管理
        UserManagerService userManagerService = new UserManagerService(conn);
        String departmentId = "DEPARTMENT";
        IDepartment department = userManagerService.getDepartmentById(departmentId);
        System.out.println(department.getName());
    }
} catch(RemoteException e) {
    e.printStackTrace();
} finally {
    // 关闭应用连接器
    conn.close();
}
```

### **注意事项**
具体的方法以及帮助请参考 Java API文档。
浏览器端SDK 通过JavaScript API 提供多个客户端组件供外部调用，满足非J2EE平台的客户环境（如.Net平台）实现与Smartbi 系统的集成要求。
### **实现步骤**
  1. 假设Smartbi 服务器已经部署到应用服务器中，访问地址为：http://localhost:18080/smartbi/vision/。
  2. 打开服务器部署文件smartbi.war，解压后将\smartbi.war\vision\js\freequery\lang\目录下的JSLoader.js 文件复制到您的web路径下。


### **调用示例**
```
<html>
<head>
	<title>javascript api 调用示例</title>
	<script type="text/javascript" src="../JSLoader.js"></script>
</head>
<body>
	<script type="text/javascript">
    var BOF_UI_DEBUG = false;
    var config = new Object();
    config.baseURL = "http://localhost:18080/smartbi/vision/"; //smartbi服务器的URL地址
 
    // 创建全局唯一的JS装载器 
    var jsloader = new JSLoader(config);
 
    // 创建应用程序对象 
    var userService = jsloader.imports("bof.usermanager.UserService");
 
    // 通过userService.getInstance()
    // 可以调用所有的UserManagerModule方法
    var result = userService.getInstance().login("admin", "manager");
    if (result) {
        alert("OK");
    }
	</script>
</body>
</html>
```

## **WebService服务接口**
Smartbi 对外提供WebService 接口， 满足非J2EE平台的客户环境（如.Net平台） 实现与Smartbi 的集成要求。
① wsdl地址格式：
http://**biserver** :**port** /smartbi/vision/services/**【接口名称】**?wsdl
  * **biserver** ：服务器ip地址
  * **port** ：服务器端口


示例： _http://**localhost** :**18080** /smartbi/vision/services/AnalysisReportService?wsdl_
② Smartbi提供以下WebService服务接口：  
AnalysisReportService | 提供多维分析相关操作功能。 | http://**biserver** :**port** /smartbi/vision/services/**AnalysisReportService**?wsdl  
BusinessViewService |  提供数据集相关操作功能。 | http://**biserver** :**port** /smartbi/vision/services/**BusinessViewService**?wsdl  
CatalogService | 提供资源目录树的访问功能等。 | http://**biserver** :**port** /smartbi/vision/services/**CatalogService**?wsdl  
UserManagerService | 提供用户、用户组、角色信息维护的相关接口。 | http://**biserver** :**port** /smartbi/vision/services/**UserManagerService**?wsdl  
ManageReportService |  提供复杂报表相关操作功能（**Deprecated** ）。 | http://**biserver** :**port** /smartbi/vision/services/**ManageReportService**?wsdl  
### 
具体的方法以及帮助请参考  
