#### 通过
# NonEmptyCrossjoin (MDX)
返回包含一个或多个集的叉积的集，不包括空元组以及无相关事实数据表数据的元组。
```
  
NonEmptyCrossjoin(Set_Expression1 [ ,Set_Expression2,...] [,Count ] )  

```

_Set_Expression1_ 返回集的有效多维表达式 (MDX)。
_Set_Expression2_ 返回集的有效多维表达式 (MDX)。
_Count_ 指定返回集的数量的有效数值表达式。
**NonEmptyCrossjoin** 函数将两个或更多集的交叉乘积作为一个集返回，不包括空元组或没有基础事实数据表提供的数据的元组。 由于 **NonEmptyCrossjoin** 函数的工作原理，系统会自动排除所有计算成员。
如果未指定 _Count_ ，则函数会交叉联接所有指定的集，并从结果集中排除空成员。 如果指定了集的数量，该函数将从第一个指定的集开始，交叉联接指定数量的集。 **NonEmptyCrossjoin** 函数使用在后续指定集中指定但尚未交叉联接的任何剩余集来确定哪些成员在生成的交叉联接集中被视为非空。 **NonEmptyCrossjoin** 函数遵循计算度量**值的NON_EMPTY_BEHAVIOR** 设置。
不推荐使用此函数并且不应使用它，保留此函数仅是为了维护向后兼容性。 相反，应将 Exists (MDX)  函数与度量值组名称参数或 NonEmpty (MDX)  函数一起使用。
1月27日 15时 - 1月27日 15时 


