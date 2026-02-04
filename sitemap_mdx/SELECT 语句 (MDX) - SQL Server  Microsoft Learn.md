#### 通过
# MDX 数据操作 - SELECT
从指定多维数据集中检索数据。
```
  
[ WITH <SELECT WITH clause>   
   [ , <SELECT WITH clause>...n ]   
]   
SELECT   
     [ *   
    | ( <SELECT query axis clause>   
                  [ , <SELECT query axis clause>,...n ]   
            )   
            ]  
FROM   
   <SELECT subcube clause>   
      [ <SELECT slicer axis clause> ]  
      [ <SELECT cell property list clause> ]  
  
<SELECT WITH clause> ::=  
     ( CELL CALCULATION <CREATE CELL CALCULATION body clause> )   
   | ( [ CALCULATED ] MEMBER <CREATE MEMBER body clause>)   
   | ( SET <CREATE SET body clause>)  
   | ( MEASURE = <measure body clause> )  
  
<SELECT query axis clause> ::=  
   [ NON EMPTY ] Set_Expression  
   [ <SELECT dimension property list clause> ]   
      ON   
            Integer_Expression   
       | AXIS(Integer)   
       | COLUMNS   
       | ROWS   
       | PAGES   
       | SECTIONS   
       | CHAPTERS   
  
<SELECT subcube clause> ::=  
      Cube_Name   
   | [NON VISUAL] (SELECT   
                  [ *   
       | ( <SELECT query axis clause> [ ,   
           <SELECT query axis clause>,...n ] )   
         ]   
            FROM   
         <SELECT subcube clause>   
         <SELECT slicer axis clause> )  
  
<SELECT slicer axis clause> ::=   
      WHERE Tuple_Expression  
  
<SELECT cell property list clause> ::=   
   [ CELL ] PROPERTIES CellProperty_Name   
      [ , CellProperty_Name,...n ]  
  
<SELECT dimension property list clause> ::=  
   [DIMENSION] PROPERTIES   
      (DimensionProperty_Name   
         [,DimensionProperty_Name,...n ] )   
    | (LevelProperty_Name   
         [, LevelProperty_Name,...n ] )   
    | (MemberProperty_Name   
         [, MemberProperty_Name,...n ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_整数_ 一个介于 0 和 127 之间的整数。
_Cube_Name_ 提供多维数据集名称的有效字符串。
_Tuple_Expression_ 返回元组的有效多维表达式 (MDX)。
_CellProperty_Name_ 表示单元属性的有效字符串。
_DimensionProperty_Name_ 表示维度属性的有效字符串。
_LevelProperty_Name_ 表示级别属性的有效字符串。
_MemberProperty_Name_ 表示成员属性的有效字符串。
`<SELECT slicer axis clause>` 表达式必须包含维度和层次结构中的成员，而不是包含指定的 `<SELECT query axis clause>` 表达式中所引用的成员。
如果指定的 `<SELECT query axis clause>` 表达式和 `<SELECT slicer axis clause>` 值中省略了多维数据集中的某个属性，则该属性的默认成员将隐式添加到切片器轴中。
使用 subselect 语句中的 NON VISUAL 选项，可以筛选出成员，同时保留实际总数，而不是筛选出的总数。 这样，您可以查询前十位的销售（人员/产品/地区），并获取所有查询成员的实际销售总数，而不是返回的前十位的销售总数。 有关详细信息，请参阅下面的示例。
每当使用连接字符串参数 _subqueries=1_ 打开连接时，计算成员都可以包含在 SELECT 查询轴子句>中<;有关参数用法，请参阅支持的 XMLA 属性 (XMLA)  和 ConnectionString 。 下面是有关嵌套 select 语句中的计算成员的示例。
## Autoexists
在 SELECT 语句中使用维度的两个或更多属性时，Analysis Services 会计算这些属性的表达式，以确保这些属性的成员得到适当限制，使它们满足所有其他属性的条件。 例如，假定您在处理来自 Geography 维度的属性。 如果你有一个表达式从 City 属性返回所有成员，而另一个表达式将 Country 属性中的成员限制为欧洲所有国家/地区，则这将导致 City 成员仅限于属于欧洲国家/地区的那些城市。 Analysis Services 的这一特性称为 Autoexists，并且仅适用于同一维度内的属性。 Autoexists 仅适用于同一维度中的属性，因为它试图阻止在一个属性表达式中排除的维度记录被包括在其他属性表达式中。 也可以将 Autoexists 理解为不同的属性表达式产生的维度记录的交集。 请参阅下面的以下示例：
```
//Obtain the Top 10 best reseller selling products by Name  
with member [Measures].[PCT Discount] AS '[Measures].[Discount Amount]/[Measures].[Reseller Sales Amount]', FORMAT_STRING = 'Percent'  
set Top10SellingProducts as 'topcount([Product].[Model Name].children, 10, [Measures].[Reseller Sales Amount])'  
set Preferred10Products as '  
{[Product].[Model Name].&[Mountain-200],  
[Product].[Model Name].&[Road-250],  
[Product].[Model Name].&[Mountain-100],  
[Product].[Model Name].&[Road-650],  
[Product].[Model Name].&[Touring-1000],  
[Product].[Model Name].&[Road-550-W],  
[Product].[Model Name].&[Road-350-W],  
[Product].[Model Name].&[HL Mountain Frame],  
[Product].[Model Name].&[Road-150],  
[Product].[Model Name].&[Touring-3000]  
}'  
select {[Measures].[Reseller Sales Amount], [Measures].[Discount Amount], [Measures].[PCT Discount]} on 0,  
Top10SellingProducts on 1  
from [Adventure Works]  

