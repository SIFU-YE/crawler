#### 通过
# DrilldownLevelBottom (MDX)
将集中某一指定级别上的最底层成员深化到下一个级别。
```
DrilldownLevelBottom(Set_Expression, Count [,[<Level_Expression>] [,[<Numeric_Expression>][,INCLUDE_CALC_MEMBERS]]])  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Count_ 指定要返回的元组数的有效数值表达式。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
_Numeric_Expression_ 可选。 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
_Include_Calc_Members_ 可选。 将计算成员添加到深化结果的关键字。
如果指定了数值表达式， **则 DrilldownLevelBottom** 函数会根据指定值，按对子成员集的计算结果，按升序对指定集中每个成员的子级进行排序。 如果未指定数值表达式，则此函数根据由查询上下文决定的子成员集所表示的单元的值，对指定的集中每个成员的子成员按升序排序。此行为类似于 BottomCount 和 Tail (MDX) 函数，都以自然顺序返回一组成员，没有任何排序。
排序后， **DrilldownLevelBottom** 函数返回一个集，其中包含父成员以及 _Count_ 中指定的子成员数，值为最小值。
**DrilldownLevelBottom** 函数类似于 DrilldownLevel 函数，但 **DrilldownLevelBottom** 函数返回最底层的子成员数，而不是包括指定级别的每个成员的所有子成员。
通过查询 XMLA 属性 MdpropMdxDrillFunctions，可以验证服务器为钻取函数提供的支持级别;有关详细信息 ，请参阅 XMLA) (支持的 XMLA 属性  。
下面的示例将根据默认度量值返回产品类别级别的最后三个子成员。 在 Adventure Works 示例多维数据集中，Accessories 的最后三个子成员是 Tires and Tubes、Pumps 和 Panniers。 在 Management Studio 的 MDX 查询窗口中，你可导航到“产品 | 产品类别 | 成员 | 所有产品 | 附件”查看完整的列表。 你可增加计数参数以返回更多成员。
```
SELECT DrilldownLevelBottom   
   ([Product].[Product Categories].children,  
   3,  
   [Product].[Product Categories].[Category])  
   ON 0  
   FROM [Adventure Works]  

```

下一个示例演示如何使用 **include_calc_members** 标志，该标志用于在向下钻取级别中包含计算成员。 度量值 [Reseller Order Count] 将添加到 **DrilldownLevelBottom** 语句，以确保按该度量值对结果进行排序。 要查看计算成员，必须将计数至少增加到 9。
```
WITH MEMBER   
[Product].[Product Categories].[Category].&[3].[Premium Clothes] AS  
[Product].[Product Categories].[Subcategory].&[18] +  
[Product].[Product Categories].[Subcategory].&[21]  
SELECT [Measures].[Reseller Order Count] ON 0,  
DRILLDOWNLEVELBOTTOM(  
  [Product].[Product Categories].children ,  
  9,  
  [Product].[Product Categories].[Category] ,  
  [Measures].[Reseller Order Count],  
  INCLUDE_CALC_MEMBERS ) ON 1  
FROM [Adventure Works]  

```

DrilldownLevel (MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


