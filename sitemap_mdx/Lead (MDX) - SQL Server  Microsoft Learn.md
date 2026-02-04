#### 通过
# Lead (MDX)
返回在成员级别中比指定成员位置靠后且靠后位数为指定位数的成员。
```
  
Member_Expression.Lead( Index )  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Index_ 指定成员位置位数的有效数值表达式。
级别内的成员位置由属性层次结构的自然顺序决定。 位置的编号从零开始。
如果指定的潜在顾客为零 (0) ， **则 Lead** 函数返回指定的成员。
如果指定的潜在顾客为负数， **则 Lead** 函数返回以前的成员。
`Lead(1)` 等效于 NextMember 函数。 `Lead(-1)` 等效于 PrevMember 函数。
**Lead** 函数类似于 Lag 函数，只是 **Lag** 函数看起来与 **Lead** 函数相反。 也就是说，`Lead(n)` 等效于 `Lag(-n)`。
下例将返回 2001 年 12 月的值：
```
SELECT [Date].[Fiscal].[Month].[February 2002].Lead(-2) ON 0  
FROM [Adventure Works]  
  

```

下例将返回 2002 年 3 月的值：
```
SELECT [Date].[Fiscal].[Month].[February 2002].Lead(1) ON 0  
FROM [Adventure Works]  
  

```

1月27日 15时 - 1月27日 15时 


