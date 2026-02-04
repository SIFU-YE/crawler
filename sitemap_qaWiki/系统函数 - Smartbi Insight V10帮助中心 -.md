
系统函数指与用户信息相关的一类函数，包括内置的系统函数和用户自定义的函数。
例如在数据权限管理、与用户权限相关的查询定义中通常会使用到这些函数。
其中内置的函数不允许删除，自定义的函数允许删除。
## 系统内置函数
系统内置的函数主要是一些常用的函数，比如当前用户的信息。一般用户在数据权限设置中使用。
系统内置的函数如下：
字符串 | GetSubDepartments() | 获取指定用户组的子组，参数是组编号。例如，获取" 华南"下面的子组GetSubDepartments(’华南的组编号‘)。  
---|---|---  
CurrentUserDefaultDepartmentAndSubDepartments() | 获取当前用户默认组和子组。  
CurrentResourceTypes() | 获取资源类型列表。  
CurrentMonth() | 获取当前月份。  
CurrentDatetime() | 获取当前日期和时间。  
CurrentUserAllRoleIDs() | 获取当前用户拥有的角色id。  
CurrentUserAllRoleNames() | 获取当前用户拥有的角色名字。  
Concat() | 拼接字符串。参数：[字符串...]。  
CurrentUserAlias() | 获取当前用户别名。无参数。  
CurrentUserID() | 获取当前用户的编号。无参数。  
CurrentUserName() | 获取当前用户的名称。无参数。  
GetCookie() | 获取Cookie信息。参数1：cookiePropertyName[字符串]。  
GetFirstDayOfFrequencyParameter() | 获取频度日期参数值对应的第一天，例如获取2012年第1周的第一天，返回值为2012-01-01。参数：参数值[字符串]。  
GetLastDayOfFrequencyParameter() | 获取频度日期参数值对应的最后一天，例如获取2012年第1周的最后一天，返回值为2012-01-07。参数：参数值[字符串]。  
GetUserProperty(propertyName) | 获取用户属性的值。参数：propertyName—指系统管理中的“用户属性”名。使用示例可参考设置数据权限  
GetUserProperty() | 获取用户属性。参数1：propertyName[字符串]。  
CurrentUserAllDepartmentIDRecursively() | 当前用户所属机构及其所有子机构的编号。无参数。  
CurrentUserDepartments() | 获取用户所属机构的编号，无参数。用法常见于 select 字段 from table where 字段 in (CurrentUserDepartments())。  
CurrentUserDefaultDepartmentAlias() | 获取用户所属默认用户组的别名。无参数。  
CurrentUserDefaultDepartmentID() | 获取用户所属默认用户组的编号。无参数。对应知识库中t_group表中的c_orgid字段。  
CurrentUserDefaultDepartmentName() | 获取用户所属默认用户组的真名。无参数。  
CurrentReportName() | 获取报表名称的系统函数  
GetSessionAttribute(AttributeName) |  获取当前会话中的属性值；参数是“属性名称”。 前提：通过代码向会话中插入属性，包含属性名称和属性值。 示例：通过调用相关api向会话中插入属性用户昵称，属性名称为"user_nickname”，属性值为"小花"。使用系统函数GetSessionAttribute("user_nickname"），即可获取“小花”。  
Process1000LimitOfIn() |  处理多选树参数或下拉框参数超过1000时报错问题。当参数超过1000时，函数会将其转化为“字段 in (list1) or 字段 in (list2)” 参数有两个：
  * 第一个参数：字段名，如果是可视化数据集，直接拖字段，如果是原生SQL数据集，最好用英文双引号括起来，如table1."A"。
  * 第二个参数：Smartbi的多选树或下拉框参数，直接拖参数。

  
GetSelectedMembers() | 获取当前多维分析中指定维度层次下的所有成员。参数是“hierarchy”即维度层次。该函数常用于自定义成员中汇总表达式。  
GetUserAccessibleMembers() |  获取指定维度层次中当前用户具有数据访问权限的成员。参数有两个：
  * 第一个参数：“hierarchy”即维度层次。
  * 第二个参数：“Self”表示获取顶层成员；“SelfAndChildren”表示获取顶层成员及其子成员；“Children”表示获取顶层成员的子成员。

  
