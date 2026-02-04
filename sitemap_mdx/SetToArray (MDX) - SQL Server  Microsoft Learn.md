#### 通过
# SetToArray (MDX)
将一个或多个集转换为数组，以便在用户定义函数中使用。
```
  
SetToArray(Set_Expression1 [ ,Set_Expression2,...n ][ ,Numeric_Expression ] )  

```

_Set_Expression1_ 返回集的有效多维表达式 (MDX)。
_Set_Expression2_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
**SetToArray** 函数将一个或多个集转换为数组，以便在用户定义的函数中使用。 所得到的数组中的维度数与指定的集数相同。
可选的数值表达式可以为数组单元提供值。 如果未指定数值表达式，则在当前上下文中对集的交叉联接求值。
所得到的数组中的单元坐标与各个集在列表中的位置相对应。 例如，有三个集，`SA`、`SB` 和 `SC`。 其中每个集都有两个元素。 则 MDX 语句 `SetToArray(SA, SB, SC)` 创建以下三维数组：
```
(SA1, SB1, SC1) (SA2, SB1, SC1) (SA1, SB2, SC1) (SA2, SB2, SC1)   
(SA1, SB1, SC2) (SA2, SB1, SC2) (SA1, SB2, SC2) (SA2, SB2, SC2)   

```

**SetToArray** 函数的返回类型是 VARIANT 类型，VT_ARRAY。 因此， **SetToArray** 函数的输出应仅用作用户定义函数的输入。
下例将返回一个数组。
```
SetToArray([Geography].[Geography].Members, [Measures].[Internet Sales Amount])  

```

1月27日 15时 - 1月27日 15时 


