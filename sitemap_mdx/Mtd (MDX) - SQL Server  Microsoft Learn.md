#### 通过
# Mtd (MDX)
按照时间维度中的年级别的约束，从给定成员所在的级别返回一组同级成员，从第一个同级成员开始到给定成员为止。
```
  
Mtd( [ Member_Expression ] )  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
如果未指定成员表达式，则默认值为第一个层次结构的当前成员，度量值组中第一个维度中的 _Time_ 类型为 _Month_ 。
当级别所基于的属性层次结构的 Type 属性设置为 Months 时，**Mtd** 函数是 PeriodsToDate 函数的 _快捷方式函数。_ 也就是说，`Mtd(Member_Expression)` 等效于 `PeriodsToDate(Month_Level_Expression,Member_Expression)`。
下例将返回 2002 年 7 月（截止于 2002 年 7 月 20 日）Internet 销售的当月运费成本总和。
```
WITH MEMBER Measures.x AS SUM   
   (  
      MTD([Date].[Calendar].[Date].[July 20, 2002])  
     , [Measures].[Internet Freight Cost]  
     )  
SELECT Measures.x ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


