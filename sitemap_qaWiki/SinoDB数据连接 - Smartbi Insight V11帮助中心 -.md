
# 1 概述
SinoDB是星瑞格具有自主知识产权的高端国产数据库管理系统产品。
SinoDB采用国密算法，提供多层次数据加密加强数据安全，倾力打造的旗舰级国产数据库软件。
产品安全、可靠、自主、可控，具备高性能、高可用、高稳定等特性，能够满足金融、电信、电力、政府、军工、教育、医疗等各行业核心业务系统的需要，是理想的企业级数据管理和分析平台。
本文介绍如何在Smartbi中连接SinoDB数据库。
1、不支持导入Excel和ETL取数。2、跨库暂不支持该数据库。
3、产品目前暂不支持星格瑞的boolean字段。
# 2 数据连接
## 2.1 配置信息
版本信息如下：
驱动程序存放目录 | 支持数据库版本  
---|---  
com.informix.jdbc.IfxDriver |  jdbc 连接url，默认：jdbc:informix-sqli://<servername>:8080/<database>:INFORMIXSERVER<servicename>;CLIENT_LOCALE=zh_cn.utf8;DB_LOCALE=zh_cn.utf8;NEWCODESET=utf8,8859-1,819 如果自定义了，要严格根据配置来进行设置。 | 自定义 | V16.8  
1）连接字符串主要信息说明：
<servername>：数据库的地址；
<port>：端口号; 
以上信息一般向数据库管理员获取。
2）添加自定义驱动方法，详情可查看：如何向Smartbi中添加数据库驱动：
a、进入到%Smartbi%\Tomcat\bin\dynamicLibraryPath文件夹下，手动添加sinoDb文件夹
b、进入SinoDB文件夹下，添加sinoDb驱动（驱动包可以从数据库官网获取或向数据库管理员获取）。
c、最后在数据源连接时需要点击自定义选项，选择sinoDb。
## 2.2 连接步骤
1）登录Smartbi企业报表分析平台，选择**数据连接 >关系数据库** ，点击** SinoDB**图标进入数据库连接界面。如下图所示：
2）根据 提供的配置信息，输入数据库对应的信息。如下图所示：
说明：
a、名称是数据连接名称，用户可以自定义，不可为空。
b、用户名和密码是连接字符串中配置的数据库的连接用户名和密码，一般可以联系数据库管理员获取。
## 2.3 测试连接
1）信息正确输入后，点击 ，若出现如下图的 弹出框，则表示可以成功连接上数据库。如下图所示：
2）测试连接成功后，点击右下角的按钮，选择数据源的保存位置，保存成功后，该数据连接即添加成功。如下图所示：
3）数据库连接成功后，可以参考 _快速新建透视分析_、 _快速新建即席查询_、 _快速新建电子表格_等 _快速入门_使用方式查看数据。
# 三、注意事项
1、SinoDB不支持设置和获取表字段的注释作为别名。2、数据库没有相关的功能函数无法支持的情况：week(年周)、log2（返回指定浮点数以2为底的对数）。年周函数不支持，数据模型不支持年周时间维度。其他函数不支持只影响到相关函数功能使用。（数据库厂家确认暂时无法支持）。3、数据库没有相关的功能函数无法支持的情况：week、locate、bitlength、insert、position、log2、numberformat。4、默认情况下数据库的引用标识符为空，如果数据库没有设置标识符，数据连接业务库的标识符也必须为空，否则执行sql会报错。5、case when 、union all、coalesce等语句只支持返回同类型数据，例如：
不支持：
select T.orderdate as orderdate, cast(null as BIGINT) as discontinued_mfrom northwind_for_compatibility:informix.orders Tunion allselect to_date(to_char(null, '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S') as orderdate, T.discontinued as discontinued_mfrom northwind_for_compatibility:informix.products T
支持：
select T.orderdate as orderdate, cast(null as BIGINT) as discontinued_mfrom northwind_for_compatibility:informix.orders Tunion allselect CAST(to_date(to_char(null, '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S') AS DATETIME YEAR TO SECOND) as orderdate, T.discontinued as discontinued_mfrom northwind_for_compatibility:informix.products T
6、因为第5点的限制，存在以下不支持情况，需要规避处理：表实际字段类型不是smartbi类型（字符串、整形、长整形、浮点型、长浮点型、日期、日期时间、ASCII编码等，数据模型跨表或sql查询时，需要使用union all处理可能会报错。例如：当表等对象字段两边不相等时，会用cast函数将null转为对应不为null的smartbi字段类型，客户表中的字段可能是boolean、real等类型，但是模型不支持这个类型（数据源管理中表字段也是没有boolean类型的），会转为Integer类型。 就导致 CAST(null AS INTEGER) 与 boolean类型字段union all报类型不匹配。
规避方案：思路是sql简化将没用到的字段裁剪掉，如果这个boolean是需要查询的字段。那么新建一个计算列，将原boolean类型字段转为integer，然后将原字段隐藏，用新的计算列替代原boolean字段。  
