
  *     * 

## **推荐配置**
Smartbi及其组件部署的**硬件推荐配置** 如下：
注意事项
根据内部环境验证测试结果得出以下推荐部署方案。测试场景是基于100万行的底表数据，在不同部署环境下，打开普通报表，并发查询的最大响应时间内，最大并发数做为参考。
若项目实际环境并发访问的报表相对较为复杂，数据量更大，则支持的并发数也会相应的减少，需根据项目实际使用场景进行调整，必要时可对实际环境的常用高并发资源进行压测。
由于各个服务组件存在资源抢占问题，生产环境，不建议将所有节点都部署在同一个服务器。
在有缓存的情况下，浏览报表并不消耗内存资源，所以相对于两台机器，三台机器增加了各组件内存，查询并发没有变化。
导出和抽取是不走缓存，在增加内存后，并发会有所增加。
注册用户数 | 在线用户数 | 并发用户数 | 推荐配置 | 部署方案 | 底表数据量 | 浏览报表最大响应时间 | 导出并发数 | 抽取并发数  
---|---|---|---|---|---|---|---|---  
4000 | 800 | 160 |  服务器数量：2台每台服务器配置： CPU：16核 2.90 GHZ 以上 内存：64G 硬盘：500G | 服务器1：smartbi（32g内存）+导出引擎（16g内存）+知识库服务器2：olap（16g内存）+MPP（16g内存）+ETL（16g内存） | 100W | 3s | 20 | 5  
7500 | 1500 | 300 |  服务器数量：2台 每台服务器配置： CPU：16核 2.90 GHZ 以上 内存：64G 硬盘：500G | 服务器1：smartbi（32g内存）+导出引擎（16g内存）+知识库服务器2：olap（16g内存）+MPP（16g内存）+ETL（16g内存） | 100W | 6s | 20 | 5  
4000 | 800 | 160 |  服务器数量：3台每台服务器配置： CPU：16核 2.90 GHZ 以上 内存：64G 硬盘：500G | 服务器1：smartbi（48g内存）+知识库服务器2：olap（32g内存）+导出引擎（16g内存）服务器3：MPP（32g内存）、ETL（16g内存） | 100W | 3s | 40 | 15  
7500 | 1500 | 300 |  服务器数量：3台每台服务器配置： CPU：16核 2.90 GHZ 以上 内存：64G 硬盘：500G | 服务器1：smartbi（48g内存）+知识库服务器2：olap（32g内存）+导出引擎（16g内存）服务器3：MPP（32g内存）、ETL（16g内存） | 100W | 6s | 40 | 15  
6500 | 1300 | 260 |  服务器数量：5台 每台服务器配置： CPU：16核 2.90 GHZ 以上 内存：64G 硬盘：500G | 服务器1：smartbi（48g内存）+知识库服务器2：smartbi(48g内存)+ngnix服务器3：MPP(48g内存) 服务器4：olap(48g内存) 服务器5：导出引擎（32g内存）+ETL(16g内存)  | 100W | 3s | 40 | 35  
11000 | 2200 | 440 |  服务器数量：5台每台服务器配置： CPU：16核 2.90 GHZ 以上 内存：64G 硬盘：500G | 服务器1：smartbi（48g内存）+知识库服务器2：smartbi(48g内存)+ngnix服务器3：MPP(48g内存) 服务器4：olap(48g内存) 服务器5：导出引擎（32g内存）+ETL(16g内存)  | 100W | 6s | 40 | 35  
服务 | 数据量 | 并发 | 配置推荐 | 服务器数量推荐  
---|---|---|---|---  
Smartbi数据挖掘/SmartbiETL | 500MB~5GB | 15~30 | 16核，64G内存，1TB硬盘 | 1~3台  
5GB~10GB | 15~30 | 16核，64G内存，1TB硬盘 | 3~5台  
10GB~50GB | 15~30 | 16核，64G内存，1TB硬盘 | 5~10台  
500MB~5GB | 30~60 | 16核，64G内存，1TB硬盘 | 3~5台  
5GB~10GB | 30~60 | 16核，64G内存，1TB硬盘 | 5~10台  
10GB~50GB | 30~60 | 16核，64G内存，1TB硬盘 | 15~20台  
这个只是根据测试结果估算，不绝对准确，同时并发数也可以调大，调大后会有资源争用，跑得慢一些，不会有其它影响
根据不同场景可以灵活准备部署方案和硬件配置，可以参考文档：Smartbi部署方案参考
如果是个人试用体验，建议使用4核16G以上服务器进行安装部署。
## **Smartbi相关要求**
Smartbi部署、使用、访问的相关要求如下：
### 应用服务器要求
Tomcat | tomcat8.5、tomcat9、tomcat10  
---|---  
IBM WebSphere | WebSphere 9.0  
Oracle WebLogic | WebLogic 12.2.1，14.1.1.0  
东方通 TongWeb | TongWeb 7.0和8.0版本  
中创中间件 | InforSuiteAS_StE_V10.0.5  
宝兰德中间件 | BES-9.5  
金蝶中间件 | Apusic V10  
普元中间件 | 普元中间件 V6.5  
1、Tomcat10版本的smartbi.war包和tomcat8，tomcat9的不一样，需要在申请安装介质时说明项目环境的tomcat版本信息。
2、不支持Tomcat 11版本
### Java环境版本要求
Oracle JDK | Oracle JDK 8、Oracle JDK 11、Oracle JDK17  
---|---  
OpenJDK | OpenJDK 11、OpenJDK 17、OpenJDK 18  
bishengJDK | bishengjdk-8  
jdk版本要求是针对smartbi的部署的说明。
其他组件对jdk版本要求，请分别查看各个组件的部署文档说明
### 知识库要求：
在产品中配置知识库可参考：⬝ TiDB做为知识库
数据库类型 | 数据库字符集（参考）  
---|---  
UTF-8  
GaussDB |  GaussDB，GaussDB(DWS）（不推荐做知识库，适合做业务库） 1）GaussDB 100，GaussDB 200，目前华为官网已没有该产品，之前已经使用的客户可继续使用，24年12月初发布及之后的版本不再支持。 2）GaussDB(DWS）作为知识库存在性能问题，属于数据库本身的问题，技术上无法解决。 | UTF-8 | 集中式部署  
Gbase 8S 、Gbase 8S V8.4、Gbase8S V8.8 3.0+ | GBK  
GoldenDB | V6.1.03.05 | utf8m64  
GreatDB | V8.0.32-27 | UTF-8  
Kingbase | V7.1.1、V8、V9 | GBK | V9版本可以使用kingbaseV8的数据源连接，但是自定义驱动要使用kingbase V9版本的驱动。  
MariaDB | V10.3.24  | UTF-8  
MogDB | V3.0.6（LTS） | UTF-8  
GBK  
OceanBase |  V2.2.7（MySQL模式）、V3（MySQL模式）、V4（MySQL模式） V3版本使用空库升级，必须执行以下SQL延长事务自动回滚的时间 SET GLOBAL max_allowed_packet=67108864;SET GLOBAL ob_query_timeout=3600000000;SET GLOBAL ob_trx_timeout=3600000000;SET GLOBAL ob_trx_idle_timeout = 3600000000;ALTER SYSTEM SET open_cursors=1500; | utf8mb4  
OpenGauss | OpenGauss_2.1.0 极简版 | UTF-8  
Oracle | 11G，19C | GBK  
PanWeiDB | V1.0 | UTF-8  
PostgreSQL | UTF-8  
ShenTong | V7.0.8 | UTF8  
TDSQL（MySQL版）5.7.30 （需要单独部署扩展包实现） | GBK  
TiDB | V5.1.2 | UTF-8 | 分布式  
Vastbase | G100（MySQL模式）、G100（PG模式） | UTF-8  
XuguDB | V12.6.9 | UTF-8  
达梦 | V6、V7、V8 | UTF-8  
云数据库 RDS MySQL | V5.7（使用MySQL的连接方式即可） | GBK  
### 数据连接要求
详细的数据库连接情况可查看：数据连接支持情况-汇总。
国产数据库：Aliyun AnalyticDB、Aliyun MaxCompute、Doris、GaussDB(DWS)、GaussDB、Gbase 8A、Gbase 8S V8.4、 Gbase 8S V8.8、GoldenDBHuawei FusionInsight HD、Obase、OceanBase、PanWeiDB、RapidsDB 、SelectDB 、ShenTong 、StarRocks、Smartbi JDBC for Excel、TiDB、YMatrix、达梦、星环 Greenplum、Hadoop_Hive、HANA、IMPALA、Informix、MariaDB、MonetDB、MS SQL Server、MySQL、Smartbi Jdbc4Olap、Spark SQL、Sybase、Teradata、Vertica  
---  
Essbase 7、Essbase 9、IBM Cubing Services、Jedox Palo、Kyligence、Mondrian、SAP、SQL Server2000、SQL Server2005  
数据挖掘模块仅支持部分数据源类型，详情请参考 数据连接支持情况-汇总。
浏览用户 |  无需安装插件，可在Web浏览器上查看、刷新、导出电子表格/分析报告。 注意：浏览器版本要求，可以参考 章节  
---|---  
**Microsoft .Net Framework**  
Windows 7 windows 10 Windows Server 2008 Windows Server 2012 |  Microsoft Office 2013专业版 Microsoft Office 2016专业版 Microsoft Office 365 桌面版 Office2019 Home Student（注：V9.3及之后版本支持） WPS Office 2016个人版 WPS Office 2019个人版 | Microsoft.Net Framework 4.5 Full  
1、在进行电子表格报表/分析报告开发时，最好使用64位的office软件。
2、WPS Office 2016个人版支持分析报告的大部分功能。详情可参考 插件使用注意事项。
3、WPS Office 2019个人版需要安装宏安装包才能使用Smartbi内置函数，并且在安装宏安装包后，在WPS的“**开发工具 > 宏安全性**”界面将安全级设置为“低”，否则总是提出安全警告提示。
4、原则上，WPS个人版不支持直接安装宏插件，用户如果有需要使用WPS的宏，需要自行在网上寻找相应WPS版本的VBA安装包。
5、插件端除了不支持W.P.S.9208.12012.2019版本以外，其他版本均可正常登录及使用。
6、Microsoft Office 365 网页版不支持excel或office插件。桌面版本可以支持。
处理器推荐4核或以上  
---  
内存推荐4GB以上  
操作系统 | Windows 2008/2012/Win7/Win8/Win10 64位操作系统  
推荐使用“Chrome、360极速、Firefox”的新版本。 支持的最低版本如下：
  * **360极速** ：9.0（仅支持极速模式）
  *   * **Edge** ：基于Chromium内核的版本
  * **可信浏览器：** 国密开发者专版 1.1.45335.52基于Chromium内核的版本
  * **红莲花浏览器：** 基础版5.0.3.8，基于Chromium内核的版本
  * ，基于Chromium内核的版本

1）V11不支持IE浏览器。 2）浏览器都必须使用64位。  
移动设备（平板/手机） |  支持下列系统移动设备：
  * iOS 9.0.3（原控件版APP，不再维护，无法上架AppStore，只能从Smartbi官网下载。）
  * iOS 12.0（WK控件版，已经上架AppStore，也可以从Smartbi官网下载。）
  * Android 6.0
  * HarmonyOS 2.0.0

  
语言环境当前仅支持简体中文、繁体中文和英文  
