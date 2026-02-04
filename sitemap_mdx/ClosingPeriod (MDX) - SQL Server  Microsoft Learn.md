#### 通过
# ClosingPeriod (MDX)
返回指定成员在指定级别的后代中的最后一个同级成员。
```
  
ClosingPeriod( [ Level_Expression [ ,Member_Expression ] ] )  

```

_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
此函数主要用于具有 Time 类型的维度，但也可用于任何维度。
  * 如果指定了级别表达式， **则 ClosingPeriod** 函数使用包含指定级别的维度，并返回指定级别的默认成员后代中的最后一个同级。
  * 如果同时指定了级别表达式和成员表达式， **则 ClosingPeriod** 函数将返回指定级别的指定成员后代之间的最后一个同级。
  * 如果未指定级别表达式和成员表达式， **则 ClosingPeriod** 函数将使用维度的默认级别和成员 (如果多维数据集中具有时间类型的任何) 。


**ClosingPeriod** 函数等效于以下 MDX 语句：
`Tail(Descendants(Member_Expression, Level_Expression), 1)`.
OpeningPeriod 函数类似于 **ClosingPeriod** 函数，只不过 **OpeningPeriod** 函数返回第一个同级而不是最后一个同级。
下面的示例返回 Date 维度（具有 Time 语义类型）的“FY2007”成员的默认度量值。 返回此成员是因为：“会计年度”级别是“(全部)”级别的第一个后代；“Fiscal”层次结构是默认层次结构（因为它是层次结构集合中的第一个用户定义的层次结构）；而且“FY 2007”成员是此层次结构在此级别处的最后一个同级成员。
```
SELECT ClosingPeriod() ON 0  
FROM [Adventure Works]  

```

下面的示例返回“November 30, 2006”成员在 Date.Date 属性层次结构的 Date.Date.Date 级别处的默认度量值。 此成员是 Date.Date 属性层次结构中“(全部)”级别的后代的最后一个同级成员。
```
SELECT ClosingPeriod ([Date].[Date].[Date]) ON 0  
FROM [Adventure Works]  

```

下例返回“December, 2003”成员的默认度量值。该成员是用户定义的层次结构“Calendar”中年份级别成员“2003”的后代的最后一个同级成员。
```
SELECT ClosingPeriod ([Date].[Calendar].[Month],[Date].[Calendar].[Calendar Year].&[2003]) ON 0  
FROM [Adventure Works]  

```

下面的示例返回“June, 2003”成员的默认度量值，该成员是用户定义的层次结构“Fiscal”中年份级别成员“2003”的后代的最后一个同级成员。
```
SELECT ClosingPeriod ([Date].[Fiscal].[Month],[Date].[Fiscal].[Fiscal Year].&[2003]) ON 0  
FROM [Adventure Works]  

```

OpeningPeriod (MDX) MDX 函数参考 (MDX) LastSibling (MDX)
1月27日 15时 - 1月27日 15时 


