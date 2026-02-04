#### 通过
# ToggleDrillState (MDX)
在成员之间切换深化模式和浅化模式的状态。
```
  
ToggleDrillState(Set_Expression1,Set_Expression2 [, [RECURSIVE] [,INCLUDE_CALC_MEMBERS] ] )  

```

_Set_Expression1_ 返回集的有效多维表达式 (MDX)。
_Set_Expression2_ 返回集的有效多维表达式 (MDX)。
_递 归_ （可选）。 指示集的递归比较的关键字。 **ToggleDrillState** 函数是 **DrillupMember** 和 **DrilldownMember** 函数的组合。 仅当成员处于 **DrilldownMember** 状态时，递归才适用。
_Include_calc_members_ （可选）。 指示是否在深化级别包括计算成员（如果存在）的标志。
**ToggleDrillState** 函数切换第一个集中存在的第二个集的每个成员的钻取状态。 第一个集可以包含任意维数的元组，但是第二个集必须包含单个维度的成员。 **ToggleDrillState** 函数是 **DrillupMember** 和 **DrilldownMember** 函数的组合。 如果第二个集的成员 _m_ 存在于第一个集中，并且该成员向下钻取 (也就是说，紧跟) 后有一个后代，则 `DrillupMember(Set_Expression1, {m})` 应用于第一个集中的成员或元组。 如果该 _m_ 成员 (即向上钻取，则没有紧跟 _m) 的_`DrilldownMember(Set_Expression1, {m}[, RECURSIVE])` m 后代应用于第一
如果使用可选的 **RECURSIVE** 标志，则以递归方式应用向上钻取和向下钻取。 有关递归标志的详细信息，请参阅 DrillupMember 和 DrilldownMember 函数。
通过查询 XMLA 属性 MdpropMdxDrillFunctions，可以验证服务器为钻取函数提供的支持级别;有关详细信息，请参阅 XMLA (支持的 XMLA 属性)  。
有关涉及此函数的方案和示例，请参阅 数据库日志：MDX Set 函数：ToggleDrillState () 函数 。
下例对第一个集中的澳大利亚成员进行深化，而对第一个集中的美国成员进行浅化。
```
SELECT ToggleDrillState  
   ({[Geography].[Geography].[Country].Members, [Geography].[Geography].[Country].&[United States].Children},  
      {[Geography].[Geography].[Country].[Australia]  
      , [Geography].[Geography].[Country].&[United States]}  
      --, recursive  
      --, include_calc_members  
   ) ON 0  
   FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


