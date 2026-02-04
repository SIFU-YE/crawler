#### 通过
# Max (MDX)
返回对集求值的数值表达式的最大值。
```
  
Max( Set_Expression [ , Numeric_Expression ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
如果指定了数值表达式，则对集计算指定数值表达式的值，然后返回求得的最大值。 如果没有指定数值表达式，则在指定集成员的当前上下文中计算指定集，然后返回求得的最大值。
Analysis Services 在计算一组数字中的最大值时忽略 null。
以下示例返回 Adventure Works 多维数据集中每个季度、子类别和国家/地区的最大月销售额。
```
WITH MEMBER Measures.x AS Max   
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


