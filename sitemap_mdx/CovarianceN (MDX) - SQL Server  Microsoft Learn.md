#### 通过
# CovarianceN (MDX)
通过使用无偏差总体公式（除以 x-y 对的数目），返回对集求得的 x-y 值对的样本协方差。
```
  
CovarianceN(Set_Expression, Numeric_Expression_y [ ,Numeric_Expression_x ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_y_ 返回表示 Y 轴值的数字的有效数值表达式，通常是单元坐标的多维表达式 (MDX)。
_Numeric_Expression_x_ 通常是单元坐标（返回代表 X 轴的值的数字）的多维表达式 (MDX) 的有效数值表达式。
**CovarianceN** 函数根据第一个数值表达式计算指定的集，以获取 y 轴的值。 然后，此函数对指定的集计算第二个数值表达式（如果指定），以获得 x 轴的一组值。 如果未指定第二个数值表达式，则该函数使用指定集中的单元的当前上下文作为 X 轴的值。
**协变N** 函数使用无偏置总体公式。 这与使用偏置总体公式 (除以) x-y 对数的 协变 函数相反。
**CovarianceN** 函数忽略空单元格或包含文本或逻辑值的单元格。 但是，该函数将包含值为零的单元。
1月27日 15时 - 1月27日 15时 


