#### 通过
# DrilldownLevelTop (MDX)
将集中某一指定级别上最顶端的成员深化到下一个级别。
```
  
DrilldownLevelTop(<Set_Expression>, <Count> [,[<Level_Expression>] [,[<Numeric_Expression>][,INCLUDE_CALC_MEMBERS]]])  
  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Count_ 指定要返回的元组数的有效数值表达式。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
_Include_Calc_Members_ 用于将计算成员添加到深化结果的关键字。
如果指定了数值表达式， **DrilldownLevelTop** 函数会根据数值表达式的值对指定集中每个成员的子级进行降序排序，如对子成员集进行计算。 如果未指定数值表达式，则此函数根据由查询上下文确定的子成员集所表示的单元值，对指定集中每个成员的子成员按降序排序。
排序后， **DrilldownLevelTop** 函数返回一个集，该集包含父成员以及 Count 中指定的子成员数 _，_ 其值为最大值。
**DrilldownLevelTop** 函数类似于 DrilldownLevel 函数，但 **DrilldownLevelTop** 函数不包括指定级别的每个成员的所有子级，而是返回最顶层的子成员数。
通过查询 XMLA 属性 MdpropMdxDrillFunctions，可以验证服务器为钻取函数提供的支持级别;有关详细信息，请参阅 XMLA (支持的 XMLA 属性)  。
下面的示例根据默认度量值返回产品类别级别的前三个子成员。 在 Adventure Works 示例多维数据集中，Accessories 的前三个子成员是Bike Racks、Bike Stands 和 Bottles and Cages。 在 Management Studio 的 MDX 查询窗口中，你可导航到“产品 | 产品类别 | 成员 | 所有产品 | 附件”查看完整的列表。 你可增加计数参数以返回更多成员。
```
SELECT DrilldownLevelTop   
   ([Product].[Product Categories].children,  
   3,  
   [Product].[Product Categories].[Category])  
   ON 0  
   FROM [Adventure Works]  

```

下一个示例演示如何使用 **include_calc_members** 标志，该标志用于在向下钻取级别中包含计算成员。 度量值 [经销商订单计数] 包含在 **DrilldownLevelTop** 语句中，以确保返回值按该度量值排序。
```
WITH MEMBER   
[Product].[Product Categories].[Category].&[3].[Premium Clothes] AS  
[Product].[Product Categories].[Subcategory].&[18] +  
[Product].[Product Categories].[Subcategory].&[21]  
SELECT [Measures].[Reseller Order Count] ON 0,  
DRILLDOWNLEVELTOP(  
  [Product].[Product Categories].children ,  
  2,  
  [Product].[Product Categories].[Category] ,  
  [Measures].[Reseller Order Count],  
  INCLUDE_CALC_MEMBERS ) ON 1  
FROM [Adventure Works]  

```

DrilldownLevel (MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


