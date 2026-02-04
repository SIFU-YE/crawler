#### 通过
# DrilldownMemberBottom (MDX)
深化第一个指定集与第二个指定集的交集中的成员，并将结果集的成员数限制为指定数目。 或者，此函数还可以使用第一个元组层次结构或可选的指定层次结构向下钻取一组元组。
```
  
DrillDownMemberBottom(<Set_Expression1>, <Set_Expression2>, <Count> [,[<Numeric_Expression>] [,[<Hierarchy>]] [,[RECURSIVE][,INCLUDE_CALC_MEMBERS]]])  

```

_Set_Expression1_ 返回集的有效多维表达式 (MDX)。
_Set_Expression2_ 返回集的有效多维表达式 (MDX)。
_Count_ 指定要返回的元组数的有效数值表达式。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
_层次结构_ 返回层次结构的有效多维表达式 (MDX)。
_递 归_ 指示集的递归比较的关键字。
_Include_Calc_Members_ 用于使计算成员能够包括在深化结果中的关键字。
如果指定了数值表达式， **DrilldownMemberBottom** 函数将按升序对第一组成员中的每个成员的子级进行排序，根据数值表达式的值对子成员集进行计算。 如果未指定数值表达式，此函数将根据由查询上下文决定的子成员集所表示的单元的值，对第一个集中每个成员的子成员按升序排序。 此行为类似于 BottomCount 和 Tail (MDX) 函数，都以自然顺序返回一组成员，没有任何排序。
排序后， **DrilldownMemberBottom** 函数返回一个集，该集包含父成员以及 Count 中指定的子成员数，其值最低 _，_ 由两个集包含。
如果指定 **了 RECURSIVE** ，则该函数将按前面所述对第一个集进行排序，然后递归地将第一组的成员（按层次结构中的组织方式）与第二组进行比较。 此函数检索第一个集与第二个集的交集中每个成员的指定数目的最底层子成员。
第一个集可以包含元组，但不能包含成员。 元组的深化是 OLE DB 的扩展，它返回元组集而非成员集。
**DrilldownMemberBottom** 函数类似于 DrilldownMember 函数，但 **DrilldownMemberBottom** 函数不包括第一组成员的所有子级（也存在于第二组），而是返回每个成员最底部的子成员数。
通过查询 XMLA 属性 MdpropMdxDrillFunctions，可以验证服务器为钻取函数提供的支持级别;有关详细信息，请参阅 XMLA (支持的 XMLA 属性)  。
1月27日 15时 - 1月27日 15时 


