#### 通过
# Aggregate (MDX)
返回一个数字，该数字是通过对集表达式返回的单元进行聚合而算出的。 如果未提供数值表达式，此函数将使用为每个度量值指定的默认聚合运算符来聚合当前查询上下文中的每个度量值。 如果指定了数值表达式，此函数将先计算指定集中的每个单元的数值表达式，然后再求和。
```
  
Aggregate(Set_Expression [ ,Numeric_Expression ])  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
如果指定了一组空元组或一个空集，则此函数返回一个空值。
下表描述了 **Aggregate** 函数对不同聚合函数的行为方式。
Sum | 返回对集求得的值之和。  
---|---  
Count | 返回对集求得的值数。  
Max | 返回对集求得的最大值。  
Min | 返回对集求得的最小值。  
半累加性聚合函数 | 返回将形状投影到时间轴后，对集进行的半累加性计算。  
Distinct Count | 当切片器轴包括某个集时，构成子多维数据集的事实数据的聚合。 为集的每个成员返回非重复计数。 结果取决于正在聚合的单元的安全性而不是需要计算的单元的安全性。 集的单元安全性生成错误；低于指定集的粒度的单元安全性将被忽略。 对集进行计算会生成错误。 集粒度以下的计算将被忽略。 当集包含一个成员及其一个或多个子级时，对该集进行的非重复计数将返回跨越子成员事实数据范围的非重复计数。  
不能聚合的属性 | 返回值之和。  
混合式聚合函数 | 不支持这种聚合函数，将生成错误。  
一元运算符 | 不遵从；通过求和聚合值。  
计算度量值 | 设置求解次序以确保应用计算度量值。  
计算成员 | 应用一般规则，即最后一个求解次序优先。  
分配 | 分配根据度量值聚合函数聚合。 如果度量值聚合函数是非重复计数，则对分配求和。  
以下示例从 **Adventure Works** 多维数据集返回成员的总`Measures.[Order Quantity]`和，该成员在维度中包含的 `Date` 2003 日历年头八个月聚合。
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

下面的示例根据用 Aggregate 函数计算、用户选择的 State-Province 成员值，返回上一个时期销售额下滑的分销商的计数。 **Hierarchize** 和 **DrillDownLevel** 函数用于返回 Product 维度中产品类别销售额下降的值。
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

PeriodsToDate (MDX) Children (MDX) Hierarchize (MDX) Count（集）(MDX) Filter (MDX) AddCalculatedMembers (MDX) DrilldownLevel (MDX) Properties (MDX) PrevMember (MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


