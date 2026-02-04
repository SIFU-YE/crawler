
# 1、概述
接口查询主要场景是客户不想或者没有办法连接到数据源，需要通过接口的方式获取数；更多的是作为数据集的存在，并且返回的数据是基本都是一个大宽表。
Smartbi 数据模型支持添加 2 种接口查询：Java查询、脚本查询。
前置条件
1、Java查询、脚本查询只支持抽取模式， 如果模型原先是直连模式，加入了Java查询会强制变成抽取模式！详情可查阅：直连&抽取。
2、如果Java查询、脚本查询有定义参数，可参考参数设置进行参数映射。
3、 可参考自定义JavaBean示例获取数据。
4、可参考：带参数Java查询示例。
# 2 Java查询
Java查询是指由用户通过二次开发，自定义JavaQueryData接口实现类，以实现自定义数据结构。
支持以下几种方式：
  * 读取客户放在服务器上文件：CSV查询、Txt查询。
  * 通过http方式获取数据：WebService作为数据源。
  * 需要写java代码从接口获取不开放数据库取数的场景：自定义类。


## 2.1 示例说明
### 2.1 获取文件数据
下面示例演示通"CSV查询"获取文件数据。
刘老师想基于把学生每个月的考试分数进行一个趋势分析，所以把线下数据上传到服务器上方便读取分析。
前置条件
1、如果想复现示例时，可以把数据先导入到模型中，详细请参考**：**导入文件数据**。**
2、可以下载
具体步骤如下：
1、先把 **部署Smartbi war包** 的服务器上，并且文件上传到home目录下； 以Linux服务器为例，可以把文件上传到home目录下; 路径不限，存放的文件夹可以是自己新建的、也可以是已有的文件夹。
2、去建数据模型，并在模型中建 **Java查询** ，并选择 **CSV查询** ，操作如下图：
  * **文件存放路径** ：输入刚存放的路径"/home/StudentScore.csv"; 注意: 一定要输入 **绝对路径**(即指目录下的绝对位置，直接到达目标位置，通常是从盘符开始的路径)，如果不是绝对路径，会查找不到文件。
  * **编码** ：一般填写GBK或UTF-8，也可以根据需求填写其他的编码比如Unicode、ASCII； 另外，上传的文件如果没有列头，则默认以第一行数据为列头。
  * **执行** ：填写配置信息 点击 **执行 ，** 可以预览到文件的数据。


3、 如果想回到数据模型，建议先点击**保存，** 再点击**回到模型** ；回到模型，在 关系视图 可以选中查询，**右键菜单** 可以进行更多操作，具体可查看：设置及修改查询。
4、基于模型去建最终效果如下，可以查看”学生每个月考试分数趋势分析“：
由于 **txt查询** 与 **CSV查询** 都是获取文件数据，逻辑一致，不再单独说明 **txt查询。**
### 2.2 通过自定义类获取数据
对于技术能力比较强的客户，Smartbi提供了灵活的接口，方便用户自定义Java文件，实现某些业务需求。
为了方便举例，使用产品内置的类”获取某段日期范围的会话信息“为例进行查看”日期汇总信息“。
具体的操作如下:
1、创建数据模型并在添加 **Java查询**
  * **自定义类名** ：输入”smartbi.session.SessionQueryData“ 类名。 在输入自定义类名之前，需要先参考二次开发文档，编写IJavaQueryData接口实现类，实现自己的JAVABean逻辑，并将编译好的class文件添加到系统中。相关内容请参考：IJavaQueryData。
  * 输入了 **自定义类名** 之后，点击右侧的 **获取默认配置** ，在配置信息中会出现java类中定义的一些配置信息，对此进行配置，如果没有则无需进行配置。
  * 配置完毕之后，需要点击工具栏的 **执行** 按钮或 鼠标移开，会根据输入的自定义类和配置信息，输出参数和结果集。
  * **参数默认值** ：如果有参数，需要输入参数默认值；给参数”BeginTime“ 默认值设成 ”2023-05-01“, "EndTime"默认值设成”2023-06-01“，"Scale"默认值设成”1“。
  * 点击 **执行** 在 **数据预览** 区域 可以查看参数默认值的数据。


