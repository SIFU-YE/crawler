
# 1 概述
Apache Doris 是一个基于 MPP 架构的高性能、实时的分析型数据库，以极速易用的特点被人们所熟知，仅需亚秒级响应时间即可返回海量数据下的查询结果，不仅可以支持高并发的点查询场景，也能支持高吞吐的复杂分析场景。基于此，Apache Doris 能够较好的满足报表分析、即时查询、统一数仓构建、数据湖联邦查询加速等使用场景，用户可以在此之上构建用户行为分析、AB 实验平台、日志检索分析、用户画像分析、订单分析等应用。
**Doris已支持写入功能**
  * Doris支持 excel 导入时，需要使用到 stream load 接口（https://doris.apache.org/zh-CN/docs/data-operate/import/import-way/stream-load-manual/），该接口为 http 接口，端口默认为 8030，实际上用户的端口是会变更的，可以在界面上允许用户配置stream load的接口，如下图所示：


  * 回写只能支持**内catalog**[即名称为Internal的catalog]


# 2 数据连接
## 2.1 配置信息
版本信息如下：
驱动程序存放目录 | 支持数据库版本  
---|---  
org.mariadb.jdbc.Driver | jdbc:doris://<servername>:<port>/<database>?useSSL=false | Doris 2.1.5  
驱动类：请到数据库厂商 官网下载 https://enterprise-doris-releases.oss-accelerate.aliyuncs.com/jdbc_driver/doris-connector-j-for-smartbi-0.10.jar
1）连接字符串主要信息说明：
<servername>：数据库地址；
<port>：数据库端口；
<database>：数据库名称; 
以上信息一般向数据库管理员获取。
2）添加自定义驱动方法，详情可查看：如何向Smartbi中添加数据库驱动：
a、进入到%Smartbi%\Tomcat\bin\dynamicLibraryPath文件夹下，手动添加 Doris 文件夹
b、进入 Doris 
c、最后在数据源连接时需要点击自定义选项，选择 Doris。
## 2.2 连接步骤
1）登录Smartbi，选择**数据连接 >关系数据库** ，点击**Doris** 图标进入数据库连接界面。如下图所示：
2）根据 提供的配置信息，输入数据库对应的信息。如下图所示：
说明：
a、名称是数据连接名称，用户可以自定义，不可为空。
b、用户名和密码是连接字符串中配置的数据库的连接用户名和密码，一般可以联系数据库管理员获取。
## 2.3 测试连接
1）信息正确输入后，点击 ，若出现如下图的 弹出框，则表示可以成功连接上数据库
2）测试连接成功后，点击右下角的按钮，选择数据源的保存位置，保存成功后，该数据连接即添加成功。如下图所示：
3）数据库连接成功后，可以参考 _快速新建透视分析_、 _快速新建即席查询_、 _快速新建电子表格_等 _快速入门_使用方式查看数据。  
