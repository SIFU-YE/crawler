
## 1 概述
本文介绍如何在Smartbi中连接RapidsDB数据库。
版本信息如下：
**Smartbi版本**  
---  
rpdsql-java-client-2.7.4.2.jar | Smartbi V10.5.8及以上  
## 2 数据连接
### 2.1 配置信息
驱动程序类 | 连接字符串 | 驱动程序存放目录 | 支持数据库版本  
---|---|---|---  
com.boraydata.jdbc.Driver |  jdbc:rpdsql://<servername>:<port>/<database>?useOldAliasMetadataBehavior=true&useUnicode=true&zeroDateTimeBehavior=convertToNull 支持jdbc:rpdsql 、 jdbc:mysql 2种协议 | 产品内置 |  RapidsDB V4.7.6  
连接字符串主要信息说明：
  * <servername>：数据库的地址；
  * <port>：数据库端口；
  * <database>：数据库名称；


以上三个信息一般可以向数据库管理员获取。
RapidsDB数据库
1.不支持全连接
2.使用mysql 5 的JDBC驱动不支持获取存储过程，不支持区分表和视图。
3.使用mysql 8 的JDBC驱动会与ETL的内置的Mysql 5的JDBC驱动冲突。
4.不支持GBK编码，连接字符串中需要把characterEncoding的参数设为UTF8或把”characterEncoding=GBK“ 删掉
5.不支持写入功能，目前只支持数据读取功能
### 2.2 连接步骤
1、登录Smartbi平台，选择**数据连接 >关系数据库** ，点击 **RapidsDB** 图标进入数据库连接界面。如下图所示：
2、根据提供的配置信息，输入数据库对应的信息。如下图所示：
说明： 
1）名称是数据连接名称，用户可以自定义，不可为空
2）用户名和密码是连接字符串中配置的数据库的连接用户名和密码，一般可以联系数据库管理员获取。
3）驱动程序类型：自定义
4) 连接字符串： 支持jdbc:rpdsql 、 jdbc:mysql 2种协议
**2.****3****测试连接**
1、信息正确输入后，点击，若出现如下图的 弹出框，则表示可以成功连接上数据库。如下图所示：
2、测试连接成功后，点击右下角的 按钮，选择数据源的保存位置，保存成功后，该数据连接即添加成功。如下图所示：
3、数据库连接成功后，可以参考、、等使用方式查看数据。  
