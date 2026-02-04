#### 通过
# Rank (MDX)
返回指定元组在指定集中的排名（从 1 开始）。
```
  
Rank(Tuple_Expression, Set_Expression [ ,Numeric Expression ] )  

```

_Tuple_Expression_ 返回元组的有效多维表达式 (MDX)。
_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
如果指定了数值表达式， **则 Rank** 函数将通过针对元组计算指定的数值表达式来确定指定元组的从 1 开始的排名。 如果指定了数值表达式， **则 Rank** 函数会将相同的排名分配给集中具有重复值的元组。 为值相同的元组分配相同的排名，会影响该集中后续元组的排名。 例如，由以下元组组成的集：`{(a,b), (e,f), (c,d)}`。 元组 `(a,b)` 与元组 `(c,d)` 具有相同的值。 如果元组 `(a,b)` 的排名为 1，则 `(a,b)` 和 `(c,d)` 的排名都为 1。 但元组 `(e,f)` 的排名为 3。 此集中可能没有排名为 2 的元组。
如果未指定数值表达式， **则 Rank** 函数将返回指定元组的从 1 开始的序号位置。
**Rank** 函数不对集进行排序。
以下示例通过使用 **Filter** 、 **NonEmpty** 、 **Item** 和 **Rank** 函数查找每个客户购买的最后一个日期，返回包含客户和购买日期的元组集。
```
WITH SET MYROWS AS FILTER  
   (NONEMPTY  
      ([Customer].[Customer Geography].MEMBERS  
         * [Date].[Date].[Date].MEMBERS  
         , [Measures].[Internet Sales Amount]  
      ) AS MYSET  
   , NOT(MYSET.CURRENT.ITEM(0)  
      IS MYSET.ITEM(RANK(MYSET.CURRENT, MYSET)).ITEM(0))  
   )  
SELECT [Measures].[Internet Sales Amount] ON 0,  
MYROWS ON 1  
FROM [Adventure Works]  

```

以下示例使用 **Order** 函数（而不是 **Rank** 函数）根据“经销商销售额”度量值对 City 层次结构的成员进行排名，然后按排名顺序显示它们。 通过使用 **Order** 函数先对 City 层次结构的成员集进行排序，排序只需执行一次，然后进行线性扫描，然后再按排序顺序显示。
```
WITH   
SET OrderedCities AS Order  
   ([Geography].[City].[City].members  
   , [Measures].[Reseller Sales Amount], BDESC  
   )  
MEMBER [Measures].[City Rank] AS Rank  
   ([Geography].[City].CurrentMember, OrderedCities)  
SELECT {[Measures].[City Rank],[Measures].[Reseller Sales Amount]}  ON 0   
,Order  
   ([Geography].[City].[City].MEMBERS  
   ,[City Rank], ASC)  
    ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


