#### 通过
# BottomCount (MDX)
按升序对集进行排序，并返回指定集中具有最小值的指定数目的元组。
```
  
BottomCount(Set_Expression, Count [,Numeric_Expression])  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Count_ 指定要返回的元组数的有效数值表达式。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
如果指定了数值表达式，则此函数根据在指定集中计算出的指定数值表达式的值，对指定集中的元组按升序进行排序。 然后 **，BottomCount** 函数返回具有最小值的指定数量的元组。
**与 TopCount** 函数一样，BottomCount 函数始终会中断层次结构。
如果未指定数值表达式，则函数将按自然顺序返回成员集，而不进行任何排序，其行为类似于 Tail (MDX)  函数。
下例将返回每个日历年中最后五个“产品子类别”销售额的“分销商订单数量”度量值，并根据“分销商销售额”度量值进行排序。
```
SELECT BottomCount([Product].[Product Categories].[Subcategory].Members  
   , 10  
   , [Measures].[Reseller Sales Amount]) ON 0,  
   [Date].[Calendar].[Calendar Year].Members ON 1  
  
FROM  
    [Adventure Works]  
WHERE  
    [Measures].[Reseller Order Quantity]  

```

1月27日 15时 - 1月27日 15时 


