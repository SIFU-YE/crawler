#### 通过
# StdevP (MDX)
使用偏置总体公式除以 _n_) ，返回对集求值的数值表达式的总体标准偏差 (。
```
  
StdevP(Set_Expression [ ,Numeric_Expression ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
**StdevP** 函数使用有偏差总体公式，而 Stdev 函数使用无偏差总体公式。
下面的示例将使用有偏差总体公式返回对 2003 日历年度中前三个月求得的 Internet Order Quantity 的标准偏差。
```
WITH MEMBER Measures.x AS   
   StdevP   
   ( { [Date].[Calendar].[Month].[January 2003],  
       [Date].[Calendar].[Month].[February 2003],  
       [Date].[Calendar].[Month].[March 2003]},  
    [Measures].[Internet Order Quantity])  
SELECT Measures.x ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


