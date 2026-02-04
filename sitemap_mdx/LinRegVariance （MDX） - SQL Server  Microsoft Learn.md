#### 通过
# LinRegVariance （MDX）
计算集的线性回归，并返回与回归线关联的方差，y = ax + b。
```
  
LinRegVariance(Set_Expression, Numeric_Expression_y [ ,Numeric_Expression_x ] ] )  

```

_Set_Expression_ 返回集的有效多维表达式 （MDX） 表达式。
_Numeric_Expression_y_ 一个有效的数值表达式，它通常是单元格坐标的多维表达式（MDX）表达式，该表达式返回一个数字，表示 y 轴的值。
_Numeric_Expression_x_ 一个有效的数值表达式，该表达式通常是单元格坐标的多维表达式（MDX）表达式，该表达式返回一个表示 x 轴值的数字。
使用最小平方方法的线性回归计算回归线的公式（即一系列点的最佳拟合线）。 回归线具有以下公式，其中 a 是斜率，b 是截距：
y = ax+b
**LinRegVariance** 函数根据第一个数值表达式计算指定的集，以获取 y 轴的值。 然后，该函数根据第二个数值表达式（如果指定）计算指定的集，以获取 x 轴的值。 如果未指定第二个数值表达式，该函数将使用指定集中单元格的当前上下文作为 x 轴的值。 不指定 x 轴参数经常与时间维度一起使用。
获取点集后，**LinRegVariance** 函数返回描述线性公式拟合到点的统计方差。
linRegVariance 函数 忽略包含文本或逻辑值的空单元格或单元格。 但是，该函数包含值为零的单元格。
以下示例将描述线性公式拟合的统计方差返回单位销售额和商店销售度量值的点。
```
LinRegVariance(LastPeriods(10),[Measures].[Unit Sales],[Measures].[Store Sales])  

```

1月27日 15时 - 1月27日 15时 


