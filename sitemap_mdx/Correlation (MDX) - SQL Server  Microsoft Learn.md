#### 通过
# Correlation (MDX)
返回对集求值的 X-Y 值对的关联系数。
```
  
Correlation( Set_Expression, Numeric_Expression_y [ ,Numeric_Expression_x ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_y_ 返回表示 Y 轴值的数字的有效数值表达式，通常是单元坐标的多维表达式 (MDX)。
_Numeric_Expression_x_ 通常是单元坐标（返回代表 X 轴的值的数字）的多维表达式 (MDX) 的有效数值表达式。
**Correlation** 函数通过首先根据第一个数值表达式计算指定的集来计算两对值的相关系数，以获取 y 轴的值。 然后，此函数根据第二个数值表达式（如果存在）对指定集求值，以获取 X 轴对应的值。 如果未指定第二个数值表达式，则此函数使用指定集中的单元的当前上下文作为 X 轴的值。
**Correlation** 函数忽略空单元格或包含文本或逻辑值的单元格。 但是，该函数将包含值为零的单元。
1月27日 15时 - 1月27日 15时 


