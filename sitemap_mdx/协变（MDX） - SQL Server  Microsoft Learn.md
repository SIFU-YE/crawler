#### 通过
# 协变（MDX）
通过使用偏置总体公式（除以 x-y 对数），返回通过集计算的 x-y 对值的填充协变。
```
  
Covariance(Set_Expression,Numeric_Expression_y [ ,Numeric_Expression_x ] )  

```

_Set_Expression_ 返回集的有效多维表达式 （MDX） 表达式。
_Numeric_Expression_y_ 一个有效的数值表达式，它通常是单元格坐标的多维表达式（MDX）表达式，该表达式返回一个数字，表示 y 轴的值。
_Numeric_Expression_x_ 一个有效的数值表达式，该表达式通常是单元格坐标的多维表达式（MDX）表达式，该表达式返回一个表示 x 轴值的数字。
**协变** 函数根据第一个数值表达式计算指定的集，以获取 y 轴的值。 然后，该函数根据第二个数值表达式（如果指定）计算指定的集，以获取 x 轴的值集。 如果未指定第二个数值表达式，该函数将使用指定集中单元格的当前上下文作为 x 轴的值。
**协变** 函数使用偏置总体公式。 这与使用无偏差总体公式的 协方差N 函数（除以 x-y 对数，然后减去 1） 的函数形成鲜明对比。
**协变** 函数将忽略包含文本或逻辑值的空单元格或单元格。 但是，该函数包含值为零的单元格。
以下示例演示如何使用协变函数：
```
WITH   
MEMBER [Measures].[CovarianceDemo] AS  
COVARIANCE([Date].[Date].[Date].Members, [Measures].[Internet Sales Amount], [Measures].[Internet Order Count])   
SELECT {[Measures].[CovarianceDemo]} ON 0   
FROM  
[Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


