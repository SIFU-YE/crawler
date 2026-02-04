
## **1 概述**
本文介绍如何在smartbi中连接StarRocks数据库。
版本信息如下：
**Smartbi版本**  
---  
_JDBC_mysql-connector-java-5.1.48.jar(内置,也支持自定义) | Smartbi V10.5.8及以上  
、StarRocks支持多Catalog。
2、StarRocks支持作为Smartbi 的高速缓存库。
StarRocks已支持写入功能。
StarRocks支持 excel 导入时，需要使用到 stream load 接口（具体查看官方说明），该接口为 http 接口，端口默认为 8030，目前excel导入在代码里固定写死了端口为8030。
实际上用户的端口是会变更的，可以在界面上允许用户配置stream load的接口，如下图所示：
## **2 数据连接**
### 2.1 配置信息
驱动程序类 | 连接字符串 | 驱动程序存放目录 | 支持数据库版本  
---|---|---|---  
com.mysql.jdbc.Driver |  jdbc:mysql://<servername>:<port>/<database> ?useOldAliasMetadataBehavior=true &useUnicode=true&zeroDateTimeBehavior=convertToNull | 产品内置 | StarRocks 社区版2.2.2  
连接字符串主要信息说明：
  * <servername>：数据库的地址；
  * <port>：数据库端口；
  * <database>：数据库名称；


以上三个信息一般可以向数据库管理员获取。
1.starRocks连接字符串不支持characterEncoding=GBK，只支持utf-8
2. mysql的JDBC产品无法支持starRocks的物化视图(通过“CREATE MATERIALIZED VIEW 物化视图名称 ”语句创建的物化视图）
StarRocks支持导入数据（excel导入、回写、excel导入模板配置），但是在导入时，需要注意几点：
  * 列的内容不能包含换行符，存在则会删除换行符。
  * 列的内容不能包含tab建，因为tab建是作为列分隔符。
  * 导入时的数据库表名建议是英文字母、数字，不能包含中文和特殊字符。
  * 导入的列为文本型时，列的内容要求在 255 个字节内，超过时会导不进去。


### 2.2 连接步骤
1、登录Smartbi企业报表分析平台，选择**数据连接 >关系数据库** ，点击 **StarRocks** 图标进入数据库连接界面。如下图所示：
2、在连接数据库之前，请收集以下信息
  * 数据库的版本（版本要求：StarRocks ≥ 2.2）；
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 数据库的用户名和密码；
  * 需要连接的数据库方式。


说明：
1）名称是数据连接名称，用户可以自定义，不可为空
2）用户名和密码是连接字符串中配置的数据库的连接用户名和密码，一般可以联系数据库管理员获取。
3）驱动程序类型为StarRocks时会提供“大数据量兼容”、“允许加载Excel数据”的配置：
  * 大数据量兼容：默认勾选。针对MySQL类型数据库的一个策略，在勾选“大数据量兼容”后，会自动在“连接字符串”结尾添加“&useCursorFetch=true&defaultFetchSize=-2147483648”，用于优化内存占用，在抽取千万级别的海量数据到高速缓存库时能显著提高数据抽取性能。
  * 允许加载Excel数据：用于设置允许加载文件数据源。


###  **2.****3****测试连接**
1、信息正确输入后，点击，若出现如下图的 弹出框，则表示可以成功连接上数据库。如下图所示：
2、测试连接成功后，点击右下角的 按钮，选择数据源的保存位置，保存成功后，该数据连接即添加成功。如下图所示：
**2.4 、数据库管理(加载表)**
1、选择建好的StarRocks，右键菜单，选择”“
starRocks可以选择catalog，如下图，
3、数据库连接成功后，可以参考、、等使用方式查看数据。

  
