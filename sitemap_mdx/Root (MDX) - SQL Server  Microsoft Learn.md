#### 通过
# Root (MDX)
返回一个元组，该元组由多维数据集、维度或元组中当前范围内每个属性层次结构中的 **All** 成员组成。 有关范围的详细信息，请参阅 SCOPE 语句 (MDX) 。
如果属性层次结构没有 **All** 成员，则元组包含该层次结构的默认成员。
```
  
Cube syntax  
Root ()  
Dimension syntax  
Root( Dimension_Name )  
Tuple syntax  
Root( Tuple_Expression )  

```

_Dimension_Name_ 指定维度名称的有效字符串表达式。
_Tuple_Expression_ 返回元组的有效多维表达式 (MDX)。
如果未指定维度名称和元组表达式，则 **根** 函数返回包含 **All** 成员 (的元组;如果从多维数据集中的每个属性层次结构) 不存在 **All** 成员，则返回默认成员。 成员在元组中的顺序基于多维数据集中定义属性层次结构的顺序。
如果指定了维度名称， **则 Root** 函数将返回一个元组，其中包含 **All** 成员 (;如果指定维度中的每个属性层次结构中不存在 **All** 成员，则返回默认成员) 基于当前成员的上下文。 成员在元组中的顺序基于维度中定义属性层次结构的顺序。
如果指定了层次结构名称， **则元组** 函数将从指定的层次结构名称中选取维度名称。
如果指定元组表达式， **则 Root** 函数将返回一个元组，其中包含指定元组的交集和未显式包含在指定元组中的所有其他维度属性 **的 All** 成员。
以下示例返回包含 **All** 成员的元组 (或默认值（如果 **所有** 成员不存在）) Adventure Works 多维数据集中的每个层次结构。
```
SELECT Root()ON 0  
FROM [Adventure Works]  

```

以下示例返回包含 **All** 成员 (元组，如果 **所有** 成员不存在，) Adventure Works 多维数据集中日期维度中的每个层次结构中的所有成员，以及与这些默认成员相交的 Measures 维度指定成员的值，则返回默认值。
```
SELECT Root([Date]) ON 0  
FROM [Adventure Works]  
WHERE [Measures].[Order Count]  

```

以下示例返回包含指定元组成员 (2001 年 7 月 1 日，以及 **All** 成员 (或默认值（如果“ **日期** ”维度 Adventure Works 多维数据集中每个非指定的层次结构) 中所有成员不存在）和与这些成员相交的 Measures 维度的指定成员的值，则返回默认值。
```
SELECT Root([Date].[July 1, 2001]) ON 0  
FROM [Adventure Works]  
WHERE [Measures].[Order Count]  

```

1月27日 15时 - 1月27日 15时 


