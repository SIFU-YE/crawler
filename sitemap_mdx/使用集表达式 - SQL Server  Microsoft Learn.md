#### 通过
# 使用集表达式
集由零个或多个元组的有序列表组成。 不包含任何元组的集称为“空集”。
一个集的完整表达式由零个或多个显式指定的元组构成，各元组放在大括号中：
{ [ { _Tuple_expression_ } [ ， { _Tuple_expression |__Member_expression_ } ] ... ] }
集表达式中指定的成员表达式将被转换为由一个成员构成的元组表达式。
以下示例说明在查询的列和行轴上使用的两个集表达式：
```
SELECT  
{[Measures].[Internet Sales Amount], [Measures].[Internet Tax Amount]} ON COLUMNS,  
{([Product].[Product Categories].[Category].&[4], [Date].[Calendar].[Calendar Year].&[2004]),  
([Product].[Product Categories].[Category].&[1], [Date].[Calendar].[Calendar Year].&[2003]),  
([Product].[Product Categories].[Category].&[3], [Date].[Calendar].[Calendar Year].&[2004])}  
ON ROWS  
FROM [Adventure Works]  

```

在列轴上，集
{[Measures].[Internet Sales Amount], [Measures].[Internet Tax Amount]}
由 Measures 维度的两个成员组成。 在行轴上，集
{（[Product]。[产品类别]。[Category].&&[4]， [Date]。[日历]。[Calendar Year].&&[2004]），
（[Product]。[产品类别]。[Category].&&[1]， [Date]。[日历]。[Calendar Year].&&[2003]），
（[Product]。[产品类别]。[Category].&&[3]， [Date]。[日历]。[Calendar Year].&&[2004]]]}
由三个元组组成，每个元组包含对 Product 维度的 Product Categories 层次结构和 Date 维度的 Calendar 层次结构上成员的两个显式引用。
有关返回集的函数的示例，请参阅“使用成员”、“元组”和“集”（MDX）。
1月27日 15时 - 1月27日 15时 


