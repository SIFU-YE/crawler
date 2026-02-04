#### 通过
# 使用逻辑函数
逻辑函数对对象和表达式执行逻辑操作或比较并返回布尔值。 在多维表达式 (MDX) 中，逻辑函数对确定成员的位置至关重要。
最常用的逻辑函数是 **IsEmpty** 函数。 有关如何使用 **IsEmpty** 函数的详细信息，请参阅 使用空值。
以下查询演示如何使用 **IsLeaf** 和 **IsAncestor** 函数：
```
WITH  
//Returns true if the CurrentMember on Calendar is a leaf member, ie it has no children  
MEMBER MEASURES.[IsLeafDemo] AS IsLeaf([Date].[Calendar].CurrentMember)  
//Returns true if the CurrentMember on Calendar is an Ancestor of July 1st 2001  
MEMBER MEASURES.[IsAncestorDemo] AS IsAncestor([Date].[Calendar].CurrentMember, [Date].[Calendar].[Date].&[1])  
SELECT{MEASURES.[IsLeafDemo],MEASURES.[IsAncestorDemo] } ON 0,  
[Date].[Calendar].MEMBERS ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


