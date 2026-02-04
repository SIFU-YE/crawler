#### 通过
# Descendants (MDX)
返回成员在指定级别或距离上的后代集，可以选择包括或不包括其他级别的后代。
```
  
Member expression syntax using a level expression  
Descendants(Member_Expression [ , Level_Expression [ ,Desc_Flag ] ] )  
  
Member expression syntax using a numeric expression  
Descendants(Member_Expression [ , Distance [ ,Desc_Flag ] ] )  
  
Set expression syntax using a level expression  
Descendants(Set_Expression [ , Level_Expression [ ,Desc_Flag ] ] )  
  
Member expression syntax using a numeric expression  
Descendants(Set_Expression [ , Distance [ ,Desc_Flag ] ] )  
  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
_距离_ 指定与指定成员距离的有效数值表达式。
_Desc_Flag_ 指定用于区分可能后代集的说明标志的有效字符串表达式。
如果指定了级别， **则 Descendants** 函数返回一个集，该集包含指定成员的后代或指定集的成员（在指定级别），可以选择由 _Desc_Flag_ 中指定的标志修改。
如果指定 _了 Distance_ ， **则 Descendants** 函数将返回一个集，该集包含指定成员的后代或指定集的成员，这些成员是指定成员层次结构中指定级别数（可选）由 _Desc_Flag_ 中指定的标志修改。 通常情况下，此函数与 Distance 参数一同用于处理不规则的层次结构。 如果指定距离为零 (0)，该函数将返回仅由指定的成员或指定的集组成的集。
如果指定了集表达式，则会为集的每个成员单独解析 **后代** 函数，并再次创建该集。 换句话说，用于 **子代** 函数的语法在功能上等效于 MDX Generate 函数。
如果未指定级别或距离，则函数使用的级别的默认值通过调用 Level 函数 (<<Member>> 来确定。指定成员的级别) (如果) 指定了成员，或者通过调用指定集的每个成员的 **Level** 函数 (如果) 指定集。 如果未指定级别表达式、距离或标志，此函数将在假定使用了以下语法的情况下执行操作：
```
Descendants  
(  
Member_Expression ,  
Member_Expression.Level ,  
SELF_BEFORE_AFTER  
)  

```

如果指定了级别但未指定说明标志，此函数将在假定使用了以下语法的情况下执行操作：
```
Descendants  
(  
Member_Expression ,  
Level_Expression,  
SELF  
)  

```

通过更改说明标志的值，可以包括或排除位于指定级别或指定距离处的后代、位于指定级别或距离之前或之后（直到叶节点为止）的子成员以及位于任何级别或距离的叶子成员。 下表描述了 _Desc_Flag_ 参数中允许的标志。
SELF | 仅返回指定级别或指定距离处的后代成员。 如果指定级别为指定成员所在的级别，该函数将包括指定成员。  
---|---  
AFTER | 返回指定级别或指定距离处的所有从属级别的后代成员。  
BEFORE | 返回指定成员和指定级别之间或指定距离内所有级别的后代成员。 它包括指定成员，但不包括指定级别或距离的成员。  
BEFORE_AND_AFTER | 返回指定成员所在级别的所有从属级别的后代成员。 它包括指定成员，但不包括指定级别或指定距离处的成员。  
SELF_AND_AFTER | 返回指定级别或指定距离内的后代成员，以及指定级别或指定距离内的所有从属级别的后代成员。  
SELF_AND_BEFORE | 返回指定级别或指定距离内的后代成员，以及指定成员和指定级别之间或指定距离内所有级别的后代成员（包括指定成员）。  
SELF_BEFORE_AFTER | 返回指定成员所在级别的所有从属级别的后代成员（包括指定成员）。  
LEAVES | 返回指定成员和指定级别之间或指定距离内的叶后代成员。  
下面的示例返回指定成员 (United States) 以及指定成员 (United States) 和指定级别 (City) 前一个级别的成员之间的成员。该示例返回指定成员 (United States) 本身以及 State-Province 级别（City 级别的前一个级别）的成员. 此示例包括注释参数，使您可以轻松地测试此函数的其他参数。
```
SELECT Descendants  
   ([Geography].[Geography].[Country].&[United States]  
      //, [Geography].[Geography].[Country]  
   , [Geography].[Geography].[City]  
      //, [Geography].[Geography].Levels (3)  
      //, SELF   
      //, AFTER  
      , BEFORE  
      // BEFORE_AND_AFTER  
      //, SELF_AND_AFTER  
      //, SELF_AND_BEFORE  
      //,SELF_BEFORE_AFTER  
      //,LEAVES   
   ) ON 0  
FROM [Adventure Works]   

```

以下示例从 **Adventure Works** 多维数据集返回度量值的`Measures.[Gross Profit Margin]`每日平均值，该平均值在 2003 会计年度中每个月的天数中计算得出。 **Descendants** 函数返回一组从层次结构的当前成员确定的`[Date].[Fiscal]`天数。
```
WITH MEMBER Measures.[Avg Gross Profit Margin] AS Avg  
   (  
      Descendants( [Date].[Fiscal].CurrentMember,   
           [Date].[Fiscal].[Date]  
          ),   
        Measures.[Gross Profit Margin]  
   )  
SELECT  
   Measures.[Avg Gross Profit Margin] ON COLUMNS,  
   [Date].[Fiscal].[Month].Members ON ROWS  
FROM [Adventure Works]  
WHERE ([Date].[Fiscal Year].&[2003])  

```

以下示例使用水平表达式并返回澳大利亚每个State-Province的 Internet 销售金额，并返回每个省/自治区/直辖市的澳大利亚 Internet 销售总额的百分比。 此示例使用 Item 函数从 **上级** 函数返回的集中提取第一个 (，并且仅) 元组。
```
WITH MEMBER Measures.x AS   
   [Measures].[Internet Sales Amount] /   
   ( [Measures].[Internet Sales Amount],  
      Ancestors   
         ( [Customer].[Customer Geography].CurrentMember,   
           [Customer].[Customer Geography].[Country]  
         ).Item (0)  
   ), FORMAT_STRING = '0%'  
SELECT {[Measures].[Internet Sales Amount], Measures.x} ON 0,  
{Descendants   
   ( [Customer].[Customer Geography].[Country].&[Australia],   
     [Customer].[Customer Geography].[State-Province], SELF   
   )    
} ON 1  
FROM [Adventure Works]  
  

```

1月27日 15时 - 1月27日 15时 


