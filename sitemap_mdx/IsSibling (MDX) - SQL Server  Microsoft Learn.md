#### 通过
# IsSibling (MDX)
返回一个指定成员是否为另一个指定成员的同级成员。
```
  
IsSibling(Member_Expression1, Member_Expression2)   

```

_Member_Expression1_ 返回成员的有效多维表达式 (MDX)。
_Member_Expression2_ 返回成员的有效多维表达式 (MDX)。
如果第一个指定成员是第二个指定成员的同级， **则 IsSibling** 函数返回 **true** 。 否则，该函数返回 **false** 。
如果 Date 维度的 Fiscal 层次结构上的当前成员是 2002 年 7 月的同级，则下面的示例将返回 TRUE：
```
WITH MEMBER MEASURES.ISSIBLINGDEMO AS  
IsSibling([Date].[Fiscal].CURRENTMEMBER, [Date].[Fiscal].[Month].&[2002]&[7])  
SELECT {MEASURES.ISSIBLINGDEMO} ON 0,  
[Date].[Fiscal].MEMBERS ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


