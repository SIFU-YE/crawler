#### 通过
# MDX 数据定义 - CREATE SET
为当前多维数据集创建具有会话作用域的命名集。
```
  
CREATE [SESSION] [ STATIC | DYNAMIC ] [HIDDEN] SET   
   CURRENTCUBE | Cube_Name  
      .Set_Name AS 'Set_Expression'  
      [,Property_Name = Property_Value, ...n]  

```

_Cube_Name_ 提供多维数据集名称的有效字符串表达式。
_Set_Name_ 为要创建的命名集提供名称的有效字符串表达式。
_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Property_Name_ 提供集属性名称的有效字符串。
_Property_Value_ 定义集属性值的有效标量表达式。
命名集是为重用而创建的维度成员集（或者是用于定义集的表达式）。 例如，使用命名集可以定义由销售额排在前十名的商店组成的维度成员集。 此集可以静态定义，也可以通过 TopCount 等函数进行定义。 然后，可以在需要前 10 个存储集的任意位置使用此命名集。
CREATE SET 语句创建一个在整个会话中保持可用的命名集，因此，可以在会话中的多个查询中使用。 有关详细信息，请参阅  (MDX) 创建Session-Scoped计算成员 。
也可以定义用于单个查询的命名集。 若要定义这种集，请在 SELECT 语句中使用 WITH 子句。 有关 WITH 子句的详细信息，请参阅  (MDX) 创建Query-Scoped命名集 。
_Set_Expression_ 子句可以包含支持 MDX 语法的任何函数。 如果使用 CREATE SET 语句创建集时没有指定 SESSION 子句，则该集的作用域为会话。 使用 WITH 子句创建具有查询作用域的集。
指定当前连接的多维数据集以外的多维数据集将导致错误。 因此，应使用 CURRENTCUBE 来代替多维数据集名称，以表示当前的多维数据集。
用户定义的集的作用域可以是下表所列的任意一个作用域。
查询范围 集的可见性和生存期被限制在查询中。 集是在单个查询中定义的。 查询作用域将覆盖会话作用域。 有关详细信息，请参阅  (MDX) 创建Query-Scoped命名集 。
会话范围 集的可见性和生存期被限制在创建该集的会话中。 (如果在 set 上发出 DROP SET 语句，则生存期小于会话持续时间。) CREATE SET 语句创建具有会话范围的集。 使用 WITH 子句创建具有查询作用域的集。
以下示例创建名为 Core Products 的集。 SELECT 查询并显示调用新创建的集。 必须先执行 CREATE SET 语句才可以执行 SELECT 查询 - 这两个语句不能在同一批中执行。
```
CREATE SET [Adventure Works].[Core Products] AS '{[Product].[Category].[Bikes]}'  
  
SELECT [Core Products] ON 0  
  FROM [Adventure Works]  

```

集的求取可以定义不同的发生方式；可以定义为仅在集创建时发生一次，也可以定义为在每次使用集时发生。
STATIC 指示只在执行 CREATE SET 语句时，求取一次该集。
DYNAMIC 指示每次在查询中使用该集时，都进行求取。
对于查询多维数据集的其他用户来说，集可以是可见的，也可以是不可见的。
HIDDEN 指定该集对查询多维数据集的用户不可见。
每个集都有一组默认属性。 当客户端应用程序连接到 Analysis Services 时，默认属性要么受支持，要么可供支持，由管理员选择。
CAPTION | 客户端应用程序用作集标题的字符串。  
---|---  
DISPLAY_FOLDER | 标识客户端应用程序用来显示集的显示文件夹路径的字符串。 文件夹级别的分隔符由客户端应用程序定义。 对于 Analysis Services 提供的工具和客户端，反斜杠 (\\) 是级别分隔符。 若要为已定义的集提供多个显示文件夹，则使用分号 (;) 来分隔文件夹。  
DROP SET 语句 (MDX) MDX 数据定义语句 (MDX)
1月27日 15时 - 1月27日 15时 


