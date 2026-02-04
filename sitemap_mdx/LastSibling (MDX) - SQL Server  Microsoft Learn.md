#### 通过
# LastSibling (MDX)
返回指定成员的父成员的最后一个子成员。
```
  
Member_Expression.LastSibling   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
下面的示例返回 2002 年 7 月最后一天的默认度量值。
```
SELECT [Date].[Fiscal].[Date].&[20020717].LastSibling   
   ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


