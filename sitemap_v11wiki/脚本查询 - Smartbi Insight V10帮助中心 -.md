
脚本查询是指通过编写代码脚本获取数据结果。
**适用情况：** 各种非结构化数据、特殊数据。
目前“脚本查询”支持的语言只有JavaScript，因此适用于熟悉JavaScript的技术人员。相关接口文档可参考IJavaQueryData。
  * 

## 操作入口
在“数据模型”定制界面单击创建私有查询按钮，选择**脚本查询** （如下图所示），进入脚本查询的定制界面。
## 界面介绍
脚本查询定制界面如下图所示：
“脚本查询”界面主要分为以下几个区域：
  * 功能按钮区：列出了可操作脚本查询的工具按钮；
  * 脚本编辑区：编辑脚本代码；
  * 参数设置/预览数据区：设置脚本的参数，查看输出的数据；


### 功能按钮区
功能按钮区的具体说明如下表：
执行脚本。若脚本的结果集中包含参数且未设置默认值，则会提示用户输入参数默认值。  
---  
将当前脚本查询保存到“数据模型”定制界面的表关系区内，如果是第一次创建，则会在表关系区创建对应的节点，节点名称默认为“脚本查询”。  
对脚本编辑区内的代码进行格式化操作，使其符合代码规范  
  * 校验脚本编辑区中的代码，如果有语法错误则提示具体的错误


  * 如果正确则提示校验成功。

  
在脚本编辑区生成内置的JavaScript示例代码  
返回到数据模型主页面  
###  脚本编辑区
用户可在此区域进行脚本代码的编写。
  * 在方法init()内可以自定义结果集，自定义私有参数和输出字段。私有参数，用于过滤数据。


  * 代码编辑完成后，鼠标点击编辑区域以外的区域，则会校验脚本语法，并识别所编写脚本的结果集中的参数，在“参数设置”区域生成对应的参数。


### 参数设置/数据预览区
用于显示执行脚本查询后的数据结果，主要分为**参数设置界面** 和**数据预览区** 。
1）参数设置界面
若在脚本代码的结果集中定义了参数，点击按钮 **参数设置** 切换至“参数设置”页面，“参数设置”页面会显示对应的参数，设置参数的默认值；
2）数据预览区
单击 **数据预览** 按钮可切换至数据预览区，查看输出数据；
数据预览前需在“参数设置”页面设置默认值后，点击功能按钮区中的“执行”按钮，数据预览页面才会输出相关数据。
（3）展开或收缩 数据结果展示区
  * 点击符号“∧”可将该区域展开，点击符号“∨”可将开区域收起。


示例演示
本示例以数据源“northwind”中的"产品表”为目标资源，展示了如何通过编写JavaScript脚本获取指定节点ID的数据源表数据，具体操作如下：
### 获取资源节点ID
左侧 “系统导航栏”中的“数据连接” ，选择 **“数据连接” > “northwind” > “产品表”** ，右键打开扩展菜单，点击“属性”。
记录下该资源的节点ID：
### 新建“脚本查询”节点
### 编写脚本
复制代码到“脚本编辑区”，并修改目标资源的节点id。
**示例代码·读取指定节点资源的表数据**
```
importPackage(Packages.smartbi.freequery.client.datasource);

var datasourceService = DataSourceService.getInstance();
var tableId = "TAB.northwind.null.products";   //目标资源的节点ID
var table = datasourceService.getTable(tableId);
var sql = "select";
var data;

function init() {
    var fieldList = table.getFields();
    var fields = [];
    for (var i = 0; i < fieldList.size(); i++) {
        var field = fieldList.get(i);
        sql = sql + " " + field.getName();
        fields[i] = {
            id: field.getId(), //字段ID
            name: field.getName(), //字段名称
            alias: field.getAlias(), //字段别名
            desc: field.getDesc(), //字段描述
            valueType: parseValueType(field.getDataType().getSQLType()) //字段数据类型：INTEGER | DOUBLE | LONG | STRING | DATETIME
        }
        if (i < fieldList.size() - 1) {
            sql = sql + ",";
        }
    }
    sql = sql + " from " + table.getName();
    return {
		// //参数列表
		// params: [{
			// id: 'Param.northwind.null.products', //参数ID
			// name: 'ParamName', //参数名称
			// alias: 'ParamAlias', //参数别名
			// desc: 'ParamDesc', //参数描述
			// nullable: true, //参数是否允许是空
			// valueType: 'STRING' //参数数据类型：INTEGER | DOUBLE | LONG | STRING | DATETIME
		// }],
		//输出字段
        fields: fields
    };
}

function getGridData(paramValues, from, count) {
    data = datasourceService.executeNoCacheable(table.getDataSource().getId(), sql);
    return data;
}


function getRowCount() {
    return data.getRowsCount();
}


/**
  关闭查询对象
*/
function close() {}

function parseValueType(type) {
    switch ("" + type) {
        case "LONG":
            return "LONG";
        case "BIGINT":
        case "INTEGER":
            return "INTEGER";
        case "BIGDECIMAL":
        case "DOUBLE":
            return "DOUBLE";
        case "TIME":
        case "DATE":
        case "DATETIME":
            return "DATETIME";
        default:
            return "STRING";
    }
}
```

### 校验语法
单击 **校验脚本** 按钮，校验脚本语法。
### 执行脚本
单击 **执行** 按钮，执行脚本，执行完成后数据预览区便会显示输出的数据。
### 保存节点到数据模型页面
单击 **保存** 按钮，系统提示保存成功后，当前脚本查询会以表的输出节点方式保存在数据模型的”表关系区“中。  
