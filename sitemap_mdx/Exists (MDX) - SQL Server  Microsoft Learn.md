#### 通过
# Exists (MDX)
返回与第二个指定集的一个或多个元组共存的第一个指定集中的元组集。 该函数手动执行自动 Exists 以自动方式执行的操作。 有关自动存在的详细信息，请参阅 MDX (Analysis Services) 中的关键概念 。
如果提供了可选的 <度量值组名称> ，则函数返回与第二个集中的一个或多个元组以及指定度量值组的事实数据表中具有关联行的元组。
```
  
Exists( Set_Expression1 , Set_Expression2 [, MeasureGroupName] )  

```

_Set_Expression1_ 返回集的有效多维表达式 (MDX)。
_Set_Expression2_ 返回集的有效多维表达式 (MDX)。
_MeasureGroupName_ 指定度量值组名称的有效字符串表达式。
  1. 当指定 MeasureGroupName 参数时，包含包含 null 值的度量值的度量值组行会导致 **Exists** 。 这是这种形式的 Exists 和 Nonempty 函数之间的区别：如果这些度量值的 NullProcessing 属性设置为 Preserve，这意味着当针对多维数据集的该部分运行查询时，度量值将显示 Null 值;NonEmpty 将始终从具有 Null 度量值的集中删除元组，而具有 MeasureGroupName 参数的 Exists 不会筛选具有关联度量值组行的元组，即使度量值为 Null 也是如此。
  2. 如果使用 _MeasureGroupName_ 参数，则结果将取决于引用的度量值组中是否存在可见度量值;如果引用的度量值组中没有可见度量值，则无论 _Set_Expression1_ 和 _Set_Expression2_ 的值如何，EXISTS 都将始终返回空集。


居住在加利福尼亚的客户：
```
SELECT [Measures].[Internet Sales Amount] ON 0,  
EXISTS(  
[Customer].[Customer].[Customer].MEMBERS  
, {[Customer].[State-Province].&[CA]&[US]}  
) ON 1   
FROM [Adventure Works]  
  

```

居住在加利福尼亚并且有销售额的客户：
```
SELECT [Measures].[Internet Sales Amount] ON 0,  
EXISTS(  
[Customer].[Customer].[Customer].MEMBERS  
, {[Customer].[State-Province].&[CA]&[US]}  
, "Internet Sales") ON 1   
FROM [Adventure Works]  
  

```

有销售额的客户：
```
SELECT [Measures].[Internet Sales Amount] ON 0,  
EXISTS(  
[Customer].[Customer].[Customer].MEMBERS  
, , "Internet Sales") ON 1   
FROM [Adventure Works]  
  

```

购买了自行车的客户：
```
SELECT [Measures].[Internet Sales Amount] ON 0,  
EXISTS(  
[Customer].[Customer].[Customer].MEMBERS  
, {[Product].[Product Categories].[Category].&[1]}  
, "Internet Sales") ON 1   
FROM [Adventure Works]  

```

MDX 函数参考 (MDX) Crossjoin (MDX) NonEmptyCrossjoin (MDX) NonEmpty (MDX) IsEmpty (MDX)
1月27日 15时 - 1月27日 15时 


