#### 通过
# DefaultMember (MDX)
返回层次结构的默认成员。
```
  
Hierarchy_Expression.DefaultMember  

```

_Hierarchy_Expression_ 返回层次结构的有效多维表达式 (MDX)。
特性的默认成员用于在查询中不包括特性的情况下计算表达式。
以下示例使用 **DefaultMember** 函数和 **Name** 函数返回 Adventure Works 多维数据集中 Destination Currency 维度的默认成员。 该示例返回 **美元** 。 **Name** 函数用于返回度量值的名称，而不是度量值的默认**属性。**
```
WITH MEMBER Measures.x AS   
   [Destination Currency].[Destination Currency].DefaultMember.Name  
SELECT Measures.x ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


