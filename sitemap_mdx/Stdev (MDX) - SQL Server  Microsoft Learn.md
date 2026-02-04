#### 通过
# Stdev (MDX)
返回数值表达式用无偏差总体公式（除以 n-1）对集求得的样本标准偏差。
```
  
Stdev(Set_Expression [ ,Numeric_Expression ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
**Stdev** 函数使用无偏差总体公式，而 StdevP 函数使用有偏差总体公式。
下例将使用无偏差总体公式返回对日历年 2003 的前三个月求得的 Internet Order Quantity 的标准偏差。
```
WITH MEMBER Measures.x AS   
   Stdev   
   ( { [Date].[Calendar].[Month].[January 2003],  
       [Date].[Calendar].[Month].[February 2003],  
       [Date].[Calendar].[Month].[March 2003]},  
    [Measures].[Internet Order Quantity])  
SELECT Measures.x ON 0  
FROM [Adventure Works]  

```



