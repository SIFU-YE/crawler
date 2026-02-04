#### 通过
# Ytd (MDX)
返回一组与给定成员相同的级别的同级成员，从第一个同级成员开始，以给定成员结尾，受“时间”维度中的 _“年_ ”级别的约束。
```
  
Ytd( [ Member_Expression ] )  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
如果未指定成员表达式，则默认值为第一个层次结构的当前成员，在度量值组中，第一个维度为 _Time_ 类型，其级别为 _Years_ 。
**Ytd** 函数是 PeriodsToDate 函数的快捷方式函数，其中级别所基于的属性层次结构的 Type 属性设置为 _Years_ 。 也就是说，`Ytd(Member_Expression)` 等效于 `PeriodsToDate(Year_Level_Expression,Member_Expression)`。 请注意，当 Type 属性设置为 _FiscalYears_ 时，此函数将不起作用。
以下示例从 **Adventure Works** 多维数据集返回在维度中包含的 `Date` 2003 日历年头 8 个月聚合的成员之和`Measures.[Order Quantity]`。
```
WITH MEMBER [Date].[Calendar].[First8MonthsCY2003] AS  
    Aggregate(  
        YTD([Date].[Calendar].[Month].[August 2003])  
    )  
SELECT   
    [Date].[Calendar].[First8MonthsCY2003] ON COLUMNS,  
    [Product].[Category].Children ON ROWS  
FROM  
    [Adventure Works]  
WHERE  
    [Measures].[Order Quantity]  

```

**Ytd** 经常与未指定参数结合使用，这意味着 CurrentMember (MDX)  函数将在报表中显示正在运行的累计年份至今总计，如以下查询所示：
```
WITH MEMBER MEASURES.YTDDEMO AS  
AGGREGATE(YTD(), [Measures].[Internet Sales Amount])  
SELECT {[Measures].[Internet Sales Amount], MEASURES.YTDDEMO} ON 0,  
[Date].[Calendar].MEMBERS ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


