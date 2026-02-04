#### 通过
# Count（层次结构级别）(MDX)
返回层次结构中的级别数。
```
  
Hierarchy_Expression.Levels.Count  

```

_Hierarchy_Expression_ 返回层次结构的有效多维表达式 (MDX)。
返回层次结构中的级别数，包括 `[All]` 级别（如果存在）。
如果维度只包含一个可见的层次结构，则可以通过此维度的名称或此层次结构的名称引用此层次结构，原因是此维度的名称会解析为它唯一可见的层次结构。 例如，`Measures.Levels.Count` 是一个有效的 MDX 表达式，这是因为它会解析为 Measures 维度中唯一的层次结构。
下面的示例返回 Adventure Works 多维数据集中 Product Categories 用户定义层次结构中的级别数计数。
```
WITH MEMBER measures.X AS  
   [Product].[Product Categories].Levels.Count   
Select Measures.X ON 0  
FROM [Adventure Works]  

```

Count（维度）(MDX) Count（元组）(MDX) Count（集）(MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


