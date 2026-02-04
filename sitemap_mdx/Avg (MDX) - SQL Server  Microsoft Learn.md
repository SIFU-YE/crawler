#### 通过
# Avg (MDX)
对集求值，并返回该集中的单元的非空值的平均值，此平均值是对该集中的度量值或指定度量值求得的平均值。
```
  
Avg( Set_Expression [ , Numeric_Expression ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
如果指定了一组空元组或空集， **Avg** 函数将返回一个空值。
**Avg** 函数计算指定集中单元格非空值的平均值，方法是先计算指定集中各单元格的值之和，然后将计算所得的总和除以指定集中非空单元格的计数。
Analysis Services 在计算一组数字中的平均值时会忽略 null。
如果特定的数值表达式 (通常未指定度量值) ， **则 Avg** 函数会对当前查询上下文中的每个度量值求平均值。 如果提供了特定度量值， **则 Avg** 函数首先对集的度量值求值，然后函数根据指定的度量值计算平均值。
在计算成员语句中使用 **CurrentMember** 函数时，必须指定数值表达式，因为此类查询上下文中不存在当前坐标的默认度量值。
若要强制包含空单元格，应用程序必须使用 CoalesceEmpty 函数或指定一个有效的 _Numeric_Expression_ ，该函数为空值提供零 (0) 。 有关空单元的详细信息，请参阅 OLE DB 文档。
下面的示例对指定集返回度量值的平均值。 请注意，指定度量值可以是指定集的成员的默认度量值，也可以是指定的度量值。
```
WITH SET [NW Region] AS  
{[Geography].[State-Province].[Washington]  
, [Geography].[State-Province].[Oregon]  
, [Geography].[State-Province].[Idaho]}  
MEMBER [Geography].[Geography].[NW Region Avg] AS  
AVG ([NW Region]  
--Uncomment the line below to get an average by Reseller Gross Profit Margin  
--otherwise the average will be by whatever the default measure is in the cube,  
--or whatever measure is specified in the query  
--, [Measures].[Reseller Gross Profit Margin]  
)  
SELECT [Date].[Calendar Year].[Calendar Year].Members ON 0  
FROM [Adventure Works]  
WHERE ([Geography].[Geography].[NW Region Avg])  

```

以下示例从 **Adventure Works** 多维数据集返回度量值的`Measures.[Gross Profit Margin]`每日平均值，该平均值在 2003 会计年度中每个月的天数中计算得出。 **Avg** 函数计算层次结构每个月中包含的天数集的`[Ship Date].[Fiscal Time]`平均值。 第一种形式的计算演示 Avg 将未记录任何销售额的天数从平均值计算中排除的默认行为，第二种形式的计算演示如何将没有销售额的天数包含在平均值计算中。
```
WITH MEMBER Measures.[Avg Gross Profit Margin] AS  
Avg(  
Descendants(  
[Ship Date].[Fiscal].CurrentMember,  
[Ship Date].[Fiscal].[Date]  
),  
Measures.[Gross Profit Margin]  
), format_String='percent'  
MEMBER Measures.[Avg Gross Profit Margin Including Empty Days] AS  
Avg(  
Descendants(  
[Ship Date].[Fiscal].CurrentMember,  
[Ship Date].[Fiscal].[Date]  
),  
CoalesceEmpty(Measures.[Gross Profit Margin],0)  
), Format_String='percent'  
SELECT  
{Measures.[Avg Gross Profit Margin],Measures.[Avg Gross Profit Margin Including Empty Days]} ON COLUMNS,  
[Ship Date].[Fiscal].[Fiscal Year].Members ON ROWS  
FROM  
[Adventure Works]  
WHERE([Product].[Product Categories].[Product].&[344])  

```

以下示例从 **Adventure Works** 多维数据集返回度量值的`Measures.[Gross Profit Margin]`每日平均值，该平均值在 2003 财政年度的每个学期中计算得出。
```
WITH MEMBER Measures.[Avg Gross Profit Margin] AS  
   Avg(  
      Descendants(  
         [Ship Date].[Fiscal].CurrentMember,   
            [Ship Date].[Fiscal].[Date]  
      ),   
      Measures.[Gross Profit Margin]  
   )  
SELECT  
   Measures.[Avg Gross Profit Margin] ON COLUMNS,  
      [Ship Date].[Fiscal].[Fiscal Year].[FY 2003].Children ON ROWS  
FROM  
   [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


