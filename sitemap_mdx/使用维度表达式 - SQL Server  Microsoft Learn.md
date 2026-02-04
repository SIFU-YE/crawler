#### 通过
# 使用维度表达式
将参数传递给多维表达式 (MDX) 中的函数时，通常使用维度表达式和层次结构表达式从层次结构中返回成员、集或元组。
因为维度表达式是对象标识符，所以它们只能是简单表达式。 有关简单表达式和复杂表达式的说明，请参阅 MDX)  (表达式。
维度表达式包含维度标识符或维度函数。
维度表达式很少单独使用。 相反，您通常希望在维度上指定层次结构。 唯一的例外情况是处理 Measures 维度，该维度没有层次结构。
以下示例说明计算成员，它使用表达式 [Measures] 以及 .Members 和 Count() 函数来返回 Measures 维度上成员的数目。
```
WITH MEMBER [Measures].[MeasureCount] AS  
COUNT([Measures].MEMBERS)  
SELECT [Measures].[MeasureCount] ON 0  
FROM [Adventure Works]  

```

维度标识符在用于描述 MDX 语句的 BNF 表示法中显示为 _Dimension_Name_ 。
同样，层次结构表达式包含层次结构标识符或层次结构函数。 以下示例说明使用层次结构表达式 [Date].[Calendar] 以及 .Levels 和 .Count 函数返回 Date 维度的 Calendar 层次结构中级别的数目。
```
WITH MEMBER [Measures].[CalendarLevelCount] AS  
[Date].[Calendar].Levels.Count  
SELECT [Measures].[CalendarLevelCount] ON 0  
FROM [Adventure Works]  

```

使用层次结构表达式最常见的应用场景是与 .Members 函数一起返回层次结构上的所有成员。 以下示例返回行轴上 [Date].[Calendar] 的所有成员：
```
SELECT [Measures].[Internet Sales Amount] ON 0,  
[Date].[Calendar].MEMBERS ON 1  
FROM [Adventure Works]  

```

层次结构标识符在用于描述 MDX 语句的 BNF 表示法中显示为 _Dimension_Name.Hierarchy_Name_ 。
1月27日 15时 - 1月27日 15时 


