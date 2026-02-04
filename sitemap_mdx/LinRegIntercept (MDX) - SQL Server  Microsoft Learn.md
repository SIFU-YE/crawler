#### 通过
# LinRegIntercept (MDX)
计算集的线性回归，并返回回归线中 x 截距的值，y = ax + b。
```
  
LinRegIntercept(Set_Expression, Numeric_Expression_y [ ,Numeric_Expression_x ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_y_ 返回表示 Y 轴值的数字的有效数值表达式，通常是单元坐标的多维表达式 (MDX)。
_Numeric_Expression_x_ 通常是单元坐标（返回代表 X 轴的值的数字）的多维表达式 (MDX) 的有效数值表达式。
线性回归使用最小二乘法，可以计算出回归线（即一系列点的最佳拟合线）的公式。 回归线具有以下公式，其中 a 是斜率，b 是截距：
y = ax+b
**LinRegIntercept** 函数根据第一个数值表达式计算指定的集，以获取 y 轴的值。 然后，该函数对指定集计算第二个数值表达式（如果指定）的值，以获得 X 轴的值。 如果未指定第二个数值表达式，则该函数使用指定集中的单元的当前上下文作为 X 轴的值。 不指定 x 轴参数经常与时间维度一起使用。
获取点集后， **LinRegIntercept** 函数返回上一公式) 中回归线 b (截距。
**LinRegIntercept** 函数忽略包含文本或逻辑值的空单元格或单元格。 但是，该函数将包含值为零的单元。
下例将返回单位销售额和存储销售额的回归线截距。
```
LinRegIntercept(LastPeriods(10),[Measures].[Unit Sales],[Measures].[Store Sales])  

```

1月27日 15时 - 1月27日 15时 


