#### 通过
# FirstChild (MDX)
返回指定成员的第一个子成员。
```
  
Member_Expression.FirstChild   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
下面的查询返回 Fiscal 层次结构中 2003 会计年度的第一个子级，也就是 2003 会计年度的第一个半期。
```
SELECT [Date].[Fiscal].[Fiscal Year].&[2003].FirstChild ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


