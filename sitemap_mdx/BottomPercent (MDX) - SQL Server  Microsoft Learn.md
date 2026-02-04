#### 通过
# BottomPercent (MDX)
按升序对集进行排序，并返回一个最小值元组集，该元组集的累积合计等于或大于指定的百分比。
```
  
BottomPercent(Set_Expression, Percentage, Numeric_Expression)   

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_百分比_ 一个有效的数值表达式，指定要返回的元组的百分比。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
**BottomPercent** 函数计算对指定集计算的指定数值表达式的总和，并按升序对集进行排序。 然后，该函数返回合计值累积百分比至少达到指定百分比的最小值元素。 该函数返回累积合计至少达到指定百分比的最小子集。 返回的元素按从大到小的顺序排序。
**与 TopPercent** 函数一样，BottomPercent 函数始终会中断层次结构。 有关详细信息，请参阅 Order 函数。
下面的示例返回 2003 会计年度 Geography 维度 Geography 层次结构中 City 级别的最小成员集（对于 Bike 类别），其 Reseller Sales Amount 度量值的累积合计至少是累积合计的 15%（从具有最小销售额的集的成员开始）。
```
SELECT  
[Product].[Product Categories].Bikes ON 0,  
BottomPercent  
   ({[Geography].[Geography].[City].Members}  
   , 15  
   , ([Measures].[Reseller Sales Amount],[Product].[Product Categories].Bikes)  
   ) ON 1  
FROM [Adventure Works]  
WHERE ([Measures].[Reseller Sales Amount],[Date].[Fiscal].[Fiscal Year].[FY 2003])  

```

1月27日 15时 - 1月27日 15时 