2、执行成功之后，如果要回到数据模型，建议先点击 **保存，** 再回到模型； 回到数据模型，可以在关系视图可以选中 **查询** ，**右键菜单** 支持进行更多操作，具体可查看：设置及修改查询。
如果在模型中没有映射参数，会一直以默认值的结果集输出数据；如果在模型中的 参数设置 进行了关联映射，可以随着模型设置的默认值改变输出结果集；具体可参考：参数管理。
3、基于建好的数据模型去建 查看日期汇总数据：
另外，Java查询自定义类示例，可参考：
### 2.3 通过WebService获取数据
# **3 脚本查询**
脚本查询是指通过编写代码脚本获取数据结果；
目前“脚本查询”支持的语言只有JavaScript，因此适用于熟悉JavaScript的技术人员，相关接口文档可参考IJavaQueryData。
为了方面理解，以产品自带的数据源“northwind”中的 “产品表” 为目标资源，展示了如何通过编写JavaScript脚本获取指定节点ID的数据源表数据的例子来进行说明。
具体操作如下：
1、在左侧 “系统导航栏”中的“数据连接” ，选择 **“数据连接” > “northwind” > “产品表”** ，右键打开扩展菜单，点击“属性”，找到 “产品表” 资源的节点ID，并且记录下来
2、 建数据模型并增加 **脚本查询** , 把刚记录下来的资源节点复制到下图的变量中, 再写获取数据的代码，写完之后，点击 **执行** 执行成功之后可以看到已经获取到**产品表** 的数据：
**示例代码·读取指定节点资源的表数据**
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 |  `importPackage(Packages.smartbi.freequery.client.datasource);` `var` `datasourceService = DataSourceService.getInstance();` `var` `tableId = ``"TAB.northwind.null.products"``//目标资源的节点ID` `var` `table = datasourceService.getTable(tableId);` `var` `sql = ``"select"``;` `var` `data;` `function` `init() {` `var` `fieldList = table.getFields();` `var` `fields = [];` `for` `(``var` `i = 0; i < fieldList.size(); i++) {` `var` `field = fieldList.get(i);` `sql = sql + ``" "` `+ field.getName();` `fields[i] = {` `id: field.getId(), ``//字段ID` `name: field.getName(), ``//字段名称` `alias: field.getAlias(), ``//字段别名` `desc: field.getDesc(), ``//字段描述` `valueType: parseValueType(field.getDataType().getSQLType()) ``//字段数据类型：INTEGER | DOUBLE | LONG | STRING | DATETIME` `if` `(i < fieldList.size() - 1) {` `sql = sql + ``","``;` `sql = sql + ``" from "` `+ table.getName();` `// //参数列表` `// params: [{` `// id: 'Param.northwind.null.products', //参数ID` `// name: 'ParamName', //参数名称` `// alias: 'ParamAlias', //参数别名` `// desc: 'ParamDesc', //参数描述` `// nullable: true, //参数是否允许是空` `// valueType: 'STRING' //参数数据类型：INTEGER | DOUBLE | LONG | STRING | DATETIME` `// }],` `//输出字段` `fields: fields` `function` `getGridData(paramValues, from, count) {` `data = datasourceService.executeNoCacheable(table.getDataSource().getId(), sql);` `return` `data;` `function` `getRowCount() {` `return` `data.getRowsCount();` `关闭查询对象` `function` `close() {}` `function` `parseValueType(type) {` `switch` `(``""` `+ type) {` `case` `"LONG"``:` `return` `"LONG"``;` `case` `"BIGINT"``:` `case` `"INTEGER"``:` `return` `"INTEGER"``;` `case` `"BIGDECIMAL"``:` `case` `"DOUBLE"``:` `return` `"DOUBLE"``;` `case` `"TIME"``:` `case` `"DATE"``:` `case` `"DATETIME"``:` `return` `"DATETIME"``;` `default``:` `return` `"STRING"``;`  
---|---  
3、执行成功后，如果想回到数据模型，建议先 **保存** 再回到数据模型；在模型的关系视图可以选中 **查询** ，**右键菜单** 支持进行更多操作，具体可查看：设置及修改查询。
如果在模型中没有映射参数，会一直以默认值的结果集输出数据；如果在模型中的 参数设置 进行了关联映射，可以随着模型设置的默认值改变输出结果集；具体可参考：参数管理。
在模型中**预览数据** 可以查看 “产品表”的数据信息已获取成功。

  
