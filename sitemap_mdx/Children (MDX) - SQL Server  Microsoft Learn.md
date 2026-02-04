#### 通过
# Children (MDX)
返回指定成员的子成员集。
```
Member_Expression.Children

```

####  _Member_Expression_
返回成员的有效多维表达式 (MDX)。
**Children** 函数返回一个自然排序的集，该集包含指定成员的子级。 如果指定的成员没有子成员，则此函数返回一个空集。
下例将返回 Geography 维度中 Geography 层次结构的 United States 成员的子成员。
```
SELECT [Geography].[Geography].[Country].&[United States].Children ON 0
FROM [Adventure Works];

```

以下示例返回列轴上的**“度量值”** 维度中的所有成员，其中包括所有计算成员，以及 **Adventure Works** 多维数据集中`[Product].[Model Name]`行轴上属性层次结构的所有子级集。
```
SELECT
    Measures.AllMembers ON COLUMNS,
    [Product].[Model Name].Children ON ROWS
FROM
    [Adventure Works]  

```



1月27日 15时 - 1月27日 15时 


