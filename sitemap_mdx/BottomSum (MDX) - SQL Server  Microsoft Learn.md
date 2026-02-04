#### 通过
# BottomSum (MDX)
按升序对指定集进行排序，并返回一个最小值元组集，这些元组的和等于或小于指定值。
```
  
BottomSum(Set_Expression, Value, Numeric_Expression)  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_值_ 指定与每个元组相比较的值的有效数值表达式。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
**BottomSum** 函数计算对指定集计算的指定度量值的总和，并按升序对集合进行排序。 然后，此函数返回最小值元素，其指定数值表达式的合计至少为指定值（和）。 此函数返回集的最小子集，其累积合计至少为指定值。 返回的元素按从小到大的顺序排列。
与 TopSum 函数一样，**BottomSum** 函数始终会中断层次结构。
以下示例返回 2003 会计年度 Geography 维度 Geography 层次结构中 City 级别的最小成员集（对于 Bike 类别），其使用 Reseller Sales Amount 度量值的累积合计至少是 50,000（从具有最小销售额的集的成员开始）：
```
SELECT  
[Product].[Product Categories].Bikes ON 0,  
BottomSum  
({[Geography].[Geography].[City].Members}  
, 50000  
, ([Measures].[Reseller Sales Amount],[Product].[Product Categories].Bikes)  
) ON 1  
FROM [Adventure Works]  
WHERE([Measures].[Reseller Sales Amount],[Date].[Fiscal].[Fiscal Year].[FY 2003])  

```

1月27日 15时 - 1月27日 15时 


