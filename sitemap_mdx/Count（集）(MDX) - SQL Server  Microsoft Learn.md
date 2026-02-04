#### 通过
# Count（集）(MDX)
返回集中的单元数。
```
  
Standard syntax  
Count(Set_Expression [ , ( EXCLUDEEMPTY | INCLUDEEMPTY ) ] )  
  
Alternate syntax  
Set_Expression.Count  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
**Count (Set)** 函数包含或排除空单元格，具体取决于所使用的语法。 如果使用标准语法，则可以分别使用 **EXCLUDEEMPTY** 或 **INCLUDEEMPTY** 标志来排除或包含空单元格。 如果使用备用语法，则函数始终包括空单元。
若要排除集计数中的空单元格，请使用标准语法和可选的 **EXCLUDEEMPTY** 标志。
**默认情况下，Count (Set)** 函数对空单元格进行计数。 相反，OLE DB 中对集进行计数的 **Count** 函数默认排除空单元格。
下例统计成员集中单元的数目，该成员集由“产品”维度中“型号名称”属性层次结构的子级构成。
```
WITH MEMBER measures.X AS  
   [Product].[Model Name].children.count   
SELECT Measures.X ON 0  
FROM [Adventure Works]  

```

以下示例通过将 **DrilldownLevel** 函数与 **Count** 函数结合使用来计算 Product 维度中的产品数。
```
Count(DrilldownLevel (   
   [Product].[Product].[Product]))  

```

以下示例通过将 **Count** 函数与 **Filter** 函数和许多其他函数结合使用，返回与上一日历季度相比销售额下降的经销商。 此查询使用 **Aggregate** 函数来支持选择多个地域成员，例如从客户端应用程序的下拉列表中选择。
```
WITH MEMBER Measures.[Declining Reseller Sales] AS  
   Count  
   (Filter  
      (Existing(Reseller.Reseller.Reseller),  
         [Measures].[Reseller Sales Amount]   
         < ([Measures].[Reseller Sales Amount],  
            [Date].Calendar.PrevMember)  
      )  
   )  
MEMBER [Geography].[State-Province].x AS   
   Aggregate  
   ( {[Geography].[State-Province].&[WA]&[US],   
      [Geography].[State-Province].&[OR]&[US] }   
   )  
SELECT NON EMPTY HIERARCHIZE   
   (AddCalculatedMembers   
      ({DrillDownLevel  
         ({[Product].[All Products]})  
      })  
   ) DIMENSION PROPERTIES PARENT_UNIQUE_NAME ON COLUMNS   
FROM [Adventure Works]  
WHERE ([Geography].[State-Province].x,  
   [Date].[Calendar].[Calendar Quarter].&[2003]&[4]  
   ,[Measures].[Declining Reseller Sales])  
  

```

Count（维度）(MDX) Count（层次结构级别）(MDX) Count（元组）(MDX) DrilldownLevel (MDX) AddCalculatedMembers (MDX) Hierarchize (MDX) Properties (MDX) Aggregate (MDX) Filter (MDX) PrevMember (MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


