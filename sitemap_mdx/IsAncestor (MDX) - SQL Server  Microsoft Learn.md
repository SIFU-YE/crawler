#### 通过
# IsAncestor (MDX)
返回一个指定成员是否为另一个指定成员的祖先。
```
  
IsAncestor(Member_Expression1, Member_Expression2)   

```

_Member_Expression1_ 返回成员的有效多维表达式 (MDX)。
_Member_Expression2_ 返回成员的有效多维表达式 (MDX)。
如果指定的第一个成员是指定的第二个成员的上级， **则 IsAncestor** 函数返回 **true** 。 否则，函数返回 **false** 。
以下示例在 [Date] 的情况下返回 **true** 。[Fiscal]。CurrentMember 是 2003 年 1 月的祖先：
```
WITH MEMBER MEASURES.ISANCESTORDEMO AS  
IsAncestor([Date].[Fiscal].CurrentMember, [Date].[Fiscal].[Month].&[2003]&[1])  
SELECT MEASURES.ISANCESTORDEMO ON 0,  
[Date].[Fiscal].MEMBERS ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


