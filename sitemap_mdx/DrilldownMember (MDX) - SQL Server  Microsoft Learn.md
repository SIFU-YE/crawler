#### 通过
# DrilldownMember (MDX)
深化第一个指定集与第二个指定集的交集中的成员。
该函数也可以通过使用第一个元组层次结构或者可选的指定层次结构，对一组元组进行深化。
```
  
DrillDownMember(<Set_Expression1>, <Set_Expression2> [,[<Target_Hierarchy>]] [,[RECURSIVE][,INCLUDE_CALC_MEMBERS]])  

```

_Set_Expression1_ 返回集的有效多维表达式 (MDX)。
_Set_Expression2_ 返回集的有效多维表达式 (MDX)。
_Target_Hierarchy_ 返回层次结构的有效多维表达式 (MDX)。
_递 归_ 指示集的递归比较的关键字。
_Include_Calc_Members_ 用于使计算成员能够包括在深化结果中的关键字。
该函数返回按层次结构排序的子成员集，并包括第一个集和第二个集的交集中的成员。 如果第一个集包含父成员以及一个或多个子成员，则不深化父成员。 第一个集可以具有任何维数，但第二个集必须包含一个一维集。 第一个集中的原始成员的顺序将保留，只不过该函数的结果集中包含的所有子成员都紧随在它们的父成员之后。 该函数将通过检索第一个集与第二个集的交集中的每个成员的子成员来构造结果集。 如果指定了 **RECURSIVE** ，该函数将继续以递归方式将结果集的成员与第二个集进行比较，检索结果集中也存在于第二个集中的每个成员的子级，直到在第二个集中找不到结果集中的更多成员。
通过查询 XMLA 属性 **MdpropMdxDrillFunctions** ，可以验证服务器为钻取函数提供的支持级别;有关详细信息 ，请参阅 XMLA) (支持的 XMLA 属性  。
第一个集可以包含元组，但不能包含成员。 对元组的深化是一种 OLE DB 扩展，这种深化将返回元组集而非成员集。
当成员后面紧跟其子成员之一时，将不会深化该成员。 成员集中成员的顺序对于 Drilldown* 和 Drillup* 系列的函数非常重要。
下例深化了 Australia 成员，它是第一个集与第二个集的交集成员。
```
SELECT DrilldownMember   
   ( [Geography].[Geography].Children,  
      {[Geography].[Geography].[Country].[Australia],  
        [Geography].[Geography].[State-Province].[New South Wales]}  
   )  
   ON 0  
   FROM [Adventure Works]  

```

下例深化了 Australia 成员，它是第一个集与第二个集的交集成员。 但是，由于指定了 RECURSIVE 参数，该函数会继续将结果集的成员（State-Province 级别的成员）与第二个集中的成员进行递归比较，检索结果集（City 级别的成员）与第二个集的交集中的每个成员的子成员，直到找遍结果集与第二个集的交集中的成员为止。
```
SELECT DrilldownMember   
   ( [Geography].[Geography].Children,  
      {[Geography].[Geography].[Country].[Australia],  
        [Geography].[Geography].[State-Province].[New South Wales]}  
   ,RECURSIVE)  
   ON 0  
   FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


