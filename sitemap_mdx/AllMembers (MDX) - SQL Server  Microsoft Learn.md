#### 通过
# AllMembers (MDX)
计算层次结构或级别表达式，并返回一个包含指定层次结构或级别的所有成员的集，该集包含层次结构或级别的所有计算成员。
```
  
Hierarchy syntax  
Hierarchy_Expression.AllMembers  
  
Level syntax  
Level_Expression.AllMembers  

```

_Hierarchy_Expression_ 返回层次结构的有效多维表达式 (MDX)。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
**AllMembers** 函数返回一个集，其中包含指定层次结构或级别中的所有成员（包括计算成员）。 即使指定的层次结构或级别不包含可见成员， **AllMembers** 函数也会返回计算成员。
如果维度仅包含单个可见层次结构，由于在此情况下维度名称将解析为其唯一可见的层次结构，所以既可以通过维度名称也可以通过层次结构名称来引用该层次。 例如，`Measures.AllMembers` 是一个有效的 MDX 表达式，这是因为它会解析为 Measures 维度中唯一的层次结构。
**AllMembers** 函数在语义上类似于 AddCalculatedMembers (MDX)  函数。
以下示例返回列轴上 [`Date].[Calendar Year]` 属性层次结构中的所有成员，其中包括计算成员，以及 **Adventure Works** 多维数据集中行轴上属性层次结构的所有子`[Product].[Model Name]`级集。
```
SELECT  
   [Date].[Calendar Year].AllMembers ON COLUMNS,  
   [Product].[Model Name].Children ON ROWS  
FROM  
   [Adventure Works]  

```

以下示例返回列轴上**“度量值”** 维度中的所有成员，其中包括所有计算成员，以及 **Adventure Works** 多维数据集中行轴上属性层次结构的所有子`[Product].[Model Name]`级集。
```
SELECT  
    Measures.AllMembers ON COLUMNS,  
    [Product].[Model Name].Children ON ROWS  
FROM  
    [Adventure Works]  

```

AddCalculatedMembers (MDX) Children (MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


