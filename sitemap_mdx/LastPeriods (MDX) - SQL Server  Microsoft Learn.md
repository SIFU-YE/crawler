#### 通过
# LastPeriods (MDX)
返回指定成员之前（包含该成员）的成员集。
```
  
LastPeriods(Index [ ,Member_Expression ] )  

```

_Index_ 指定期间数的有效数值表达式。
_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
如果指定的周期数为正数， **则 LastPeriods** 函数将返回一组成员，这些成员从指定的成员表达式中滞后 _于 Index_ - 1 的成员开始，以指定成员结尾。 函数返回的成员数等于 _Index_ 。
如果指定的句点数为负数， **则 LastPeriods** 函数返回一组成员，这些成员以指定成员开头，以从指定成员 ( - _索引_ - 1) 的成员结束。 函数返回的成员数等于 _Index_ 的绝对值。
如果指定的周期数为零， **LastPeriods** 函数将返回空集。 这与 **Lag** 函数不同，后者在指定 0 时返回指定成员。
如果未指定成员， **LastPeriods** 函数将使用 **Time.CurrentMember** 。 如果没有任何一个维度标记为 Time 维度，该函数将在不发生错误的情况下分析并执行，但将导致客户端应用程序出现单元错误。
下面的示例返回 2002 会计年度第二、第三和第四会计季度的默认度量值。
```
SELECT LastPeriods(3,[Date].[Fiscal].[Fiscal Quarter].[Q4 FY 2002]) ON 0  
FROM [Adventure Works]  

```

此示例还可以用 :（冒号）运算符编写：
`[Date].[Fiscal].[Fiscal Quarter].[Q4 FY 2002]: [Date].[Fiscal].[Fiscal Quarter].[Q2 FY 2002]`
下面的示例返回 2002 会计年度第一会计季度的默认度量值。 虽然指定的期间数为三个，但是只能返回一个，因为该会计年度中没有更早的期间。
```
SELECT LastPeriods  
   (3,[Date].[Fiscal].[Fiscal Quarter].[Q1 FY 2002]  
   ) ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


