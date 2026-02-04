
# 1 概述
Vastbase 数据库，也称海量数据库，是海量数据基于华为openGauss内核，融合多年对各行业应用场景的深入理解，携多年数据库开发积累，倾力打造的企业级关系型数据库。
本文介绍如何在Smartbi中连接 Vastbase 数据库，当前支持 Vastbase G100 的 MySQL模式 、PG模式 和 Oracel模式。
以下功能，Smartbi暂不支持：
1、暂不支持物化视图。
2、暂不支持存储过程。
# 2 数据连接
## 2.1 配置信息
版本信息如下：
驱动程序存放目录 | 支持数据库版本  
---|---  
cn.com.vastbase.Driver |  MySQL模式：jdbc:vastbase://<servername>:5432/<dbName>?autosave=always&prepareThreshold=0&batchMode=false&cleanupSavepoints=true PG模式：jdbc:vastbase://<servername>:5432/<dbName>?defaultRowFetchSize=10000 Oracle模式：jdbc:vastbase://<servername>:5432/<dbName> | 自定义 | VastbaseG100 V2.2Build15  
1）连接字符串主要信息说明：
<servername>：数据库的地址；
<dbName>：数据库名; 
以上信息一般向数据库管理员获取。
2）添加自定义驱动方法，详情可查看：如何向Smartbi中添加数据库驱动：
a、进入到%Smartbi%\Tomcat\bin\dynamicLibraryPath文件夹下，手动添加 Vastbase 文件夹
b、进入 Vastbase 文件夹下，添加 Vastbase 驱动（驱动包可以从数据库官网获取或向数据库管理员获取）。
c、最后在数据源连接时需要点击自定义选项，选择 Vastbase。
## 2.2 连接步骤
1）登录Smartbi，选择**数据连接 >关系数据库** ，点击** Vastbase G100 **图标进入数据库连接界面。如下图所示：
2）根据 提供的配置信息，输入数据库对应的信息。如下图所示：
说明：
a、名称是数据连接名称，用户可以自定义，不可为空。
b、用户名和密码是连接字符串中配置的数据库的连接用户名和密码，一般可以联系数据库管理员获取。
c、提供“允许加载Excel数据”的配置：
  * 允许加载Excel数据：用于设置允许加载文件数据源。详情请看：文件数据源。


## 2.3 测试连接
1）信息正确输入后，点击 ，若出现如下图的 弹出框，则表示可以成功连接上数据库。如下图所示：
2）测试连接成功后，点击右下角的按钮，选择数据源的保存位置，保存成功后，该数据连接即添加成功。如下图所示：
3）数据库连接成功后，可以参考 _快速新建透视分析_、 _快速新建即席查询_、 _快速新建电子表格_等 _快速入门_使用方式查看数据。  
