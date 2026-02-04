#### 通过
# Siblings (MDX)
返回指定成员的同级，包括该成员本身。
```
  
Member_Expression.Siblings   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
下面的示例返回 March 2003 的同级（即 January 2003 和 February 2003，也包括 March 2003）的默认度量值。
```
SELECT [Date].[Calendar].[Month].[March 2003].Siblings ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


