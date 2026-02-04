#### 通过
# IIf (MDX)
根据布尔条件为 true 还是 false，计算不同的分支表达式。
```
  
IIf(Logical_Expression, Expression1 [HINT <hints>], Expression2 [HINT <hints>])  

```

IIf 函数采用三个参数：iif (<condition>， <然后分支>， <else branch>) 。
_Logical_Expression_ 计算结果为 **true** (1) 或 **false** (0) 的条件。 它必须是有效的多维表达式 (MDX) 逻辑表达式。
_Expression1 提示 [Eager|严格 |延迟]]_ 当逻辑表达式的计算结果为 **true** 时使用。 Expression1 必须是有效的多维表达式 (MDX) 表达式。
_Expression2 提示 [Eager|严格 |延迟]]_ 当逻辑表达式的计算结果为 **false** 时使用。 Expression2 必须是有效的多维表达式 (MDX) 表达式。
当此表达式的值为零时，逻辑表达式指定的条件的计算结果为 **false** 。 任何其他值的计算结果为 **true** 。
条件为 **true** 时， **IIf** 函数将返回第一个表达式。 否则，该函数返回第二个表达式。
指定的表达式可以返回值或 MDX 对象。 此外，指定表达式的类型无需匹配。
不建议使用 **IIf** 函数基于搜索条件创建一组成员。 相反，使用 Filter 函数根据逻辑表达式计算指定集中的每个成员，并返回成员的子集。
如果任意一个表达式的计算结果为 NULL，则当满足该条件时，结果集为 NULL。
提示是一个可选修饰符，用于决定如何以及何时计算表达式。 它允许您通过指定计算表达式的方式来覆盖默认查询计划。
  * EAGER 针对原始 IIF 子空间计算表达式。
  * STRICT 仅在逻辑条件表达式创建的受限制子空间中计算表达式。
  * LAZY 在逐个单元的模式下计算表达式。


EAGER 和 STRICT 仅应用于 IIF 的 then-else 分支，LAZY 则应用于所有 MDX 表达式。 任意 MDX 表达式可以后跟 HINT LAZY，后者在逐个单元的模式下计算该表达式。
在提示中，EAGER 和 STRICT 是互斥的；可以在不同表达式的相同 IIF(,,) 中使用它们。
有关详细信息，请参阅 SQL Server Analysis Services 2008 中的 IIF 函数查询提示和 MDX IIF 函数和 CASE 语句的执行计划和计划提示。
以下查询显示了在计算度量值 Internet Sales Amount 大于或小于 $10000 时，在计算度量值内简单使用 **IIF** 以返回两个不同的字符串值之一：
```
WITH MEMBER MEASURES.IIFDEMO AS  
IIF([Measures].[Internet Sales Amount]>10000  
, "Sales Are High", "Sales Are Low")  
SELECT {[Measures].[Internet Sales Amount],MEASURES.IIFDEMO} ON 0,  
[Date].[Date].[Date].MEMBERS ON 1  
FROM [Adventure Works]  

```

IIF 的一个常见用法是处理计算度量值中的“除以零”错误，如以下示例所示：
```
WITH  
//Returns 1.#INF when the previous period contains no value  
//but the current period does  
MEMBER MEASURES.[Previous Period Growth With Errors] AS  
([Measures].[Internet Sales Amount]-([Measures].[Internet Sales Amount], [Date].[Date].CURRENTMEMBER.PREVMEMBER))  
/  
([Measures].[Internet Sales Amount], [Date].[Date].CURRENTMEMBER.PREVMEMBER)  
,FORMAT_STRING='PERCENT'  
//Traps division by zero and returns null when the previous period contains  
//no value but the current period does  
MEMBER MEASURES.[Previous Period Growth] AS  
IIF(([Measures].[Internet Sales Amount], [Date].[Date].CURRENTMEMBER.PREVMEMBER)=0,  
NULL,  
([Measures].[Internet Sales Amount]-([Measures].[Internet Sales Amount], [Date].[Date].CURRENTMEMBER.PREVMEMBER))  
/  
([Measures].[Internet Sales Amount], [Date].[Date].CURRENTMEMBER.PREVMEMBER)  
),FORMAT_STRING='PERCENT'  
SELECT {[Measures].[Internet Sales Amount],MEASURES.[Previous Period Growth With Errors], MEASURES.[Previous Period Growth]} ON 0,  
DESCENDANTS(  
[Date].[Calendar].[Calendar Year].&[2004],  
[Date].[Calendar].[Date])  
ON 1  
FROM [Adventure Works]  
WHERE([Product].[Product Categories].[Subcategory].&[26])  

```

下面是 **IIF** 在 Generate 函数内返回两个集之一的示例，以在行上创建一组复杂的元组：
```
SELECT {[Measures].[Internet Sales Amount]} ON 0,  
//If Internet Sales Amount is zero or null  
//returns the current year and the All Customers member  
//else returns the current year broken down by Country  
GENERATE(  
[Date].[Calendar Year].[Calendar Year].MEMBERS  
, IIF([Measures].[Internet Sales Amount]=0,  
{([Date].[Calendar Year].CURRENTMEMBER, [Customer].[Country].[All Customers])}  
, {{[Date].[Calendar Year].CURRENTMEMBER} * [Customer].[Country].[Country].MEMBERS}  
))  
ON 1  
FROM [Adventure Works]  
WHERE([Product].[Product Categories].[Subcategory].&[26])  

```

最后，此示例显示如何使用计划提示：
```
WITH MEMBER MEASURES.X AS  
IIF(  
[Measures].[Internet Sales Amount]=0  
, NULL  
, (1/[Measures].[Internet Sales Amount]) HINT EAGER)  
SELECT {[Measures].x} ON 0,  
[Customer].[Customer Geography].[Country].MEMBERS ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


