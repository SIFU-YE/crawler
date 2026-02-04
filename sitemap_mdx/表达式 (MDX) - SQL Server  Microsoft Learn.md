#### 通过
# 表达式 (MDX)
表达式是标识符、值和运算符的组合，可以计算这些标识符、值和运算符来获取结果。 访问或更改数据时，可以在多个不同位置使用数据。 例如，可以将表达式用作查询要检索的数据的一部分，或用作查找满足一组条件的数据的搜索条件。
## 简单表达式和复杂表达式
在 MDX 中，表达式可以是简单的，也可以是复杂的：
简单表达式可以是下列几种表达式之一：
常数 在 MDX 中，常量是表示单个特定值的符号。 字符串、数字和日期值可以呈现为常量。 与数值常量不同，字符串和日期常量必须用单引号 (') 字符分隔开。
标量函数 在 MDX 中，标量函数返回计算上下文内的单个值。 此区别对于理解 MDX 如何解析标量函数很重要，因为不是对单个数据元素计算大多数 MDX 表达式、语句和脚本，而是重复地对一组数据元素（如单元或成员）进行计算。 但在计算标量函数时，函数通常查看单个数据元素。
对象标识符 由于多维数据的本质，因此 MDX 是面向对象的。 在 MDX 中，对象标识符被视为简单表达式。 有关标识符的详细信息，请参阅标识符  (MDX) 。
可以从用运算符联接的这些实体的组合生成复杂表达式。
对于由单个常量、变量、标量函数或列名生成的简单表达式，表达式的数据类型、排序规则、精度、小数位数和值是被引用元素的数据类型、排序规则、精度、小数位数和值。 因为 MDX 仅直接支持 OLE VARIANT 数据类型，所以使用简单表达式时不会发生强制。
对于复杂表达式，当使用两个或多个不同数据类型的简单表达式时，可以发生强制。
以下查询说明其定义是简单表达式的计算度量值的示例：
```
WITH
    MEMBER MEASURES.CONSTANTVALUE AS 1
    MEMBER MEASURES.SCALARFUNCTION AS [Date].[Calendar Year].CURRENTMEMBER.NAME
    MEMBER MEASURES.OBJECTIDENTIFIER AS [Measures].[Internet Sales Amount]
SELECT
    { MEASURES.CONSTANTVALUE, MEASURES.SCALARFUNCTION, MEASURES.OBJECTIDENTIFIER } ON 0,
    [Date].[Calendar Year].MEMBERS ON 1
FROM [Adventure Works]

```

表达式还可以是计算，例如 `[Measures].[Discount Amount] * 1.5`。 下面的示例说明如何在 MDX SELECT 语句使用计算来定义成员：
```
WITH   
   MEMBER [Measures].[Special Discount] AS  
   [Measures].[Discount Amount] * 1.5  
SELECT   
   [Measures].[Special Discount] on COLUMNS,  
   NON EMPTY [Product].[Product].MEMBERS  ON Rows  
FROM [Adventure Works]  
WHERE [Product].[Category].[Bikes]  

```

定义多维数据集和子多维数据集表达式。  
---  
定义维度表达式。  
定义成员表达式。  
定义元组表达式。  
定义集表达式。  
定义标量表达式。  
说明什么是空值以及如何处理此类值。  
MDX 语言参考 (MDX) MDX 查询基础知识 (Analysis Services)
1月27日 15时 - 1月27日 15时 


