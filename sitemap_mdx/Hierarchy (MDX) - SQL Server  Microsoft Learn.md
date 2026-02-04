#### 通过
# Hierarchy (MDX)
返回包含指定的成员或级别的层次结构。
```
  
Member expression syntax  
Member_Expression.Hierarchy  
  
Level expression syntax  
Level_Expression.Hierarchy  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
以下示例返回 AdventureWorks 多维数据集中 Date 维度中日历层次结构的名称。
```
WITH  
MEMBER Measures.HierarchyName as  
[Date].[Calendar].Currentmember.Hierarchy.Name  
SELECT {Measures.HierarchyName}  ON 0,  
{[Date].[Calendar].[All Periods]} ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