```

获得的结果集如下：
模型名称 + 度量值 | Reseller Sales Amount | Discount Amount | PCT Discount  
---|---|---|---  
**Mountain-200** |  **$14,356,699.36** |  **$19,012.71**  
**Road-250** |  **$9,377,457.68** |  **$4,032.47**  
**Mountain-100** |  **$8,568,958.27** |  **$139,393.27**  
**Road-650** |  **$7,442,141.81** |  **$39,698.30**  
**Touring-1000** |  **$6,723,794.29** |  **$166,144.17**  
**Road-550-W** |  **$3,668,383.88** |  **$1,901.97**  
**Road-350-W** |  **$3,665,932.31** |  **$20,946.50**  
**HL Mountain Frame** |  **$3,365,069.27** |  **$174.11**  
**Road-150** |  **$2,363,805.16**  
**Touring-3000** |  **$2,046,508.26** |  **$79,582.15**  
获得的产品集似乎与 Preferred10Products 相同；因此，请验证 Preferred10Products 集：
```
with member [Measures].[PCT Discount] AS '[Measures].[Discount Amount]/[Measures].[Reseller Sales Amount]', FORMAT_STRING = 'Percent'  
set Top10SellingProducts as 'topcount([Product].[Model Name].children, 10, [Measures].[Reseller Sales Amount])'  
set Preferred10Products as '  
{[Product].[Model Name].&[Mountain-200],  
[Product].[Model Name].&[Road-250],  
[Product].[Model Name].&[Mountain-100],  
[Product].[Model Name].&[Road-650],  
[Product].[Model Name].&[Touring-1000],  
[Product].[Model Name].&[Road-550-W],  
[Product].[Model Name].&[Road-350-W],  
[Product].[Model Name].&[HL Mountain Frame],  
[Product].[Model Name].&[Road-150],  
[Product].[Model Name].&[Touring-3000]  
}'  
select {[Measures].[Reseller Sales Amount], [Measures].[Discount Amount], [Measures].[PCT Discount]} on 0,  
Preferred10Products on 1  
from [Adventure Works]  