GetUserPropertyWithoutBrackets(propertyName) | 获取用户属性(不使用括号)。参数1：propertyName[字符串]。  
GetUserIP() | 获取当前用户登录的IP地址。无参数。  
GetUserExAttr(attrName) | 获取当前用户的指定扩展属性。参数1：attrName[字符串] （扩展属性的属性名）。  
CurrentDate() | 获取当前应用服务器日期，支持即席查询、透视分析、多维分析和多维探索的页面展示及导出。  
GetCurrentFlowProperty() | 获取当前流程属性。  
GetFlowCreatorID() | 获取当前流程发起人，仅在流程“操作者”的自定义配置使用。  
GetVisibleMembers() | 返回当前查询中指定层次结构中非前端隐藏的成员表达式。  
数值 | DoubleValue()  
GetCurrentGroupCount() | 获取系统用户组总数。  
GetCurrentOnlineSessionCount() | 获取当前在线会话数。  
GetCurrentOnlineUserCount() | 获取当前在线用户数  
GetCurrentResourceCount() | 获取系统资源总数。  
GetCurrentUserCount() | 获取系统用户总数。  
电子表格函数 | ExecNamedSQL() | 执行命名SQL，将查询结果填入当前单元格中。  
ExecSQL() | 执行SQL语句，将查询结果填入当前单元格中。  
FillNamedSQLData() | 将命名SQL结果填入表格，按返回的行、列数向下、向右覆盖填入。  
FillSQLData() | 执行SQL结果填入表格，按返回的行、列数向下、向右覆盖填入。  
获取当前日期时间。无参数。  
Today() | 获取当前日期。无参数。  
Date(year, month, day) | 生成指定日期。year：年；month：月；day：日。  
Time(hour, minute, second) | 生成指定时间。hour：时；minute：分；second：秒。  
DateTimeAdd(date, delta...) |  获取指定日期。参数有两个：
  * date：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。
  * delta..：偏移量，格式为数值+单位，可以输入多个，以英文逗号隔开，单位包含Y、M、W、D、h、m、s，代表年、月、周、日、时、分、秒），例如-1D代表前一天。

  
YearAdd(date, delta) |  获取指定日期偏移多少年后的日期。参数有两个：
  * date：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。
  * delta：偏移量，可以为正值，负值，零。

  
MonthAdd(date, delta) |  获取指定日期偏移多少个月后的日期。参数有两个：
  * date：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。
  * delta：偏移量，可以为正值，负值，零。

  
DateAdd(date, delta) |  获取指定日期偏移多少天后的日期。参数有两个：
  * date：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。
  * delta：偏移量，可以为正值，负值，零。

  
Year(serial_number) |  获取指定日期中的年。 serial_number：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。  
Month(serial_number) |  获取指定日期中的月（1-12之间的一个数）。 serial_number：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。  
Day(serial_number) |  获取指定日期中的日（ 1-31 的整数）。 serial_number：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。  
Hour(serial_number) |  获取指定日期时间中的小时（介于 0 (12 A.M.) 到 23 (11 P.M.) 之间的整数）。 serial_number：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。  
Minute(serial_number) |  获取指定日期时间中的分钟（ 0-59 的整数）。 serial_number：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。  
Second(serial_number) |  获取指定日期时间中的秒（0-59 的整数）。 serial_number：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。  
Lunar(date) |  获取指定日期的农历（闰月的月份）。 date：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。  
DateDif(start_date, end_date, unit) |  获取两个指定日期差值（起始日期不得小于结束日期）。参数有三个：
  * start_date：起始日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。
  * end_date：结束日期，支持公共参数或输入固定的日期字符串，如“2024-02-01” 。
  * unit：单位，可为Y、M、D，代表年差值、月差值、日差值。

  
Days360(start_date, end_date) |  按照一年 360 天的算法(每个月以 30 天计，一年共计 12 个月)，返回两日期间相差的天数。参数有两个：
  * start_date：起始日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。
  * end_date：结束日期，支持公共参数或输入固定的日期字符串，如“2024-02-01” 。

  
WeekNum(serial_number) |  获取指定日期在一年中的第几周。 serial_number：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。  
WeekDay(serial_num) |  返回指定日期为星期几（1(星期天)到 7(星期六)之间的整数）。 serial_num：指定日期，支持公共参数或输入固定的日期字符串，如“2024-01-01” 。  
逻辑函数 | IF() | 参数1：条件（必填），参数2：true结果（必填），参数3：false结果（可选）  
注意
以上系统函数的参数，均不支持字段。
## 自定义函数
系统允许用户自定义“字符串”类型的系统函数，以实现一些特殊功能需求：如实现“上年同期”、“取年末或是月末的值”等。
在系统中设置自定义函数，请执行下列操作：
(1) 创建扩展包，编写自定义系统函数类（使用Java语言编写）。
(2) 将编写好的自定义函数类文件存放在扩展包的以下包名下：smartbi.freequery.expression.function。
(3) 在应用服务器上重新部署扩展包。
(4) 重启应用服务器，在在“系统导航栏”选择 **公共设置** ，展开资源目录区，选择 **函数列表 > 系统函数 > 字符串，点击**更多操作，选择 **增加自定义函数（I）。**
(5) 在“字符串”的右键菜单中选择 增加自定义函数，弹出“自定义函数”窗口。
(6) 在“自定义函数”窗口输入名称，该名称必须要与放入到“function”目录中的自定义函数类文件名称一致。
(7) 创建完成后，就可以和系统内置函数一样在产品中拖拽使用了。  
