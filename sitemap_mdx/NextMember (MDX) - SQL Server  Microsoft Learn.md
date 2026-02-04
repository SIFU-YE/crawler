#### 通过
# NextMember (MDX)
返回指定成员所在级别的下一个成员。
```
  
Member_Expression.NextMember   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
**NextMember** 函数返回同一级别中包含指定成员的下一个成员。
下例将返回作为 July 2001 成员的下一个成员的 August 2001 成员。
```
SELECT [Date].[Calendar].[Month].[July 2001].NextMember ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


