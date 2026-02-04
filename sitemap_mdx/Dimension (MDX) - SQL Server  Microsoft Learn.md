#### 通过
# Dimension (MDX)
返回包含指定成员、级别或层次结构的层次结构。
```
  
Hierarchy syntax  
Hierarchy_Expression.Dimension  
  
Level syntax  
Level_Expression.Dimension  
  
Member syntax  
Member_Expression.Dimension  
  

```

_Hierarchy_Expression_ 返回层次结构的有效多维表达式 (MDX)。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
以下示例使用 **Dimension** 函数和 **Name** 函数返回指定成员的层次结构名称。
```
WITH member measures.x as [Product].[Product Model Lines].[Model].&[HL Road Tire].Dimension.Name  
SELECT measures.x on 0  
FROM [Adventure Works]  

```

下例将 Dimension 函数与 Levels 和 Count 函数结合使用，以返回包含指定成员的层次结构中的级别数目。
```
WITH member measures.x as [Product].[Product Model Lines].[Model].&[HL Road Tire].Dimension.Levels.Count  
SELECT measures.x on 0  
FROM [Adventure Works]  

```

以下示例将 **Dimension** 函数与 **Members** 和 **Count** 函数结合使用，返回层次结构中包含指定成员的成员数。
```
WITH member measures.x as [Product].[Product Model Lines].[Model].&[HL Road Tire].Dimension.Members.Count  
SELECT measures.x on 0  
FROM [Adventure Works]  

```

Count（层次结构级别）(MDX) Count（集）(MDX) Levels (MDX) Members（集）(MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


