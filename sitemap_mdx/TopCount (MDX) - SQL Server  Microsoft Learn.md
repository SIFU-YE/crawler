#### 通过
# TopCount (MDX)
按降序对集进行排序，并返回指定数目的最大值元素。
```
  
TopCount(Set_Expression,Count [ ,Numeric_Expression ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Count_ 指定要返回的元组数的有效数值表达式。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
如果指定了数值表达式， **则 TopCount** 函数会根据数值表达式指定的值对指定集指定的集中元组进行降序排序，对指定的集进行计算。 对集进行排序后， **TopCount** 函数随后返回具有最大值的指定数量的元组。
与 BottomCount 函数一样， **TopCount** 函数始终会中断层次结构。
如果未指定数值表达式，则函数将按自然顺序返回成员集，而无需进行任何排序，其行为类似于 Head (MDX)  函数。
下面的示例按 Internet Sales Amount 返回前 10 个日期：
```
SELECT [Measures].[Internet Sales Amount] ON 0,  
TOPCOUNT([Date].[Date].[Date].MEMBERS, 10, [Measures].[Internet Sales Amount])  
ON 1  
FROM [Adventure Works]  

```

下面的示例返回 Bike 类别包含 Geography 维度中 Geography 层次结构的 City 级别的所有成员组合的集中的前五个成员，并按照 Reseller Sales Amount 度量值进行排序（从成员集中销售额最高的成员开始）。
```
SELECT [Measures].[Reseller Sales Amount] ON 0,  
TopCount  
   ({[Geography].[Geography].[City].Members   
      *[Date].[Fiscal].[Fiscal Year].Members}  
   , 5  
   , [Measures].[Reseller Sales Amount]  
   ) ON 1  
FROM [Adventure Works]  
WHERE([Product].[Product Categories].Bikes)  

```

1月27日 15时 - 1月27日 15时 


