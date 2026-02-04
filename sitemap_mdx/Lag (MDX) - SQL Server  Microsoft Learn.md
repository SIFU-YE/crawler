#### 通过
# Lag (MDX)
返回在成员级别中比指定成员位置靠前且靠前位数为指定位数的成员。
```
  
Member_Expression.Lag(Index)   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Index_ 指定成员位置滞后位数的有效数值表达式。
级别内的成员位置由属性层次结构的自然顺序决定。 位置的编号从零开始。
如果指定的延迟为零， **则 Lag** 函数返回指定的成员本身。
如果指定的滞后时间为负值， **则 Lag** 函数将返回后续成员。
`Lag(1)` 等效于 PrevMember 函数。 `Lag(-1)` 等效于 NextMember 函数。
**Lag** 函数类似于 Lead 函数，只是 **Lead** 函数看起来与 **Lag** 函数相反。 也就是说，`Lag(n)` 等效于 `Lead(-n)`。
下例将返回 2001 年 12 月的值：
```
SELECT [Date].[Fiscal].[Month].[February 2002].Lag(2) ON 0  
FROM [Adventure Works]  
  

```

下例将返回 2002 年 3 月的值：
```
SELECT [Date].[Fiscal].[Month].[February 2002].Lag(-1) ON 0  
FROM [Adventure Works]  
  

```

1月27日 15时 - 1月27日 15时 


