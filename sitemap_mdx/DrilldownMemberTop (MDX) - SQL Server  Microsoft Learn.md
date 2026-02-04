#### 通过
# DrilldownMemberTop (MDX)
深化第一个指定集与第二个指定集的交集中的成员，并将结果集的成员数限制为指定数目。 或者，此函数使用第一个元组层次结构或可选的指定层次结构向下钻取一组元组。
```
  
DrillDownMemberTop(<Set_Expression1>, <Set_Expression2>, <Count> [,[<Numeric_Expression>] [,[<Hierarchy>]] [,[RECURSIVE][,INCLUDE_CALC_MEMBERS]]])  

```

_Set_Expression1_ 返回集的有效多维表达式 (MDX)。
_Set_Expression2_ 返回集的有效多维表达式 (MDX)。
_Count_ 指定要返回的元组数的有效数值表达式。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
_层次结构_ 返回层次结构的有效多维表达式 (MDX)。
_递 归_ 指示集的递归比较的关键字。
_Include_Calc_Members_ 用于使计算成员能够包括在深化结果中的关键字。
如果指定了数值表达式， **则 DrilldownMemberTop** 函数会根据数值表达式的值，按对子成员集的计算结果，按降序排序第一个集中每个成员的子级。 如果未指定数值表达式，则此函数根据由查询上下文确定的子成员集所表示的单元值，对第一个集中每个成员的子成员按降序排序。 此行为类似于 TopCount 和 Head (MDX) 函数，都以自然顺序返回一组成员，没有任何排序。
排序后， **DrilldownMemberTop** 函数返回一个集，该集包含父成员和 Count 中指定的子成员数 _，_ 具有最大值，并且包含在两个集中。
如果指定 **了 RECURSIVE** ，则该函数按前面所述对第一个集进行排序，然后递归方式将第一个集的成员与第二个集进行比较（按层次结构中组织）。 函数检索第一个集中每个成员的最顶层子级数，该成员也存在于第二个集中。
第一个集可以包含元组，但不能包含成员。 元组的深化是 OLE DB 的扩展，它返回元组集而非成员集。
**DrilldownMemberTop** 函数类似于 DrilldownMember 函数，但 **DrilldownMemberTop** 函数返回每个成员的最顶层子成员数，而不是包括第一个集中的每个成员的所有子成员（也存在于第二个集中）。
通过查询 XMLA 属性 MdpropMdxDrillFunctions，可以验证服务器为钻取函数提供的支持级别;有关详细信息 ，请参阅 XMLA) (支持的 XMLA 属性  。
下例深化了服装类别，返回已发货订单数量最多的三个服装子类别。
```
SELECT DrilldownMemberTop   ({[Product].[Product Categories].[All Products],        
[Product].[Product Categories].[Category].Bikes,        
[Product].[Product Categories].[Category].Clothing},     
{[Product].[Product Categories].[Category].Clothing},     
3,     
[Measures].[Reseller Order Quantity])     
ON 0     
FROM [Adventure Works]     
WHERE [Measures].[Reseller Order Quantity]  
  

```

1月27日 15时 - 1月27日 15时 


