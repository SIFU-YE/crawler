#### 通过
# LastChild (MDX)
返回指定成员的最后一个子成员。
```
  
Member_Expression.LastChild   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
下例将返回 2001 年 9 月的值，它是 2002 会计年度第一个会计季度的最后一个子成员。
```
SELECT [Date].[Fiscal].[Fiscal Quarter].[Q1 FY 2002].LastChild ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


