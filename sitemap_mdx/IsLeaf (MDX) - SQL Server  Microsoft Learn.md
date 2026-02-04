#### 通过
# IsLeaf (MDX)
返回指定成员是否为叶成员。
```
  
IsLeaf(Member_Expression)   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
如果指定的成员是叶成员， **则 IsLeaf** 函数返回 **true** 。 否则，函数返回 **false** 。
如果 [Date].[Fiscal].CurrentMember 是叶成员，下面的示例将返回 TRUE：
```
WITH MEMBER MEASURES.ISLEAFDEMO AS  
IsLeaf([Date].[Fiscal].CURRENTMEMBER)  
SELECT {MEASURES.ISLEAFDEMO} ON 0,  
[Date].[Fiscal].MEMBERS ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


