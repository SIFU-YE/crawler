#### 通过
# LookupCube (MDX)
返回用多维表达式 (MDX) 对同一数据库中的另一个指定多维数据集求得的值。
```
  
Numeric expression syntax  
LookupCube(Cube_Name, Numeric_Expression )  
  
String expression syntax  
LookupCube(Cube_Name, String_Expression )  

```

_Cube_Name_ 指定多维数据集名称的有效字符串表达式。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
_String_Expression_ 一个有效的字符串表达式，通常为返回一个字符串的单元坐标的有效多维表达式 (MDX)。
如果指定了数值表达式， **LookupCube** 函数将计算指定多维数据集中的指定数值表达式，并返回生成的数值。
如果指定了字符串表达式， **LookupCube** 函数将计算指定多维数据集中的指定字符串表达式，并返回生成的字符串值。
**LookupCube** 函数适用于运行包含 **LookupCube** 函数的 MDX 查询所在的源多维数据集所在的同一数据库中的多维数据集。
因为当前查询的上下文不会延续到将要查询的多维数据集，所以必须在数值或字符串表达式内提供任何必要的当前成员。
使用 **LookupCube** 函数的任何计算都可能会受到性能不佳的影响。 请考虑重新设计您的解决方案，而不是使用此函数，以便在一个多维数据集中提供您所需的所有数据。
以下查询演示 LookupCube 的用法：
```
WITH MEMBER MEASURES.LOOKUPCUBEDEMO AS  
LOOKUPCUBE("Adventure Works", "[Measures].[In" + "ternet Sales Amount]")  
SELECT MEASURES.LOOKUPCUBEDEMO  ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