```

根据以下结果，两个产品集（Top10SellingProducts 和 Preferred10Products）是相同的
模型名称 + 度量值 | Reseller Sales Amount | Discount Amount | PCT Discount  
---|---|---|---  
**Mountain-200** |  **$14,356,699.36** |  **$19,012.71**  
**Road-250** |  **$9,377,457.68** |  **$4,032.47**  
**Mountain-100** |  **$8,568,958.27** |  **$139,393.27**  
**Road-650** |  **$7,442,141.81** |  **$39,698.30**  
**Touring-1000** |  **$6,723,794.29** |  **$166,144.17**  
**Road-550-W** |  **$3,668,383.88** |  **$1,901.97**  
**Road-350-W** |  **$3,665,932.31** |  **$20,946.50**  
**HL Mountain Frame** |  **$3,365,069.27** |  **$174.11**  
**Road-150** |  **$2,363,805.16**  
**Touring-3000** |  **$2,046,508.26** |  **$79,582.15**  
在上面的示例中，我们创建了两个集：一个作为计算表达式，另一个作为常量表达式。 这些示例阐释了 Autoexists 的不同风格。
可以对表达式进行 Autoexists 深度或浅表应用。 默认设置为 deep。 下面的示例将阐释深度 Autoexists 的概念。 在该示例中，我们将依据 [Product].[Product Line] 属性对 [Mountain] 组中的产品筛选 Top10SellingProducts。 请注意两个属性（slicer 和 axis）均属于同一维度 [Product]。
```
with member [Measures].[PCT Discount] AS '[Measures].[Discount Amount]/[Measures].[Reseller Sales Amount]', FORMAT_STRING = 'Percent'  
set Top10SellingProducts as 'topcount([Product].[Model Name].children, 10, [Measures].[Reseller Sales Amount])'  
// Preferred10Products set removed for clarity  
select {[Measures].[Reseller Sales Amount], [Measures].[Discount Amount], [Measures].[PCT Discount]} on 0,  
Top10SellingProducts on 1  
from [Adventure Works]  
where [Product].[Product Line].[Mountain]  

```

产生以下结果集：
模型名称 + 度量值 | Reseller Sales Amount | Discount Amount | PCT Discount  
---|---|---|---  
**Mountain-200** |  **$14,356,699.36** |  **$19,012.71**  
**Mountain-100** |  **$8,568,958.27** |  **$139,393.27**  
**HL Mountain Frame** |  **$3,365,069.27** |  **$174.11**  
**Mountain-300** |  **$1,907,249.38** |  **$876.95**  
**Mountain-500** |  **$1,067,327.31** |  **$17,266.09**  
**Mountain-400-W** |  **$592,450.05** |  **$303.49**  
**LL Mountain Frame** |  **$521,864.42** |  **$252.41**  
**ML Mountain Frame-W** |  **$482,953.16** |  **$206.95**  
**ML Mountain Frame** |  **$343,785.29** |  **$161.82**  
**Women's Mountain Shorts** |  **$260,304.09** |  **$6,675.56**  
在前面的结果集中，我们看到 Top10SellingProducts 列表中有七种新产品，并且 Mountain-200、Mountain-100 和 HL Mountain Frame 移到了列表顶部。 在前面的结果集中，这三个值是混杂的。
这称为深度 Autoexists，因为对 Top10SellingProducts 集进行计算以符合查询的切片条件。 深度 Autoexists 意味着将对所有表达式进行计算，以便在应用了切片器表达式、轴中的嵌套 select 表达式等后到达可能的最深空间。
不过，有人可能希望能够对与 Preferred10Products 等效的 Top10SellingProducts 进行分析，如下面的示例所示：
```
with member [Measures].[PCT Discount] AS '[Measures].[Discount Amount]/[Measures].[Reseller Sales Amount]', FORMAT_STRING = 'Percent'  
set Top10SellingProducts as 'topcount([Product].[Model Name].children, 10, [Measures].[Reseller Sales Amount])'  
set Preferred10Products as '  
{[Product].[Model Name].&[Mountain-200],  
[Product].[Model Name].&[Road-250],  
[Product].[Model Name].&[Mountain-100],  
[Product].[Model Name].&[Road-650],  
[Product].[Model Name].&[Touring-1000],  
[Product].[Model Name].&[Road-550-W],  
[Product].[Model Name].&[Road-350-W],  
[Product].[Model Name].&[HL Mountain Frame],  
[Product].[Model Name].&[Road-150],  
[Product].[Model Name].&[Touring-3000]  
}'  
select {[Measures].[Reseller Sales Amount], [Measures].[Discount Amount], [Measures].[PCT Discount]} on 0,  
Preferred10Products on 1  
from [Adventure Works]  
where [Product].[Product Line].[Mountain]  

