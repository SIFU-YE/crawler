
## 1 概述
如果您使用的是阿里云OceanBase数据库，在对接Smartbi进行数据分析时，可以添加OceanBase云数据源，阿里云OceanBase的详情请参见云数据库OceanBase。
OceanBase是一款金融级的分布式关系数据库，具备高性能、高可用、强一致、可扩展和兼容性高等典型优势，适用于对性能、成本和扩展性要求高的金融场景。
本文介绍如何在Smartbi中连接OceanBase数据库。
OeacleBase MySQL 模式作为高速缓存库时：
  * 需要oceanbase版本在v4.2.2以上，才支持LOAD DATA LOCAL INFILE
  * 具体参考：https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000511007
  * 同时建议oceanbase版本是在v4.3.1以上，可以使用oceanBase AP使用其列式数据库
  * ETL还不支持Oceanbase作为缓存库。


## 2 数据连接
### 2.1 配置信息
模式 | 驱动程序类 | 连接字符串 | 驱动程序存放目录 | 支持数据库版本  
---|---|---|---|---  
MySQL 模式 | com.alipay.oceanbase.jdbc.Driver |  jdbc:oceanbase://<servername>:<port>/<database>?useOldAliasMetadataBehavior=true&useUnicode=true &zeroDateTimeBehavior=convertToNull&useCursorFetch=true&defaultFetchSize=10000 | 自定义 |  OceanBase V2.2.7 OceanBase V3 OceanBase V4  
Oracle 模式 | com.oceanbase.jdbc.Driver | jdbc:oceanbase:oracle://<servername>:<port>/<database> | 自定义  
连接字符串主要信息说明：
  * <servername>：数据库地址；
  * <port>：数据库端口；
  * <database>：数据库名称；


以上三个信息一般可以向数据库管理员获取。
### 2.2 连接步骤
1、登录Smartbi平台，选择**数据连接 >关系数据库** ，点击 **OceanBase** 图标进入数据库连接界面。如下图所示：
2、根据提供的配置信息，输入数据库对应的信息。
连接“Mysql 模式”
连接“Oracle模式”
说明： 
1）名称是数据连接名称，用户可以自定义，不可为空
2）用户名和密码是连接字符串中配置的数据库的连接用户名和密码，一般可以联系数据库管理员获取
MySQL模式、Oracle模式
1. 都是自定义驱动
2. 只支持读取数据，不支持写入
3. OceanBase 2.2.7是不支持返回游标的存储过程的，3.2.x 版本中是可以的
**2.****3****测试连接**
1、信息正确输入后，点击，若出现如下图的 弹出框，则表示可以成功连接上数据库。如下图所示：
2、测试连接成功后，点击右下角的 按钮，选择数据源的保存位置，保存成功后，该数据连接即添加成功。如下图所示：
3、数据库连接成功后，可以参考、、等使用方式查看数据。  
