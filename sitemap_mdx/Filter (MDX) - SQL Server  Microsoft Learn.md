#### 通过
# Filter (MDX)
返回根据搜索条件对指定集进行筛选后得到的集。
```
  
Filter(Set_Expression, Logical_Expression )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Logical_Expression_ 计算结果为 True 或 False 的有效多维表达式 (MDX) 逻辑表达式。
**Filter** 函数针对指定集中的每个元组计算指定的逻辑表达式。 函数返回一个集，该集由指定集中的每个元组组成，其中逻辑表达式的计算结果为 **true** 。 如果没有元组的计算结果为 **true** ，则返回空集。
**Filter** 函数的工作方式类似于 IIf 函数。 **IIf** 函数仅根据 MDX 逻辑表达式的计算返回两个选项之一，而 **Filter** 函数返回一组满足指定搜索条件的元组。 实际上， **Filter** 函数对集中的每个元组执行 `IIf(Logical_Expression, Set_Expression.Current, NULL)` ，并返回生成的集。
以下示例说明 Filter 函数在查询的行轴上的用法，以便仅返回 Internet Sales Amount 大于 $10000 的 Date：
```
SELECT [Measures].[Internet Sales Amount] ON 0,  
FILTER(  
[Date].[Date].[Date].MEMBERS  
,  [Measures].[Internet Sales Amount]>10000)  
ON 1  
FROM  
[Adventure Works]  

```

Filter function 函数还可以在计算成员定义内部使用。 以下示例从 **Adventure Works** 多维数据集返回在维度中包含的 `Date` 2003 年前 9 个月内聚合的成员之和`Measures.[Order Quantity]`。 **PeriodsToDate** 函数定义 **Aggregate** 函数在其上运行的集中元组。 **Filter** 函数将返回的元组限制为上一个时间段的“经销商销售金额”度量值较低的元组。
```
WITH MEMBER Measures.[Declining Reseller Sales] AS Count  
   (Filter  
      (Existing  
         (Reseller.Reseller.Reseller),   
            [Measures].[Reseller Sales Amount] <   
               ([Measures].[Reseller Sales Amount],[Date].Calendar.PrevMember)  
        )  
    )  
MEMBER [Geography].[State-Province].x AS Aggregate   
( {[Geography].[State-Province].&[WA]&[US],   
   [Geography].[State-Province].&[OR]&[US] }   
)  
SELECT NON EMPTY HIERARCHIZE   
   (AddCalculatedMembers   
      ({DrillDownLevel  
         ({[Product].[All Products]})}  
        )  
    ) DIMENSION PROPERTIES PARENT_UNIQUE_NAME ON COLUMNS   
FROM [Adventure Works]  
WHERE ([Geography].[State-Province].x,   
   [Date].[Calendar].[Calendar Quarter].&[2003]&[4],  
   [Measures].[Declining Reseller Sales])  

```

1月27日 15时 - 1月27日 15时 


