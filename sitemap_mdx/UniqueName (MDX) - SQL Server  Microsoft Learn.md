#### 通过
# UniqueName (MDX)
返回指定的维度、层次结构、级别或成员的唯一名称。
```
  
Dimension expression syntax  
Dimension_Expression.UniqueName  
  
Hierarchy expression syntax  
Hierarchy_Expression.UniqueName  
  
Level expression syntax  
Level_Expression.UniqueName  
  
Member expression syntax  
Member_Expression.UniqueName  

```

_Dimension_Expression_ 解析为维度的有效多维表达式 (MDX)。
_Hierarchy_Expression_ 返回层次结构的有效多维表达式 (MDX)。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
**UniqueName** 函数返回对象的唯一名称，而不是 Name 函数返回的名称。 返回的名称不包括多维数据集的名称。 返回的结果取决于服务器端设置或 MDX Unique Name Style 连接字符串属性。 
下例将返回 Adventure Works 多维数据集中的 Product 维度、Product Categories 层次结构、Subcategory 级别和 Bike Racks 成员的唯一名称值。
```
WITH MEMBER DimensionUniqueName   
   AS [Product].UniqueName  
MEMBER HierarchyUniqueName   
   AS [Product].[Product Categories].UniqueName  
MEMBER LevelUniqueName   
   AS [Product].[Product Categories].[Subcategory].UniqueName  
MEMBER MemberUniqueName   
   AS [Product].[Product Categories].[Subcategory].[Bike Racks]  
SELECT   
   {DimensionUniqueName  
   , HierarchyUniqueName  
   , LevelUniqueName  
   , MemberUniqueName }  
   ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


