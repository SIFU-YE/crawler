#### 通过
# CurrentOrdinal (MDX)
返回迭代过程中集内的当前迭代数。
```
  
Set_Expression.CurrentOrdinal  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
循环访问集时，例如使用 Filter (MDX)  或 Generate (MDX)  函数， **CurrentOrdinal** 函数将返回迭代数。
下面的简单示例演示如何将 **CurrentOrdinal** 与 **Generate** 一起使用，以返回一个字符串，其中包含集合中每个项的名称及其在集中的位置：
```
WITH SET MySet AS [Customer].[Customer Geography].[Country].MEMBERS  
MEMBER MEASURES.CURRENTORDINALDEMO AS  
GENERATE(MySet, CSTR(MySet.CURRENTORDINAL) + ") " + MySet.CURRENT.ITEM(0).NAME, ", ")  
SELECT MEASURES.CURRENTORDINALDEMO ON 0  
FROM [Adventure Works]  

```

CurrentOrdinal 的实际用法仅限于非常复杂的计算。 以下示例返回集中唯一的产品数，在使用 **Filter** 函数之前使用 **Order** 函数对非空元组进行排序。 **CurrentOrdinal** 函数用于比较和消除关联。
```
WITH MEMBER [Measures].[PrdTies] AS Count  
   (Filter  
      (Order  
        (NonEmpty  
          ([Product].[Product].[Product].Members  
          , {[Measures].[Reseller Order Quantity]}  
          )  
       , [Measures].[Reseller Order Quantity]  
       , BDESC  
       ) AS OrdPrds  
    , NOT((OrdPrds.CurrentOrdinal < OrdPrds.Count   
       AND [Measures].[Reseller Order Quantity] =   
          ( [Measures].[Reseller Order Quantity]  
            , OrdPrds.Item  
               (OrdPrds.CurrentOrdinal  
               )  
            )  
         )  
         OR (OrdPrds.CurrentOrdinal > 1   
            AND [Measures].[Reseller Order Quantity] =   
               ([Measures].[Reseller Order Quantity]  
               , OrdPrds.Item  
                  (OrdPrds.CurrentOrdinal-2)  
                )  
             )  
          ))  
       )  
SELECT {[Measures].[PrdTies]} ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


