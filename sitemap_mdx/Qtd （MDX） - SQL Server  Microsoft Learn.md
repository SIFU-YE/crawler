#### 通过
# Qtd （MDX）
返回一组与给定成员相同的级别的同级成员，从第一个同级开始，以给定成员结尾，受时间维度中 _季度_ 级别的约束。
```
  
Qtd( [ Member_Expression ] )  

```

_Member_Expression_ 返回成员的有效多维表达式 （MDX） 表达式。
如果未指定成员表达式，则默认值为第一个层次结构的当前成员，其类型为 _季度_ 类型 _度量值组中第一个时间_ 类型的第一个维度。
**Qtd** 函数是 PeriodsToDate （MDX） 函数的快捷函数，其级别表达式参数设置为 _Quarter_ 。 也就是说，`Qtd(Member_Expression)` 在功能上等效于 `PeriodsToDate(Quarter_Level_Expression, Member_Expression)`。
以下示例从 adventure Works 多维数据集返回  成员的总和，该  维度中包含的日历年第三季度的前两个月的总和。
```
WITH MEMBER [Date].[Calendar].[First2MonthsSecondSemester2003] AS  
    Aggregate(  
        QTD([Date].[Calendar].[Month].[August 2003])  
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


