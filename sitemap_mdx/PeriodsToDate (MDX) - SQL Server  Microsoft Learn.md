#### 通过
# PeriodsToDate (MDX)
按照时间维度中的指定级别的约束，从给定成员所在的级别返回一组同级成员，从第一个同级成员开始到给定成员为止。
```
  
PeriodsToDate( [ Level_Expression [ ,Member_Expression ] ] )  

```

_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
在指定级别的范围内， **PeriodsToDate** 函数返回与指定成员相同的级别的句点集，从第一个句点开始，以指定成员结束。
  * 如果指定了级别，则层次结构的当前成员是推断 _层次结构_ 。**CurrentMember** ，其中 _层次结构_ 是指定级别的层次结构。
  * 如果未指定级别和成员，则级别是度量值组中第一个维度 Time 类型的第一个层次结构的当前成员的父级别。


`PeriodsToDate( Level_Expression, Member_Expression )` 的功能与以下 MDX 表达式相同：
`TopCount(Descendants(Ancestor(Member_Expression, Level_Expression), Member_Expression.Level), 1):Member_Expression`
以下示例从 **Adventure Works** 多维数据集返回在维度中包含的 `Date` 2003 日历年头 8 个月聚合的成员之和`Measures.[Order Quantity]`。
```
WITH MEMBER [Date].[Calendar].[First8Months2003] AS  
    Aggregate(  
        PeriodsToDate(  
            [Date].[Calendar].[Calendar Year],   
            [Date].[Calendar].[Month].[August 2003]  
        )  
    )  
SELECT   
    [Date].[Calendar].[First8Months2003] ON COLUMNS,  
    [Product].[Category].Children ON ROWS  
FROM  
    [Adventure Works]  
WHERE  
    [Measures].[Order Quantity]  

```

下面的示例对 2003 日历年第二个半期的前两个月聚合。
```
WITH MEMBER [Date].[Calendar].[First2MonthsSecondSemester2003] AS  
    Aggregate(  
        PeriodsToDate(  
            [Date].[Calendar].[Calendar Semester],   
            [Date].[Calendar].[Month].[August 2003]  
        )  
    )  
SELECT   
    [Date].[Calendar].[First2MonthsSecondSemester2003] ON COLUMNS,  
    [Product].[Category].Children ON ROWS  
FROM  
    [Adventure Works]  
WHERE  
    [Measures].[Order Quantity]  

```

1月27日 15时 - 1月27日 15时 


