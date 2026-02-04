#### 通过
# Median (MDX)
返回对集求值的数值表达式的中值。
```
  
Median(Set_Expression [ ,Numeric_Expression ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
如果指定了数值表达式，则对集计算指定数值表达式的值，然后返回求得的中值。 如果没有指定数值表达式，则在指定集成员的当前上下文中计算指定集，然后返回求得的中值。
中值是一组有序数值的中间值。 （中值不同于平均值，平均值是一组数值的总和除以这组数值的个数所得的值）。 中值是通过选择最小值以使这组数值中至少有一半值不大于所选的值来确定的。 如果这组数值的个数为奇数，则中值对应于单个值。 如果这组数值的个数为偶数，则中值对应于两个中间值的和除以 2 所得的值。
Analysis Services 在计算一组有序数字中的中值时会忽略 null。
以下示例返回 Adventure Works 多维数据集中每个季度、每个子类别和每个国家/地区的每月销售额中位数。
```
WITH MEMBER Measures.x AS Median   
   ([Date].[Calendar].CurrentMember.Children  
      , [Measures].[Reseller Order Quantity]  
   )  
SELECT Measures.x ON 0  
,NON EMPTY [Date].[Calendar].[Calendar Quarter]*   
   [Product].[Product Categories].[Subcategory].members *  
   [Geography].[Geography].[Country].Members  
ON 1  
FROM [Adventure Works]  
  

```

1月27日 15时 - 1月27日 15时 


