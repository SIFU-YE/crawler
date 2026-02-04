#### 通过
# 使用成员函数
成员函数是返回成员的多维表达式 (MDX) 函数。 成员函数（如元组函数和 set 函数）对于协商 Analysis Services 中的多维结构至关重要。
在 MDX 中的许多成员函数中，最重要的是 **CurrentMember** 函数，该函数用于确定层次结构上的当前成员。 以下查询演示了如何使用它以及 **Parent** 、 **Ancestor** 和 **Prevmember** 函数：
```
WITH  
//Returns the name of the currentmember on the Calendar hierarchy  
MEMBER MEASURES.[CurrentMemberDemo] AS [Date].[Calendar].CurrentMember.Name  
//Returns the name of the parent of the currentmember on the Calendar hierarchy  
MEMBER MEASURES.[ParentDemo] AS [Date].[Calendar].CurrentMember.Parent.Name  
//Returns the name of the ancestor of the currentmember on the Calendar hierarchy at the Year level  
MEMBER MEASURES.[AncestorDemo] AS ANCESTOR([Date].[Calendar].CurrentMember, [Date].[Calendar].[Calendar Year]).Name  
//Returns the name of the member before the currentmember on the Calendar hierarchy  
MEMBER MEASURES.[PrevMemberDemo] AS [Date].[Calendar].CurrentMember.Prevmember.Name  
SELECT{MEASURES.[CurrentMemberDemo],MEASURES.[ParentDemo],MEASURES.[AncestorDemo],MEASURES.[PrevMemberDemo] } ON 0,  
[Date].[Calendar].MEMBERS ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


