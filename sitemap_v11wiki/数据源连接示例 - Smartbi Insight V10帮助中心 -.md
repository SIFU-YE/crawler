
数据库连接示例 | 支持数据库版本 | 驱动程序类 | 连接字符串  
---|---|---|---  
Aliyun AnalyticDB 公有云 | com.mysql.jdbc.Driver | jdbc:mysql://<servername>/<database>?useUnicode=true&characterEncoding=UTF-8&engine=MPP  
Aliyun MaxCompute 公有云 | com.aliyun.odps.jdbc.OdpsDriver | jdbc:odps:<endpoint>?project=<project>&charset=UTF-8  
ClickHouse19.4.2  | ru.yandex.clickhouse.ClickHouseDriver |  jdbc:clickhouse://<servername>:8123/<database>?socket_timeout=1000000 *注：产品默认端口为 8123，可以按照实际进行修改。  
DB2 9.72 | com.ibm.db2.jcc.DB2Driver | jdbc:db2://<servername>:<port>/<database>  
GaussDB 100 | com.huawei.gauss.jdbc.ZenithDriver | jdbc:zenith:@<servername>:<port>?useSSL=true  
GaussDB 200 V6.5 | com.huawei.gauss200.jdbc.Driver |  jdbc:gaussdb://<servername>:25308/<dbName> *注：产品默认端口为 25308，可以按照实际进行修改。  
Gbase 8A V8.6.2.23-R14.95765 | com.gbase.jdbc.Driver | jdbc:gbase://<servername>:<port>/<dbName>  
GBase 8S V8.4 |  com.informix.jdbc.IfxDriver |  jdbc:informix-sqli://<host>:9088/<database>:INFORMIXSERVER=<servicename>;CLIENT_LOCALE=zh_cn.utf8;DB_LOCALE=zh_cn.utf8;NEWCODESET=utf8,8859-1,819 *注：产品默认端口为 9088，可以按照实际进行修改。请补充各个字段的含义  
GBase 8S V8.8  
Greenplum 4.3.9 | org.postgresql.Driver |  jdbc:postgresql://<servername>:5432/<dbName>?gssEncMode=disable *注：产品默认端口为 5432，可以按照实际进行修改。  
Hadoop 2.7.2 Hive 2.0.0 | org.apache.hive.jdbc.HiveDriver |  jdbc:hive2://<servername>:10000/default?hive.resultset.use.unique.column.names=false *注：产品默认端口为 100000，可以按照实际进行修改。  
HANA V2.0 | com.sap.db.jdbc.Driver |  jdbc:sap://<servername>:30015?reconnect=true *注：产品默认端口为 30015，可以按照实际进行修改。  
HuaWei FusionInsight HD | org.apache.hive.jdbc.HiveDriver |  jdbc:hive2://<zkServer1>:24002,<zkServer2>:24002,<zkServer3>:24002/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2;sasl.qop=auth-conf;auth=KERBEROS;principal=hive/hadoop.hadoop.com@HADOOP.COM *注：<zkServer1，zkServer2，zkServer3>为数据库的地址，可以按照实际进行修改。  
IMPALA V3.0 | com.cloudera.impala.jdbc41.Driver | jdbc:impala://<servername>:<port>/<database>  
Infobright | com.mysql.jdbc.Driver | jdbc:mysql://<servername>:<port>/<database>?useOldAliasMetadataBehavior=true&useUnicode=true&characterEncoding=GBK&zeroDateTimeBehavior=convertToNull  
Informix 115 | com.informix.jdbc.IfxDriver | jdbc:informix-sqli://<servername>:1526/<database>:INFORMIXSERVER=<InformixServer>;NEWLOCALE=zh_cn,en_us;NEWCODESET=GBK,8859-1,819  
Kingbase V7 | com.kingbase.Driver |  jdbc:kingbase://<servername>:54321/<dbName> *注：产品默认端口为 54321，可以按照实际进行修改。  
KADB 3.0.14 | com.kingbase.kingbaseanalyticsdb.Driver | jdbc:kingbaseanalyticsdb://<servername>:<port>/<database>  
kylin 2.0 | org.apache.kylin.jdbc.Driver  | jdbc:kylin://<servername>:<port>/<projectName>  
SQL Server 2008 | net.sourceforge.jtds.jdbc.Driver |  jdbc:jtds:sqlserver://<servername>:1433;DatabaseName=<database> *注：产品默认端口为 1433，可以按照实际进行修改。  
MySQL 5.7 MySQL 8.0 | com.mysql.jdbc.Driver | jdbc:mysql://<servername>:<port>/<database>?useOldAliasMetadataBehavior=true&useUnicode=true&characterEncoding=GBK&zeroDateTimeBehavior=convertToNull  
Obase 1.0.44 | com.mysql.jdbc.Driver | jdbc:mysql://<servername>/<database>?useOldAliasMetadataBehavior=true&useUnicode=true&characterEncoding=GBK&zeroDateTimeBehavior=convertToNull  
oracle 10g | oracle.jdbc.driver.OracleDriver |  jdbc:oracle:thin:@<ip>:1521/<serviceName> *注：产品默认端口为1521，可以按照实际进行修改。  
| TimesTen 11.2.2 | com.timesten.jdbc.TimesTenClientDriver | jdbc:timesten:client:dsn={dsnname}  
PostgreSQL 10.5 | org.postgresql.Driver |  jdbc:postgresql://<servername>:5432/<dbName> *注：产品默认端口为5432，可以按照实际进行修改。  
presto 0.189 | com.facebook.presto.jdbc.PrestoDriver | jdbc:presto://<servername>:38080/<database>  
shentong 7.0 | com.oscar.Driver | jdbc:oscar://<servername>/<database>  
Smartbi JDBC for Excel | smartbi.jdbc.ExcelDriver | jdbc:smartbi:excel:<filename or fileresource:id>  
Smartbi Jdbc 4 Olap | smartbi.jdbc.OlapDriver | http://<servername>/smartbixmla/XmlaHandler.ashx  
SparkSQL 2.0.0 | org.apache.hive.jdbc.HiveDriver |  jdbc:hive2://<servername>:10000/default *注：产品默认端口为10000，可以按照实际进行修改。  
sybase IQ 16.0 | com.sybase.jdbc3.jdbc.SybDriver | jdbc:sybase:Tds:<servername>:<port>/<database>?CHARSET=cp936  
Teradata_V12 | com.teradata.jdbc.TeraDriver | jdbc:teradata://<servername>/DataBase=<dbName>,LOB_SUPPORT=off,client_charset=gbk  
Teradata_V13及以上 | com.ncr.teradata.TeraDriver | jdbc:teradata://<servername>/DataBase=<dbName>,LOB_SUPPORT=off,client_charset=gbk  
vertical 8.1 | com.vertica.jdbc.Driver |  jdbc:vertica://<servername>:5433/<database> *注：产品默认端口为5433，可以按照实际进行修改。  
达梦6 | dm6.jdbc.driver.DmDriver |  jdbc:dm6://<servername>:5236/<database> *注：产品默认端口为5236，可以按照实际进行修改。  
达梦7 | dm.jdbc.driver.DmDriver |  jdbc:dm://<servername>:5236/<database> *注：产品默认端口为5236，可以按照实际进行修改。  
星环 5.1.2 | org.apache.hive.jdbc.HiveDriver |  jdbc:hive2://<servername>:10000/default *注：产品默认端口为10000，可以按照实际进行修改。  
Phoenix | 根据实际情况填写  
MongoDB | smartbi.jdbc.MongoDriver | jdbc:smartbi:mongo:<server>:<port>/<dbName>  
MonetDB | org.monetdb.jdbc.MonetDriver |  jdbc:monetdb://<servername>:<port>/<database> *注：产品默认端口<port>为50000，可以按照实际进行修改。  
