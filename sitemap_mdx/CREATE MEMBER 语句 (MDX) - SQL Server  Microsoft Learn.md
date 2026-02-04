#### 通过
# MDX 数据定义 - CREATE MEMBER
创建计算成员。
```
  
CREATE [ SESSION ] [HIDDEN] [ CALCULATED ] MEMBER CURRENTCUBE | Cube_Name.Member_Name   
   AS MDX_Expression  
      [,Property_Name = Property_Value, ...n]  
......[,SCOPE_ISOLATION = CUBE]  

```

_Cube_Name_ 一个有效的字符串表达式，用于提供要创建成员的多维数据集的名称。
_Member_Name_ 提供成员名称的有效字符串表达式。 指定完全限定名称以在 Measures 维度之外的维度中创建成员。 如果不提供完全限定成员名称，将在 Measures 维度中创建成员。
_MDX_Expression_ 有效的多维表达式 (MDX)。
_Property_Name_ 提供计算成员属性名称的有效字符串。
_Property_Value_ 定义计算成员属性值的有效标量表达式。
CREATE MEMBER 语句定义的计算成员在整个会话期间均可用，因此可在会话期间用于多个查询。 有关详细信息，请参阅  (MDX) 创建Session-Scoped计算成员 。
还可以定义供一个查询使用的计算成员。 若要定义只供一个查询使用的计算成员，请在 SELECT 语句中使用 WITH 子句。 有关详细信息，请参阅  (MDX) 创建Query-Scoped计算成员 。
_Property_Name_ 可以引用标准或可选的计算成员属性。 标准成员属性在本主题后面列出。 使用不带 **SESSION** 值的 CREATE MEMBER 创建的计算成员具有会话范围。 另外，计算成员定义中的字符串用双引号分隔。 这不同于 OLE DB 定义的方法，后者指定字符串应由单引号分隔。
指定当前连接的多维数据集以外的多维数据集将导致错误。 因此，应使用 CURRENTCUBE 来代替多维数据集名称，以表示当前的多维数据集。
有关 OLE DB 定义的成员属性的详细信息，请参阅 OLE DB 文档。
计算成员可出现在下表列出的一个作用域中。
查询范围 计算成员的可见性和生存期限制在查询中。 计算成员在单独的查询中定义。 查询作用域将覆盖会话作用域。 有关详细信息，请参阅  (MDX) 创建Query-Scoped计算成员 。
会话范围 计算成员的可见性和生存期限制在创建计算成员时所在的会话中。 (如果在计算成员上发出 DROP MEMBER 语句，则生存期小于会话持续时间。) CREATE MEMBER 语句创建具有会话范围的计算成员。
当多维数据集多维表达式 (MDX) 脚本包含计算成员时，默认情况下会在解析任何会话范围的计算和解析任何查询定义的计算之前对计算成员进行解析。
在某些情况下， Aggregate (MDX)  函数和 VisualTotals (MDX)  函数不会表现出此行为。
这种行为允许一般客户端应用程序处理包含复杂计算的多维数据集，而不必考虑这些计算的特定实现。 但是，在某些情况下，你可能希望在多维数据集中的某些计算之前执行会话或查询范围的计算成员，而 **Aggregate** 函数和 **VisualTotals** 函数都不适用。 若要完成此操作，应使用 SCOPE_ISOLATION 计算属性。
在下面脚本示例所示的情况下，需要 SCOPE_ISOLATION 计算属性来生成正确的结果。
**多维数据集的 MDX 脚本：**
```
CREATE MEMBER CURRENTCUBE.Measures.ProfitRatio AS 'Measures.[Store Sales]/Measures.[Store Cost]', SOLVE_ORDER = 10  

```

**MDX 查询：**
```
WITH MEMBER [Customer].[Customers].[USA]. USAWithoutWA AS  
[Customer].[Customers].[Country].&[USA] - [Customer].[Customers].[State Province.&[WA], SOLVE_ORDER=5  
SELECT {USAWithoutWA} ON 0 FROM SALES  
WHERE ProfitRatio  

```

上一个查询的所需结果为 USA（不包括 WA）销售额与 USA（不包括 WA）商店成本的比率。 上一个查询未返回所需结果；返回的是 USA 比率减去 WA 比率，这是毫无意义的结果。 若要获得所需的结果，可以使用 SCOPE_ISOLATION 计算属性。
**使用 SCOPE_ISOLATION 计算属性的 MDX 查询：**
```
WITH MEMBER [Customer].[Customers].[USA]. USAWithoutWA AS  
[Customer].[Customers].[Country].&[USA] - [Customer].[Customers].[State Province.&[WA], SOLVE_ORDER=5  
,SCOPE_ISOLATION=CUBE  
SELECT {USAWithoutWA} ON 0 FROM SALES  
WHERE ProfitRatio  

```

每个计算成员都有一个默认属性集。 当客户端应用程序连接到 Analysis Services 时，默认属性要么受支持，要么可供支持，由管理员选择。
其他成员属性是否可用取决于多维数据集定义。 下列属性表示与多维数据集中的维度级别有关的信息。
SOLVE_ORDER | 在一个计算成员引用另一个计算成员（即计算成员相交）的情况下，计算成员的求解次序。  
---|---  
FORMAT_STRING | 客户端应用程序在显示单元格值时可以使用的 Office 样式格式字符串。  
VISIBLE | 指示计算成员在架构行集中是否可见的值。 可以使用 AddCalculatedMembers 函数将可见计算成员添加到集中。 非零值表示计算成员可见。 此属性的默认值为 _Visible_ 。 不可见（此值设置为零时）的计算成员通常用作更复杂的计算成员中的中间步骤。 这些计算成员也可以由其他类型的成员（如度量值）引用。  
NON_EMPTY_BEHAVIOR | 解析空单元时，用来确定计算成员的行为的度量值或集。 ****警告**** 此属性已弃用。 避免将其设置。 有关详细信息，请参阅 SQL Server 2014 中弃用的 Analysis Services 功能。  
CAPTION | 客户端应用程序用作成员标题的字符串。  
DISPLAY_FOLDER | 标识客户端应用程序用来显示成员的显示文件夹路径的字符串。 文件夹级别的分隔符由客户端应用程序定义。 对于 Analysis Services 提供的工具和客户端，反斜杠 (\\) 是级别分隔符。 若要为定义的成员提供多个显示文件夹，请使用分号 (;) 分隔文件夹。  
ASSOCIATED_MEASURE_GROUP | 与此成员关联的度量值组的名称。  
DROP MEMBER 语句 (MDX) UPDATE MEMBER 语句 (MDX) MDX 数据定义语句 (MDX)
1月27日 15时 - 1月27日 15时 


