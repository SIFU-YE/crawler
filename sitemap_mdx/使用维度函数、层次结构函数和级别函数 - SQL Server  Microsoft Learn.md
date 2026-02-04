#### 通过
# 使用维度函数、层次结构函数和级别函数
维度函数、层次结构函数和级别函数对遍历 Analysis Services 中的多维结构非常有用。 通常将此类函数和其他函数一起使用，以获得有关维度、层次结构或级别的成员信息。
以下示例演示如何使用 **。维度** ， **。层次结构** ， 和 **。级别** 函数：
```
WITH  
MEMBER MEASURES.DIMENSIONNAME AS [Date].[Calendar].CURRENTMEMBER.DIMENSION.NAME  
MEMBER MEASURES.HIERARCHYNAME AS [Date].[Calendar].CURRENTMEMBER.HIERARCHY.NAME  
MEMBER MEASURES.LEVELNAME AS [Date].[Calendar].LEVEL.NAME  
SELECT  
{MEASURES.DIMENSIONNAME, MEASURES.HIERARCHYNAME, MEASURES.LEVELNAME}  
ON Columns,  
[Date].[Calendar].MEMBERS  
ON Rows  
FROM [Adventure Works]  

```

Dimension (MDX) 函数（MDX 语法） Hierarchy (MDX) Level (MDX)
1月27日 15时 - 1月27日 15时 


