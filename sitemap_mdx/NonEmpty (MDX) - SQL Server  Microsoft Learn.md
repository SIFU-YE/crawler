#### 通过
# NonEmpty (MDX)
根据第一个指定集与第二个集的叉积，返回指定集中的非空元组集。
```
  
NONEMPTY(set_expression1 [,set_expression2])  

```

_set_expression1_ 返回集的有效多维表达式 (MDX)。
_set_expression2_ 返回集的有效多维表达式 (MDX)。
此函数返回位于第一个指定集中并且在对第二个集中的元组求值时不为空的元组。 **NonEmpty** 函数会考虑计算并保留重复元组。 如果未提供第二个集，将在多维数据集中属性层次结构和度量值的成员的当前坐标上下文中对表达式求值。
使用此函数，而不是弃用的 NonEmptyCrossjoin (MDX)  函数。
非空是元组所引用的单元的特征，而不是元组本身的特征。
以下查询显示了 **一个非空的** 简单示例，返回 2001 年 7 月 1 日 Internet Sales Amount 的非 null 值的所有客户：
```
SELECT [Measures].[Internet Sales Amount] ON 0,  
NONEMPTY(  
[Customer].[Customer].[Customer].MEMBERS  
, {([Date].[Calendar].[Date].&[20010701], [Measures].[Internet Sales Amount])}  
)  
ON 1  
FROM [Adventure Works]  

```

以下示例返回包含客户和购买日期的元组集，使用 **Filter** 函数和 **NonEmpty** 函数查找每个客户购买的最后一个日期：
```
WITH SET MYROWS AS FILTER  
(NONEMPTY  
([Customer].[Customer Geography].[Customer].MEMBERS  
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

DefaultMember (MDX) Filter (MDX) IsEmpty (MDX) MDX 函数参考 (MDX) NonEmptyCrossjoin (MDX)
1月27日 15时 - 1月27日 15时 