```

产生以下结果集：
模型名称 + 度量值 | Reseller Sales Amount | Discount Amount | PCT Discount  
---|---|---|---  
**Mountain-200** |  **$14,356,699.36** |  **$19,012.71**  
**Mountain-100** |  **$8,568,958.27** |  **$139,393.27**  
**HL Mountain Frame** |  **$3,365,069.27** |  **$174.11**  
在上面的示例中，与预期的一样，切片生成的结果仅包含 Preferred10Products 中属于 [Product].[Product Line] 中的 [Mountain] 组的那些产品，因为 Preferred10Products 是一个常量表达式。
此结果集还可以理解为浅表 Autoexists。 这是因为该表达式是在切片子句之前计算的。 在上面的示例中，出于演示目的以介绍这一概念，该表达式是一个常量表达式。
可以使用 **Autoexists** 连接字符串属性在会话级修改 Autoexists 的行为。 下面的示例先打开一个新会话，然后将 _Autoexists=3_ 属性添加到连接字符串。 必须打开新连接才能执行该示例。 在与 Autoexist 设置建立连接后，设置将一直有效，直到该连接结束。
```
with member [Measures].[PCT Discount] AS '[Measures].[Discount Amount]/[Measures].[Reseller Sales Amount]', FORMAT_STRING = 'Percent'  
set Top10SellingProducts as 'topcount([Product].[Model Name].children, 10, [Measures].[Reseller Sales Amount])'  
//Preferred10Products set removed for clarity  
select {[Measures].[Reseller Sales Amount], [Measures].[Discount Amount], [Measures].[PCT Discount]} on 0,  
Top10SellingProducts on 1  
from [Adventure Works]  
where [Product].[Product Line].[Mountain]  

```

下面的结果集现在显示 Autoexists 的浅表行为。
模型名称 + 度量值 | Reseller Sales Amount | Discount Amount | PCT Discount  
---|---|---|---  
**Mountain-200** |  **$14,356,699.36** |  **$19,012.71**  
**Mountain-100** |  **$8,568,958.27** |  **$139,393.27**  
**HL Mountain Frame** |  **$3,365,069.27** |  **$174.11**  
可以使用连接字符串中的 AUTOEXISTS=[1|2|3] 参数修改自动存在行为;有关参数用法，请参阅 xmlA) (支持的 XMLA 属性。ConnectionString
以下示例从 **Adventure Works** 多维数据集返回成员的总`Measures.[Order Quantity]`和，该成员在维度中包含的 `Date` 2003 日历年头八个月聚合。
```
WITH MEMBER [Date].[Calendar].[First8Months2003] AS  
    Aggregate(  
        PeriodsToDate(  
            [Date].[Calendar].[Calendar Year],   
            [Date].[Calendar].[Month].[August 2003]  
        )  
    )  
SELECT   
    [Date].[Calendar].[First8Months2003] ON COLUMNS,  
    [Product].[Category].Children ON ROWS  
FROM  
    [Adventure Works]  
WHERE  
    [Measures].[Order Quantity]  

```

为了了解 **NON VISUAL，** 以下示例是 [Adventure Works] 的查询，用于获取表中的 [经销商销售额] 数字，其中产品类别为列，经销商业务类型为行。 请注意，会给出产品和分销商的总数。
以下 SELECT 语句：
```
select [Category].members on 0,  
[Business Type].members on 1  
from [Adventure Works]  
where [Measures].[Reseller Sales Amount]  

