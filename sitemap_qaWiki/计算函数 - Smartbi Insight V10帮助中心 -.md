
  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   * 

## 概述
电子表格的计算函数包含两种，Excel自带的函数和Smartbi函数，两者可以结合使用。
公式函数不区分大小写。
关于Excel自带的函数，请参考如下示例：
## SSR_ExecQuery


关于Smartbi函数，请参考如下示例：


SSR函数不支持回写
SSR_ExecFunc(让项目上的用户扩充自己的Excel函数。在项目扩展包中编写函数类并实现接口) SSR_ExecNamedSQL(执行命名SQL语句，将查询结果填入单元格中) SSR_ExecQuery(执行数据集定义的SQL，将查询结果填入单元格中) SSR_ExecSQL(执行SQL语句，将查询结果填入单元格中) SSR_FillNamedSQLData(根据映射表中的映射名称执行sql，将查询结果集填入表格中，按返回的行、列数向下、向右覆盖单元格) SSR_FillQueryData(执行数据集定义中的sql，将查询结果集填入表格中，按返回的行、列数向下、向右覆盖单元格) SSR_FillSQLData(将SQL结果集填入表格中，按返回的行、列数向下、向右覆盖填入) SSR_GetCell(获取单元格，支持偏移计算) SSR_GetCurrentPage(获取电子表格当前页数) SSR_GetCurrentUserAlias(获取当前用户别名) SSR_GetCurrentUserName(获取当前用户名称) SSR_GetIndex(获得单元格位于某个父格中的位置，以实现序列号) SSR_GetParamDisplayValue(根据参数名称获取参数显示值) SSR_GetParamValue(根据参数名称获取参数真实值) SSR_GetSubcells(根据父格获取扩展得到的所有单元格) SSR_GetTotalPage(获取电子表格总页数)  
---  
## SSR_ExecFunc
**函数原型：** SSR_ExecFunc(clzName, args1, args2, ...)
**参数说明：** clzName 是实现类的全名，如果包名为“smartbi.spreadsheetreport.core.func” 则可以忽略包名只写类名，这里可以考虑使用中文类名。
**功能说明：** 让项目上的用户扩充自己的Excel函数。在项目扩展包中编写函数类并实现接口，SSR_ExecFunc 实现 smartbi.spreadsheetreport.core.func.ICellFunction { Object getData(Object[] args);} ,如果实现了 smartbi.spreadsheetreport.core.func.IGridFunction 则只返回第一行第一列的值到单元格中。
**注意事项：** 函数中返回的Object 只可以是数值、字符串或日期类型。
## SSR_ExecNamedSQL
**函数原型：** SSR_ExecNamedSQL(datasourceId,name,rowIndex,columnIndex,param1,param2,...)
**参数说明：** datasourceId为数据源ID；name为命名SQL，命名SQL可以查看 system->分析报表->SQL映射表 获得；rowIndex为结果集中的行位置，可以忽略不填写；columnIndex为结果集中的列位置，可以忽略不填写；param1为SQL中的参数值，可以是静态数据也可以指定单元格；param2同param1。可以传递多个SQL参数值。
**功能说明：** 执行命名SQL语句，将查询结果填入单元格中。
**注意事项：** 该函数不支持“清单报表”方式。
## SSR_ExecQuery
**函数原型：** SSR_ExecQuery(queryid,rowIndex,columnIndex,param1,param2,...)
**参数说明：** queryid为数据集的 ID；rowIndex为结果集中的行位置，可以忽略不填写；columnIndex为结果集中的列位置，可以忽略不填写；param1数据集参数值，当前只支持静态数据；parameter2，同param1。可以传多个参数，其中参数的传递方式是：参数别名:参数值或者参数名:参数值，如：SSR_ExecQuery("I40288190015ea8a8a8a81001015ebd4db3da5131",0,0,"A基础资源-下拉树-区域:华北", " A基础资源-联动参数-城市:北京")。
**功能说明：** 执行数据集定义的SQL，将查询结果填入单元格中。
**注意事项：** 该函数不支持“清单报表”方式。
## SSR_ExecSQL
**函数原型：** SSR_ExecSQL(datasourceid,sql,rowIndex,columnIndex,param1,param2,...)
**参数说明：** datasourceid为数据源ID；sql为需要执行的sql语句；rowIndex为结果集中的行位置，可以忽略不填写；columnIndex为结果集中的列位置，可以忽略不填写；param1为SQL中的参数值，可以是静态数据也可以指定单元格；param2同理，可以传多个参数。
**功能说明：** 执行SQL语句，将查询结果填入单元格中。
**函数示例：“** =SSR_ExecSQL("DS.回写","select qichu from balance_sheet where f_year=? And kemu=trim(?)",0,0,"2012","流动资产")”，表示在数据源“回写”中执行sql语句 select qichu from balance_sheet where f_year="2012" and kemu=trim("流动资产")，并将返回的结果集中的第一行第一列的数据放到单元格中 。其中0,0可以省略，如以下公式实现的是同样的功能“=SSR_ExecSQL("DS.回写","select qichu from balance_sheet where f_year=? And kemu=trim(?)","2012","流动资产") ”。
**注意事项：** 该函数不支持“清单报表”方式。
## SSR_FillNamedSQLData
**函数原型：** SSR_FillNamedSQLData(datasourceId,sqlName,rowCount,param1,param2,...)
**参数说明：** datasourceId为数据源ID；sqlName为映射表中的映射SQL名称；rowCount为返回的数据行数；param1为SQL的参数，可以是静态数据也可以指定单元格;param2同param1；可以传递多个参数。
**功能说明：** 根据映射表中的映射名称执行sql，将查询结果集填入表格中，按返回的行、列数向下、向右覆盖单元格。
**注意事项：** 该函数不支持“清单报表”方式。
## SSR_FillQueryData
**函数原型：** SSR_FillQueryData(queryId,rowCount,param1,param2,...)
**参数说明：** queryId为对应的数据集的ID；rowCount为返回的数据行数；param1为SQL的参数，可以是静态数据也可以指定单元格;param2同param1；可以传递多个参数。
**功能说明：** 执行数据集定义中的sql，将查询结果集填入表格中，按返回的行、列数向下、向右覆盖单元格。
**注意事项：** 该函数不支持“清单报表”方式。
## SSR_FillSQLData
**函数原型：** SSR_FillSQLData(datasourceid,sql,rowCount,param1,param2,...)
**参数说明：** datasourceid为数据源ID；sql为在数据库中执行的sql语句；rowCount为返回的数据行数；param1为SQL的参数，可以是静态数据也可以指定单元格;param2同param1；可以传递多个参数。
**功能说明：** 将SQL结果集填入表格中，按返回的行、列数向下、向右覆盖填入。
**注意事项：** 该函数不支持“清单报表”方式。
## SSR_GetCell
**函数原型：** SSR_GetCell(取数单元格,{父单元格,偏移量}*n )
**参数说明：** 取数单元格为取得数据的单元格序号。其中父单元格为单元格序号。偏移量是整数，负数表示当前单元格向上偏移，正数表示向下偏移。父单元格和偏移量成对出现，可以一个都不写，也可以出现多次。
**功能说明：** 获取单元格，支持偏移计算。用于在扩展区域中按位置取单元格的值。其原理是，取出当前单元格的所有父单元格，变换指定的父单元格，其它不变，获取指定取数单元格的值。
**函数示例：** 单个偏移SSR_GetCell(C4,A4,-1)，多个偏移SSR_GetCell(D5,B5,-1,C5,1)。关于示例详情请参考电子表格⬝ 累计 章节。
## SSR_GetCurrentPage
**函数原型：** SSR**_** GetCurrentPage()
**功能说明：** 获取电子表格当前页数。
**注意事项：** 电子表格分页才可以使用此函数获取值。
## SSR_GetCurrentUserAlias
**函数原型：** SSR_GetCurrentUserAlias()
**功能说明：** 获取当前用户别名。
## SSR_GetCurrentUserName
**函数原型：** SSR_GetCurrentUserName()
**功能说明：** 获取当前用户名称。
## SSR_GetIndex
**函数原型：** SSR_GetIndex(Cellx)
**参数说明：** Cellx是当前单元格的某个父格，该表达式返回的值是当前单元格在指定父格中的位置。如果Cellx不是最高级别的父格，也就是说在Cellx也有父格的前提下，该表达式返回的值是指在Cellx所属父格分组内的位置。
**功能说明：** 获得单元格位于某个父格中的位置，以实现序列号。
## SSR_GetParamDisplayValue
**函数原型：** SSR_GetParamDisplayValue("参数名称")
**参数说明：** 参数为参数名称，是字符串。
**功能说明：** 根据参数名称获取参数显示值。
**函数示例：“** =SSR_GetParamDisplayValue("产品类别")”，表示获取参数名称为"产品类别"的参数显示值。
## SSR_GetParamValue
**函数原型：** SSR_GetParamValue("参数名称")
**参数说明：** 参数为参数名称，是字符串。
**功能说明：** 根据参数名称获取参数真实值。
**函数示例：“** =SSR_GetParamValue("产品类别")”，表示获取参数名称为"产品类别"的参数真实值。
## SSR_GetSubcells
**函数原型：** SSR**_** GetSubCells(取值单元格,父格单元格)
**参数说明：** 取值单元格为取得数据的单元格序号；父格单元格为设置父格的单元格序号。
**功能说明：** 根据父格获取扩展得到的所有单元格。
**函数示例：** “=sum(SSR**_** GetSubCells(C4,A4))”，表示获取父格A4扩展出来的C4单元格的所有值。
“=SSR_GetSubCells(B4:C4,A4)”，表示以A4为父格的B4、C4扩展出来的所有区域。
## SSR_GetTotalPage
**函数原型：** SSR_GetTotalPage()
**功能说明：** 获取电子表格总页数。
**注意事项：** 电子表格分页才可以使用此函数获取值。  
