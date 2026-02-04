#### 通过
# Sum (MDX)
返回对指定集计算数值表达式求得的和。
```
  
Sum( Set_Expression [ , Numeric_Expression ] )  

```

_Set_Expression_ 有效的多维表达式 (MDX) 集表达式。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
如果指定了数值表达式，则对集计算指定数值表达式的值然后求和。 如果没有指定数值表达式，则在指定集成员的当前上下文中计算指定集然后求和。 如果将 SUM 函数应用于非数值表达式，则结果不确定。
计算一组数值的总和时，Analysis Services 将忽略空值。
下例将返回 2001 和 2002 日历年 Product.Category 属性层次结构的所有成员的 Reseller Sales Amount 之和。
```
WITH MEMBER Measures.x AS SUM  
   ( { [Date].[Calendar Year].&[2001]  
         , [Date].[Calendar Year].&[2002] }  
      , [Measures].[Reseller Sales Amount]  
    )  
SELECT Measures.x ON 0  
,[Product].[Category].Members ON 1  
FROM [Adventure Works]  

```

下例将返回截至 2002 年 7 月 20 日 7 月份的 Internet 销售运费之和。
```
WITH MEMBER Measures.x AS SUM   
   (  
      MTD([Date].[Calendar].[Date].[July 20, 2002])  
     , [Measures].[Internet Freight Cost]  
     )  
SELECT Measures.x ON 0  
FROM [Adventure Works]  

```

以下示例使用 WITH MEMBER 关键字和 **SUM** 函数在“度量值”维度中定义一个计算成员，该成员包含加拿大的“经销商销售额”度量值之和，并在 Geography 维度中美国 Country 属性层次结构的成员。
```
WITH MEMBER Measures.NorthAmerica AS SUM   
      (  
         {[Geography].[Country].&[Canada]  
            , [Geography].[Country].&[United States]}  
       ,[Measures].[Reseller Sales Amount]  
      )  
SELECT {[Measures].[NorthAmerica]} ON 0,  
[Product].[Category].members ON 1  
FROM [Adventure Works]  

```

通常， **SUM** 函数与 **CURRENTMEMBER** 函数或函数（如 **YTD** ）一起使用，这些函数返回的集因层次结构的当前成员而异。 例如，下面的查询返回所有日期（从日历年的开始到行轴上显示的日期）的 Internet Sales Amount 度量值的总和。
```
WITH MEMBER MEASURES.YTDSUM AS  
SUM(YTD(), [Measures].[Internet Sales Amount])  
SELECT {[Measures].[Internet Sales Amount], MEASURES.YTDSUM} ON 0,  
[Date].[Calendar].MEMBERS ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


