
## 1 概述
本文介绍如何在Smartbi中连接SelectDB数据库。
版本信息如下：
**Smartbi版本**  
---  
mysql-connector-java-5.1.48 | Smartbi V10.5.12及以上  
**SelectDB 已支持写入功能**
  * SelectDB 支持 excel 导入时，需要使用到 stream load 接口（https://doris.apache.org/zh-CN/docs/data-operate/import/import-way/stream-load-manual/），该接口为 http 接口，端口默认为 8030，目前excel导入在代码里固定写死了端口为8030。实际上用户的端口是会变更的，可以在界面上允许用户配置stream load的接口，如下图所示：


  * 回写只能支持**内catalog**[即名称为Internal的catalog]


## 2 数据连接
### 2.1 配置信息
驱动程序类 | 连接字符串 | 驱动程序存放目录 | 支持数据库版本  
---|---|---|---  
com.mysql.jdbc.Driver |  jdbc:mysql://<servername>:<port>/<database> ?useOldAliasMetadataBehavior=true &useUnicode=true&characterEncoding=GBK &zeroDateTimeBehavior=convertToNull | 产品内置 |  SelectDB 2.0  
也可以以自定义的方式，通过数据库产商官网，下载最新的驱动类（建议用和数据库厂商一致的驱动）
https://enterprise-doris-releases.oss-accelerate.aliyuncs.com/jdbc_driver/doris-connector-j-for-smartbi-0.10.jar
连接字符串主要信息说明：
  * <servername>：数据库的地址；
  * <port>：数据库端口；
  * <database>：数据库名称；


以上三个信息一般可以向数据库管理员获取。
### 2.2 连接步骤
1、登录Smartbi平台，选择**数据连接 >关系数据库** ，点击 **SelectDB** 图标进入数据库连接界面。如下图所示：
2、根据提供的配置信息，输入数据库对应的信息。如下图所示：
说明： 
1）名称是数据连接名称，用户可以自定义，不可为空
2）用户名和密码是连接字符串中配置的数据库的连接用户名和密码，一般可以联系数据库管理员获取。
3）驱动程序类型为MYSQL时会提供“大数据量兼容”和“允许加载Excel数据”两个配置项进行选择：
  * 大数据量兼容：默认勾选。针对MySQL类型数据库的一个策略，在勾选“大数据量兼容”后，会自动在“连接字符串”结尾添加“&useCursorFetch=true&defaultFetchSize=-2147483648”，用于优化内存占用，在抽取千万级别的海量数据到高速缓存库时能显著提高数据抽取性能。


1. 不支持存储过程的方式读取数据
2.SelectDB不支持直接使用limit 10 offset 5;需要前面有order by 字段才能正常执行
**2.****3****测试连接**
1、信息正确输入后，点击，若出现如下图的 弹出框，则表示可以成功连接上数据库。如下图所示：
2、测试连接成功后，点击右下角的 按钮，选择数据源的保存位置，保存成功后，该数据连接即添加成功。如下图所示：
3、数据库连接成功后，可以参考、、等使用方式查看数据。  
