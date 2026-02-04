#### 通过
# FirstSibling (MDX)
返回成员的父成员的第一个子成员。
```
  
Member_Expression.FirstSibling   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
以下查询将返回 Fiscal 层次结构中 Fiscal Year 2003 的第一个同级，即 Fiscal Year 2002。
```
SELECT [Date].[Fiscal].[Fiscal Year].&[2003].FirstSibling ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


