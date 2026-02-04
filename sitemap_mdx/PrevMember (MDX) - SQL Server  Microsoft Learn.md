#### 通过
# PrevMember (MDX)
返回指定成员所在级别的上一个成员。
```
  
Member_Expression.PrevMember   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
**PrevMember** 函数返回与指定成员位于同一级别的上一个成员。
以下示例演示了一个简单的查询，该查询使用 **PrevMember** 函数在行轴上的当前成员前面显示成员的名称：
```
WITH MEMBER MEASURES.PREVMEMBERDEMO AS  
[Date].[Calendar].CURRENTMEMBER.PREVMEMBER.NAME  
SELECT MEASURES.PREVMEMBERDEMO ON 0,  
[Date].[Calendar].MEMBERS ON 1  
FROM [Adventure Works]  

```

下面的示例根据用 Aggregate 函数计算、用户选择的 State-Province 成员值，返回上一个时期销售额下滑的分销商的计数。 **Hierarchize** 和 **DrillDownLevel** 函数用于返回 Product 维度中产品类别销售额下降的值。 **PrevMember** 函数用于比较当前时间段与上一个时间段。
```
WITH MEMBER Measures.[Declining Reseller Sales] AS   
   Count(  
      Filter(  
         Existing(Reseller.Reseller.Reseller),   
            [Measures].[Reseller Sales Amount] < ([Measures].[Reseller Sales Amount],  
            [Date].Calendar.PrevMember)  
            )  
         )  
MEMBER [Geography].[State-Province].x AS   
   Aggregate (   
      {[Geography].[State-Province].&[WA]&[US],   
      [Geography].[State-Province].&[OR]&[US] }   
         )  
SELECT NON EMPTY Hierarchize (  
   AddCalculatedMembers (  
      {DrillDownLevel({[Product].[All Products]})}  
         )  
   )  
        DIMENSION PROPERTIES PARENT_UNIQUE_NAME ON COLUMNS   
FROM [Adventure Works]  
WHERE ([Geography].[State-Province].x,   
    [Date].[Calendar].[Calendar Quarter].&[2003]&[4],  
    [Measures].[Declining Reseller Sales])  

```

1月27日 15时 - 1月27日 15时 


