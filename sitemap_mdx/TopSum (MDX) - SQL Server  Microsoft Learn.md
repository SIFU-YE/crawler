#### 通过
# TopSum (MDX)
对集进行排序并返回累计合计至少达到指定值的最前面的元素。
```
  
TopSum(Set_Expression, Value, Numeric_Expression)   

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_值_ 指定与每个元组相比较的值的有效数值表达式。
_Numeric_Expression_ 返回度量值的有效数值表达式，通常是多维表达式 (MDX)。
**TopSum** 函数计算对指定集计算的指定度量值的总和，并按降序对集进行排序。 然后，该函数返回最大值元素，其指定数值表达式的合计至少为指定值。 此函数返回集的最小子集，其累积合计至少为指定值。 返回的元素按从大到小的顺序排序。
与 BottomSum 函数一样， **TopSum** 函数始终会打破层次结构。
下面的示例返回 Geography 维度中 Geography 层次结构内 City 级别的最小成员集（对于 Bike 类别），使用 Reseller Sales Amount 度量值时该集的累积合计至少为 6,000,000（从集中具有最大销售额的成员开始）。
```
SELECT [Measures].[Reseller Sales Amount] ON 0,  
TopSum  
   ({[Geography].[Geography].[City].Members}  
   , 6000000  
   , [Measures].[Reseller Sales Amount]  
   ) ON 1  
FROM [Adventure Works]  
WHERE([Product].[Product Categories].Bikes)  

```

1月27日 15时 - 1月27日 15时 


