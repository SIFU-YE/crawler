#### 通过
# Hierarchize (MDX)
对层次结构中的某个集的成员进行排序。
```
  
Hierarchize(Set_Expression [ , POST ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
**Hierarchize** 函数按层次结构顺序组织指定集的成员。 此函数始终保留重复项。
  * 如果未指定 **POST** ，该函数将按其自然顺序对某个级别的成员进行排序。 如果未指定其他排序条件，则成员的自然顺序就是它们在层次结构中的默认排序顺序。 子成员会紧跟在它们的父成员之后。
  * 如果指定了 **POST** ， **则 Hierarchize** 函数使用后自然顺序对某个级别中的成员进行排序。 也就是说，子成员优先于他们的父级。


下例浅化了 Canada 成员。 **Hierarchize** 函数用于按分层顺序组织指定的集成员，这是 **DrillUpMember** 函数所需的。
```
SELECT DrillUpMember   
   (  
      Hierarchize  
         (  
            {[Geography].[Geography].[Country].[Canada]  
            ,[Geography].[Geography].[Country].[United States]  
            ,[Geography].[Geography].[State-Province].[Alberta]  
            ,[Geography].[Geography].[State-Province].[Brunswick]  
            ,[Geography].[Geography].[State-Province].[Colorado]   
            }  
         ), {[Geography].[Geography].[Country].[United States]}  
   )  
ON 0  
FROM [Adventure Works]  

```

以下示例从 **Adventure Works** 多维数据集返回成员的总`Measures.[Order Quantity]`和，该成员在维度中包含的 `Date` 2003 年头 9 个月聚合。 **PeriodsToDate** 函数定义由 Aggregate 函数操作的集中的元组。 **Hierarchize** 函数按层次结构顺序组织 Product 维度中指定成员集的成员。
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


