
高速缓存库是Smartbi 提供的对数据查询进行缓存和提速的功能。
高速缓存库的作用是解决用户原始数据库查询慢并且不好解决的场景，可以通过定时抽取把数据缓存到缓存库，提升报表的查询性能。
## 支持范围
高速缓存库支持下面几种数据库：
  * SmartbiMpp，广州思迈特软件有限公司研发的高速缓存库
  * SmartbiMppMD，广州思迈特软件有限公司研发的高速缓存库
  * 星环Inceptor
  * TiDB
  * OceanBase(mySQL)(信创版支持)
OeacleBase(MySQL)作为高速缓存库时，
    * 需要oceanbase版本在v4.2.2以上，才支持LOAD DATA LOCAL INFILE
    * 具体参考：https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000511007
    * 同时建议oceanbase版本是在v4.3.1以上，可以使用oceanBase AP使用其列式数据库


采购高速缓存MPP模块后，可以根据实际情况选择以上几种数据库中的一种作为高速缓存库。
1、高速缓存库支持将表抽取至ClickHouse多副本集群，抽取方式与之前抽取至分布式集群相同，选定分区字段即可。
MPP库：目前只适配了，、StarRocks、SmartbiMppMD产品exe安装包自带高速缓存库、TiDB、oceanBase(mySQL)。
3、TiDB 以及 OceanBase（ MySQL），这两者作为缓存库时，均不支持将旧数据集用作缓存库。
## 配置步骤
高速缓存库在Smartbi中的配置方法如下：
（1）启动服务器，在浏览器输入Smartbi地址，进行登录；
（2）输入用户名密码，登录平台；
（3）在“系统导航栏”选择 **数据连接，** 在“资源目录区”的高速缓存库更多操作，选择 **打开** ，或双击 **高速缓存库；**
（4）进入“高速缓存库”界面
（5）据实际使用的数据库，修改相应连接属性，连接属性详情请参见 各数据库的连接详情；
（6）点击保存，保存配置。
## 各数据库的连接详情
GaussDB(DWS) |  2、在2025/10月之后的版本，数据模型引擎V2.0GaussDB(DWS)支持为缓存库(开启ENABLE_SMARTSQL_FOR_MPP_DATASOURCE=true)
  * 不支持分区。
  * 不支持预计算。

  
---|---  
Presto+Hive |  presto使用注意 1、Presto执行多表关联查询时，会把多表拆分成多个执行计划执行，这样会影响查询效率。因此Presto不适合执行的多表关联场景有：跨库多表关联拼接查询。 2、Presto的关联机制：Presto会默认执行广播式的JOIN操作，会将左表拆分到几个工作节点上，然后发送整个右表分别到已拆分好的处理左表的工作节点上，如果右表非常大就会超出工作节点的内存限制，进而出错。因此，需要把数据量大的表放在左表才能保证查询正常。 3、presto+hive作为高速缓存库时，若hive设置了用户名密码，那么presto的配置中就需使用https证书（证书需根据服务器生成），因此跨库联合数据源中的连接字符串中需要手动添加https证书的映射参数 4、当高速缓存库驱动程序类型选择了Presto+Hive，系统默认生成的别名是smartbicache.shive，包括了非法字符"."，因此在查看高速缓存库属性时，会引起报错，手动修改别名即可。  
SmartbiMpp |  1、在windows环境下使用SmartbiMppMD作为缓存库，在Linux环境下使用 SmartbiMpp作为缓存库。 **2、SmartbiMpp的最新版本是24.8.14.39。**  
星环Inceptor |  星环Inceptor服务器配置详情请参见 星环客户端配置 内容。 添加JDBC驱动详情请参见 Smartbi添加星环JDBC驱动 内容。 1、如果MPP是星环Inceptor数据库支持分区分桶(仅在V10版本支持)。如何开启？需要在系统选项/高级设置中开启：DATAMODEL_EXTRACT_OPEN_PARTITION_SETTING，如果是true，则是开启；false则是关闭。（具体的使用方法需要参考星环本身的分区分桶） 2、在2025/10月之后的版本，数据模型引擎V2.0支持星环作为缓存库(开启ENABLE_SMARTSQL_FOR_MPP_DATASOURCE=true)：
  * 不支持分区分桶。
  * 不支持分区。
  * 不支持预计算。

  
StarRocks |  StarRocks作为MPP： 1、适配了社区版2.5。2、导入数据时，应该注意：
  * 列的内容不能包含换行符，存在则会删除换行符。
  * 列的内容不能包含tab建，因为tab建是作为列分隔符。
  * 导入时的数据库表名建议是英文字母、数字，不能包含中文和特殊字符。

3、在数据模型 生成日期表，生成到高速缓存库，目前会用时比较久。  
OceanBase(Mysql) |  OeacleBase(MySQL)作为高速缓存库时，
  * 需要oceanbase版本在v4.2.2以上，才支持LOAD DATA LOCAL INFILE
  * 具体参考：https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000511007
  * 同时建议oceanbase版本是在v4.3.1以上，可以使用oceanBase AP使用其列式数据库
  * ETL还不支持Oceanbase作为缓存库。

  
