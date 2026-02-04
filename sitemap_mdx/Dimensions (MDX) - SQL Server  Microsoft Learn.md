#### 通过
# Dimensions (MDX)
返回由数值表达式或字符串表达式指定的层次结构。
```
  
Numeric expression syntax  
Dimensions(Hierarchy_Number)  
  
String expression syntax  
Dimensions(Hierarchy_Name)  

```

_Hierarchy_Number_ 指定层次结构号的有效数值表达式。
_Hierarchy_Name_ 指定层次结构名称的有效字符串表达式。
如果指定了层次结构编号， **Dimensions** 函数将返回一个层次结构，该层次结构在多维数据集中从零开始的位置是指定的层次结构编号。
如果指定了层次结构名称， **Dimensions** 函数将返回指定的层次结构。 通常，将此字符串版本的 **Dimensions** 函数与用户定义的函数一起使用。
**度量值** 维度始终由 `Dimensions(0)`表示。
以下示例使用 **Dimensions** 函数，使用数值表达式和字符串表达式返回指定层次结构的成员的名称、级别计数和计数。
```
WITH MEMBER Measures.x AS Dimensions  
   ('[Product].[Product Model Lines]').Name  
SELECT Measures.x on 0  
FROM [Adventure Works]  
  
WITH MEMBER Measures.x AS Dimensions  
   ('[Product].[Product Model Lines]').Levels.Count  
SELECT Measures.x on 0  
FROM [Adventure Works]  
  
WITH MEMBER Measures.x AS Dimensions  
   ('[Product].[Product Model Lines]').Members.Count  
SELECT Measures.x on 0  
FROM [Adventure Works]  
  
WITH MEMBER Measures.x AS Dimensions(0).Name  
SELECT Measures.x on 0  
FROM [Adventure Works]  
  
WITH MEMBER Measures.x AS Dimensions(0).Levels.Count  
SELECT measures.x on 0  
FROM [Adventure Works]  
  
WITH MEMBER Measures.x AS Dimensions(0).Members.Count  
SELECT measures.x on 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


