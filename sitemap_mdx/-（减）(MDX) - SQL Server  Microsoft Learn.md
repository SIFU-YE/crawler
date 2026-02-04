#### 通过
# -（减）(MDX)
执行一个算术运算，将一个数减去另一个数。
```
  
Numeric_Expression - Numeric_Expression  

```

_Numeric_Expression_ 返回数值的有效多维表达式 (MDX) 表达式。
具有与优先级较高的参数相同的数据类型的值。
两个表达式必须具有相同的数据类型，或者其中一个表达式必须能够隐式转换为另一个表达式的数据类型。 如果一个表达式的值为空值，则运算符返回非空表达式的结果。
下面的示例演示了此运算符的用法。
```
-- This member returns the increase or decrease  
-- in gross profit margin over a month.  
WITH MEMBER [Measures].[GPM Delta] AS  
 (  
(Measures.[Gross Profit Margin]) -   
([Date].[Calendar].CurrentMember.PrevMember,   
Measures.[Gross Profit Margin])  
  ), FORMAT_STRING = 'Percent'  
  
SELECT   
DESCENDANTS(  
[Date].[Calendar].[Calendar Year].&[2002],   
[Date].[Calendar].[Month]) ON 0,  
[Product].[Category].[Category].Members ON 1  
FROM  
[Adventure Works]  
WHERE  
([Measures].[GPM Delta])  

```

1月27日 15时 - 1月27日 15时 


