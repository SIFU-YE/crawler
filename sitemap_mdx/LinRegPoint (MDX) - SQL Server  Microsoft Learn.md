#### 通过
# LinRegPoint (MDX)
计算集的线性回归，并返回回归线中 _y 截距_ 的值，y = ax + b 表示 x 的特定值。
```
  
LinRegPoint(Slice_Expression_x, Set_Expression, Numeric_Expression_y [ ,Numeric_Expression_x ] )  

```

_Slice_Expression_x_ 一个有效的数值表达式，通常为返回一个数值（该数值表示切片轴的值）的单元坐标的多维表达式 (MDX)。
_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_y_ 返回表示 Y 轴值的数字的有效数值表达式，通常是单元坐标的多维表达式 (MDX)。
_Numeric_Expression_x_ 通常是单元坐标（返回代表 X 轴的值的数字）的多维表达式 (MDX) 的有效数值表达式。
线性回归使用最小二乘法，可以计算出回归线（即一系列点的最佳拟合线）的公式。 回归线具有以下公式，其中 a 是斜率，b 是截距：
y = ax+b
**LinRegPoint** 函数根据第二个数值表达式计算指定的集，以获取 y 轴的值。 然后，此函数根据第三个数值表达式（如果已指定）对指定集求值，以获取 X 轴的值。 如果未指定第三个数值表达式，则该函数将使用指定集中单元的当前上下文作为 X 轴的值。 不指定 x 轴参数经常与时间维度一起使用。
一旦计算完线性回归线，即为第一个数值表达式计算等式的值，并且随后返回该值。
**LinRegPoint** 函数忽略空单元格或包含文本的单元格。 但是，该函数将包含值为零的单元。
下例根据单位销售额和商店销售额之间的统计关系，依据过去十个时期的数据得出单位销售额的预测值。
```
LinRegPoint([Measures].[Unit Sales],LastPeriods(10),[Measures].[Unit Sales],[Measures].[Store Sales])  

```

1月27日 15时 - 1月27日 15时 


