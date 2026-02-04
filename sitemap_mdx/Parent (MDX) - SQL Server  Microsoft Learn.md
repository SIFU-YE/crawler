#### 通过
# Parent (MDX)
返回成员的父成员。
```
  
Member_Expression.Parent   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
**Parent** 函数返回指定成员的父成员。
以下例返回“July 1, 2001”成员的父成员。 第一个示例在日期属性层次结构的上下文中指定了该成员并返回“所有时期”成员。
```
SELECT [Date].[Date].[July 1, 2001].Parent ON 0  
FROM [Adventure Works]  

```

下例在日历层次结构的上下文中指定了“July 1, 2001”成员。
```
SELECT [Date].[Calendar].[July 1, 2001].Parent ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


