#### 通过
# Name (MDX)
返回维度、层次结构、级别或成员的名称。
```
  
Dimension expression syntax  
Dimension_Expression.Name  
  
Hierarchy expression syntax  
Hierarchy_Expression.Name  
  
Level_expression syntax  
Level_Expression.Name  
  
Member expression syntax  
Member_Expression.Name  

```

_Dimension_Expression_ 返回维度的有效多维表达式 (MDX)。
_Hierarchy_Expression_ 返回层次结构的有效多维表达式 (MDX)。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
**Name** 函数返回对象的名称，而不是唯一名称。
### 维度、层次结构和级别表达式示例
下面的示例返回 Date 维度的维度名称以及 July 2001 成员的层次结构和级别名称。
```
WITH MEMBER Measures.DimensionName AS [Date].Name  
MEMBER Measures.HierarchyName AS [Date].[Calendar].[July 2001].Hierarchy.Name  
MEMBER Measures.LevelName as [Date].[Calendar].[July 2001].Level.Name  
  
SELECT {Measures.DimensionName, Measures.HierarchyName, Measures.LevelName} ON 0  
from [Adventure Works]  

```

下面的示例返回成员名称以及成员值、成员键和成员标题。
```
WITH MEMBER MemberName AS [Date].[Calendar].[July 1, 2001].Name  
MEMBER Measures.ValueColumn as [Date].[Calendar].[July 1, 2001].MemberValue  
MEMBER Measures.KeyColumn as [Date].[Calendar].[July 1, 2001].Member_Key  
MEMBER Measures.NameColumn as [Date].[Calendar].[July 1, 2001].Member_Name  
  
SELECT {Measures.MemberName, Measures.ValueColumn, Measures.KeyColumn, Measures.NameColumn} ON 0  
from [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


