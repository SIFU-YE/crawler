#### 通过
# TopPercent (MDX)
按降序对集进行排序，并返回一个最大值元组集，该元组集的累积合计等于或大于指定的百分比。
```
  
TopPercent(Set_Expression, Percentage, Numeric_Expression)   

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_百分比_ 一个有效的数值表达式，指定要返回的元组的百分比。
_百分比_ 需要为正值;负值生成错误。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
**TopPercent** 函数计算对指定集计算的指定数值表达式的总和，并按降序对集进行排序。 然后，该函数返回具有最高值的元素，其总合计值的累积百分比至少是指定的百分比。 该函数返回累积合计至少达到指定百分比的最小子集。 返回的元素按从大到小的顺序排序。
如果 _Numeric_Expression_ 返回任何负值，则 **TopPercent** 仅返回一 (1) 行。
请参阅针对此行为的详细演示的第二个示例。
与 BottomPercent 函数一样， **TopPercent** 函数始终会打破层次结构。
### A. 返回 TopPercent
下面的示例返回对于“自行车”类别，帮助实现前 10% 的分销商销售额的最佳城市。 结果将按降序排序，并且从具有最高销售额的城市开始。
```
SELECT [Measures].[Reseller Sales Amount] ON 0,  
TopPercent  
   ({[Geography].[Geography].[City].Members}  
   , 10  
   , [Measures].[Reseller Sales Amount]  
   ) ON 1  
FROM [Adventure Works]  
WHERE([Product].[Product Categories].[Bikes])  

```

上面的表达式生成以下结果：
城市 | Reseller Sales Amount  
---|---  
Toronto | $3，508，904.84  
London | $1，521，530.09  
Seattle | $1，209，418.16  
Paris | $1，170，425.18  
使用下面的查询可以获取原始数据集，并返回 588 行：
```
SELECT [Measures].[Reseller Sales Amount] ON 0,  
Order  
   ({[Geography].[Geography].[City].Members}  
   , [Measures].[Reseller Sales Amount]  
   , BDESC  
   ) ON 1  
FROM [Adventure Works]  
WHERE([Product].[Product Categories].[Bikes])  
  

```

以下演练将有助于了解负值在 _Numeric_Expression_ 的影响。 首先，将生成一些可展示该行为的上下文。
下面的查询将返回一个表，由分销商的“Sales Amount”、“Total Product Cost”和“Gross Profit”构成，并且按利润的降序排序。 请注意，对于利润仅存在负值；因此，最小的利润损失将出现在最顶部。
```
SELECT { [Measures].[Reseller Sales Amount], [Measures].[Reseller Total Product Cost], [Measures].[Reseller Gross Profit] } ON columns  
     ,  ORDER( [Product].[Product Categories].[Bikes].[Touring Bikes].children, [Measures].[Reseller Gross Profit], BDESC )   ON rows  
FROM [Adventure Works]  
  

```

上述查询会返回以下结果；为便于阅读，中间部分的行已删除。
观光自行车 | Reseller Sales Amount | Reseller Total Product Cost | Reseller Gross Profit  
---|---|---|---  
Touring-2000 Blue, 50 | $157，444.56 | $163，112.57 |  ($5，668.01)   
Touring-2000 Blue， 46 | $321，027.03 | $333，021.50 |  ($11，994.47)   
Touring-3000 Blue, 62 | $87，773.61 | $100，133.52 |  ($12，359.91)   
... | ... | ... | ...  
Touring-1000 黄色， 46 | $1，016，312.83 | $1，234，454.27 |  ($218，141.44)   
Touring-1000 Yellow, 60 | $1，184，363.30 | $1，443，407.51 |  ($259，044.21)   
现在，如果要求您按利润展示前 100% 的自行车，则编写如下查询：
```
SELECT { [Measures].[Reseller Sales Amount], [Measures].[Reseller Total Product Cost], [Measures].[Reseller Gross Profit] } ON columns  
     ,  TOPPERCENT( [Product].[Product Categories].[Bikes].[Touring Bikes].children, 100,[Measures].[Reseller Gross Profit] )   ON rows  
FROM [Adventure Works]  
  

```

请注意，查询要求百分之百 (100%)；这意味着应返回所有行。 但是，由于 _Numeric_Expression_ 中存在负值，因此仅返回一行。
观光自行车 | Reseller Sales Amount | Reseller Total Product Cost | Reseller Gross Profit  
---|---|---|---  
Touring-2000 Blue, 50 | $157，444.56 | $163，112.57 |  ($5，668.01)   
1月27日 15时 - 1月27日 15时 


