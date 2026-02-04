#### 通过
# UnknownMember (MDX)
返回与级别或成员相关联的未知成员。
```
  
Member expression syntax  
Member_Expression.UnknownMember  
  
Hierarchy_expression syntax  
Hierarchy_Expression.UnknownMember  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Hierarchy_Expression_ 返回层次结构的有效多维表达式 (MDX)。
当层次结构未知时，Analysis Services 会创建一个未知成员，以将事实数据表数据与层次结构相关联。 未知成员可位于下列级别之一：
  * 位于未聚合的属性层次结构的顶级。
  * 在自然层次结构的 **“所有** ”级别下面的第一个级别。
  * 位于非自然层次结构的任何一级。


如果指定了成员表达式， **则 UnknownMember** 函数将返回指定成员的未知成员子级。 如果指定的成员不存在，该函数将返回空。
如果指定了层次结构表达式， **则 UnknownMember** 函数在顶层返回未知成员（如果存在）。
如果级别或成员上不存在未知成员， **UnknownMember** 函数将创建一个空成员。
如果层次结构或成员中不存在未知成员，将生成一个错误。
下面的示例为 Measures 维度的所有成员返回 Product 属性层次结构中 All Products 成员的未知成员。
```
SELECT [Product].[Product].[All Products].UnknownMember  
    ON Columns,  
[Measures].Members  
    ON Rows  
FROM [Adventure Works]  
  

```

下面的示例为 Measures 维度的所有成员返回 Product Categories 层次结构的未知成员。
```
SELECT [Product].[Product Categories].UnknownMember  
    ON Columns,  
[Measures].Members  
    ON Rows  
FROM [Adventure Works]  
  

```

1月27日 15时 - 1月27日 15时 


