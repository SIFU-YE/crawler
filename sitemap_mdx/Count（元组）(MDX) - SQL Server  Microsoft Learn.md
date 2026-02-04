#### 通过
# Count（元组）(MDX)
返回元组中的维度数。
```
  
Tuple_Expression.Count  

```

_Tuple_Expression_ 返回元组的有效多维表达式 (MDX)。
返回元组中的维度数。
下面的查询中的计算度量值返回值 2，这是在元组 `([Measures].[Internet Sales Amount], [Date].[Calendar].[Calendar Year].&[2001])` 中提供的层次结构的数目：
```
WITH MEMBER MEASURES.COUNTTUPLE AS  
COUNT(([Measures].[Internet Sales Amount], [Date].[Calendar].[Calendar Year].&[2001]))  
SELECT MEASURES.COUNTTUPLE ON 0  
FROM [Adventure Works]  

```

Count（维度）(MDX) Count（层次结构级别）(MDX) Count（集）(MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