```

产生以下结果：
业务类型 + 类别 | All Products | Accessories | Bikes | 服装 | 部件  
---|---|---|---|---|---  
**All Resellers** |  **$80,450,596.98** |  **$571,297.93** |  **$66,302,381.56** |  **$1,777,840.84** |  **$11,799,076.66**  
**Specialty Bike Shop** |  **$6,756,166.18** |  **$65,125.48** |  **$6,080,117.73** |  **$252,933.91** |  **$357,989.07**  
**Value Added Reseller** |  **$34,967,517.33** |  **$175,002.81** |  **$30,892,354.33** |  **$592,385.71** |  **$3,307,774.48**  
**$38,726,913.48** |  **$331,169.64** |  **$29,329,909.50** |  **$932,521.23** |  **$8,133,313.11**  
若要生成一个表，其中包含仅针对Accessories 和 Clothing 产品、增值经销商和仓库经销商的数据，但保留总体总计，可以使用 NON VISUAL 编写如下：
```
select [Category].members on 0,  
[Business Type].members on 1  
from NON VISUAL (Select {[Category].Accessories, [Category].Clothing} on 0,  
{[Business Type].[Value Added Reseller], [Business Type].[Warehouse]} on 1  
from [Adventure Works])  
where [Measures].[Reseller Sales Amount]  

```

产生以下结果：
业务类型 + 类别 | All Products | Accessories | Clothing  
---|---|---|---  
**All Resellers** |  **$80,450,596.98** |  **$571,297.93** |  **$1,777,840.84**  
**Value Added Reseller** |  **$34,967,517.33** |  **$175,002.81** |  **$592,385.71**  
**$38,726,913.48** |  **$331,169.64** |  **$932,521.23**  
要生成一个表，其中列是进行直观加和，对于行总数则是所有 [类别] 的实际总和，应发出以下查询：
```
select [Category].members on 0,  
[Business Type].members on 1  
from NON VISUAL (Select {[Category].Accessories, [Category].Clothing} on 0  
from ( Select {[Business Type].[Value Added Reseller], [Business Type].[Warehouse]} on 0  
from [Adventure Works])  
)  
where [Measures].[Reseller Sales Amount]  

```

请注意，NON VISUAL 仅应用到 [Category]。
上述查询产生以下结果：
业务类型 + 类别 | All Products | Accessories | Clothing  
---|---|---|---  
All Resellers | $73,694,430.80 | $506,172.45 | $1,524,906.93  
Value Added Reseller | $34,967,517.33 | $175,002.81 | $592,385.71  
Warehouse | $38,726,913.48 | $331,169.64 | $932,521.23  
与上述结果比较时，您可以观察到 [All Resellers] 行现在是将 [Value Added Reseller] 和 [Warehouse] 仓库的显示值相加，但 [All Products] 列会显示所有产品的总值，包括那些未显示的值。
下面的示例说明如何使用嵌套 select 中的计算成员来筛选值。 若要重现此示例，必须使用连接字符串参数 _subqueries=1_ 建立连接。
```
select Measures.allmembers on 0  
from (  
Select { [Measures].[Reseller Sales Amount]  
, [Measures].[Reseller Total Product Cost]  
, [Measures].[Reseller Gross Profit]  
, [Measures].[Reseller Gross Profit Margin]  
} on 0  
from [Adventure Works]  
)  

```

上述查询产生以下结果：
Reseller Sales Amount | Reseller Total Product Cost | Reseller Gross Profit | Reseller Gross Profit Margin  
---|---|---|---  
$80,450,596.98 | $79，980，114.38 | $470，482.60 | 0.58%  
MDX 中的重要概念 (Analysis Services) MDX 数据操作语句 (MDX) 用查询轴和切片器轴限定查询 (MDX)
1月27日 15时 - 1月27日 15时 


