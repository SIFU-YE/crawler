#### 通过
# ValidMeasure (MDX)
在返回指定元组的结果时，通过将不适用的维度强制到“全部”级别（如果是不可聚合的，则为默认成员）来返回多维数据集中的度量值。
```
  
ValidMeasure(Tuple_Expression)   

```

_Tuple_Expression_ 返回元组的有效多维表达式 (MDX)。
**ValidMeasure** 函数返回元组的值，忽略与该元组返回值的 Measure 的度量值组没有关系的属性。 出于以下两个原因，属性可与度量值无关：
  * 属性的维度与元组中度量值的度量值组无关。
  * 属性的维度与度量值的度量值组无关，但粒度属性不是键属性，并且粒度属性与元组中的属性没有直接关系。


此函数指定的行为是默认服务器端行为，由度量值组对象上的 **IgnoreUnrelatedDimensions** 属性控制。
对于具有粒度的指定元组中的每个属性（也就是说，元组中的成员不是“全部”成员），其当前坐标按如下方式移动：
  * 与指定属性成员相关的属性移动至与当前成员共存的成员。
  * 与指定属性成员相关的属性移动至“全部”成员（如果层次结构是不可聚合的，则为默认成员）。
  * 不相关的属性移动至“全部”成员（根据度量值）。


下面的查询显示如何使用 ValidMeasure 函数来覆盖 IgnoreUnrelatedDimensions 属性的行为。 在 Adventure Works 多维数据集中，Sales Targets 度量值组将 IgnoreUnrelatedDimensions 设置为 False；因为 Date 维度在 Calendar Quarter 粒度联接到此度量值组，所以这意味着，Sales Quota 度量值默认情况下将在 Calendar Quarter 下返回 Null（尽管在 MDX 脚本中也存在将值向下分配给 Month 级别的计算）。 在计算度量值中使用 ValidMeasure 函数可用于使 Sales Quota 度量值的行为就像 IgnoreUnrelatedDimensions 设置为 True 一样并且强制 Sales Quota 显示当前 Calendar Quarter 的值。
```
WITH MEMBER MEASURES.VTEST AS VALIDMEASURE([Measures].[Sales Amount Quota])  
SELECT {[Measures].[Sales Amount Quota], MEASURES.VTEST} ON 0,  
[Date].[Calendar].MEMBERS ON 1  
FROM [Adventure Works]  

```

同样，Sales Targets 度量值组与 Promotion 维度完全没有任何关系，因此，在 Promotion 上任何层次结构的“全部”成员之下，它将返回 Null。 此外，可以通过使用 ValidMeasure 更改此行为：
```
WITH MEMBER MEASURES.VTEST AS VALIDMEASURE([Measures].[Sales Amount Quota])  
SELECT {[Measures].[Sales Amount Quota], MEASURES.VTEST} ON 0,  
[Promotion].[Promotions].members ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


