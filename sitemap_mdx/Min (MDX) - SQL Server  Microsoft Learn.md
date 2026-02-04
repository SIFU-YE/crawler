#### 通过
# Min (MDX)
返回对集求值的数值表达式的最小值。
```
  
Min( Set_Expression [ , Numeric_Expression ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
如果指定了数值表达式，则指定的数值表达式对集求值，然后返回该求值的最小值。 如果未指定数值表达式，则在指定集的成员的当前上下文中对该集求值，然后该求值的最小值。
Analysis Services 在计算一组数字中的最小值时忽略 null。
下面的示例返回 Adventure Works 多维数据集中每个子类别和国家/地区的最小季度销售额。
```
WITH MEMBER Measures.x AS Min   
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


