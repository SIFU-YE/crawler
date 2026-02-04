#### 通过
# Order (MDX)
排列指定集的成员，可以选择保留或打乱原有的层次结构。
```
  
Numeric expression syntax  
Order(Set_Expression, Numeric_Expression   
[ , { ASC | DESC | BASC | BDESC } ] )  
  
String expression syntax  
Order(Set_Expression, String_Expression   
[ , { ASC | DESC | BASC | BDESC } ] )  
  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Numeric_Expression_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
_String_Expression_ 通常是单元坐标（返回以字符串表示的数字）的有效多维表达式 (MDX) 的有效字符串表达式。
**Order** 函数可以是使用 **ASC** 或 **DESC** 标志指定的分层 () ，也可以是使用 **BASC** 或 **BDESC** 标志指定的非层次结构 (;**B** 代表“中断层次结构”) 。 如果指定 **了 ASC** 或 **DESC** ， **则 Order** 函数首先根据成员在层次结构中的位置排列成员，然后对每个级别进行排序。 如果指定 **了 BASC** 或 **BDESC** ， **则 Order** 函数将排列集中的成员，而不考虑层次结构。 如果未指定标志， **则 ASC** 为默认值。
如果将 **Order** 函数用于一个集合，其中两个或多个层次结构交叉联接，并且使用 **DESC** 标志，则仅对集中最后一个层次结构的成员进行排序。 这与 Analysis Services 2000 不同，后者对集合中的所有层次结构进行排序。
以下示例从 **Adventure Works** 多维数据集返回“日期”维度上“日历”层次结构中所有日历季度的经销商订单数。 **Order** 函数为 ROWS 轴重新排序集。 **Order** 函数按由层次结构确定的降序对设置`[Reseller Order Count]`进行`[Calendar]`排序。
```
SELECT
  Measures.[Reseller Order Count] ON COLUMNS,
  Order(
    [Date].[Calendar].[Calendar Quarter].MEMBERS,
    Measures.[Reseller Order Count],
    DESC
  ) ON ROWS
FROM [Adventure Works]

```

请注意，在此示例中， **当 DESC** 标志更改为 **BDESC** 时，层次结构被破坏，并且返回日历季度列表而不考虑层次结构：
```
SELECT
  Measures.[Reseller Order Count] ON COLUMNS,
  Order (
    [Date].[Calendar].[Calendar Quarter].MEMBERS,
    Measures.[Reseller Order Count],
    BDESC
  ) ON ROWS
FROM [Adventure Works]

```

下例根据 Reseller Gross Profit（分销商毛利润），返回前五个销售产品子类别的分销商销售额度量值，而不管层次结构如何。 使用 **Order** 函数对结果进行排序后，**Subset** 函数用于仅返回集中的前 5 个元组。
```
SELECT Subset
  (
    Order
      (
        [Product].[Product Categories].[SubCategory].members,
        [Measures].[Reseller Gross Profit], 
        BDESC
      ), 0, 5
  ) ON 0
FROM [Adventure Works]

```

以下示例使用 **Rank** 函数根据“经销商销售额”度量值对 City 层次结构的成员进行排名，然后按排名顺序显示这些成员。 通过使用 **Order** 函数先对 City 层次结构的成员集进行排序，排序只需执行一次，然后进行线性扫描，然后再按排序顺序显示。
```
WITH   
SET OrderedCities AS Order  
   ([Geography].[City].[City].members  
   , [Measures].[Reseller Sales Amount], BDESC  
   )  
MEMBER [Measures].[City Rank] AS Rank  
   ([Geography].[City].CurrentMember, OrderedCities)  
SELECT {[Measures].[City Rank],[Measures].[Reseller Sales Amount]}  ON 0   
,Order  
   ([Geography].[City].[City].MEMBERS  
   ,[City Rank], ASC)  
    ON 1  
FROM [Adventure Works]  

```

以下示例在使用 **Filter** 函数之前，使用 **Order** 函数对非空元组进行排序，返回集中唯一的产品数。 **CurrentOrdinal** 函数用于比较和消除关联。
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
    , (OrdPrds.CurrentOrdinal < OrdPrds.Count   
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
          )  
       )  
SELECT {[Measures].[PrdTies]} ON 0  
FROM [Adventure Works]  

```

若要了解 **DESC** 标志如何处理元组集，请先考虑以下查询的结果：
```
  
SELECT  
{[Measures].[Tax Amount]} ON 0,  
ORDER(  
[Sales Territory].[Sales Territory].[Group].MEMBERS  
,[Measures].[Tax Amount], DESC)  
ON 1  
FROM [Adventure Works]  
  

```

在行轴上，您可以看到 Sales Territory Groups 已按 Tax Amount 的降序排序，如下所示：North America、Europe、Pacific、NA。 现在，了解如果我们将“销售区域组”与“产品子类别”集交叉联接，并按相同的方式应用 **Order** 函数，会发生什么情况，如下所示：
```
  
SELECT  
{[Measures].[Tax Amount]} ON 0,  
ORDER(  
[Sales Territory].[Sales Territory].[Group].MEMBERS  
*  
{[Product].[Product Categories].[subCategory].Members}  
,[Measures].[Tax Amount], DESC)  
ON 1  
FROM [Adventure Works]  
  

```

尽管 Product Subcategories 的集合已按层次结构顺序的降序进行排序，但 Sales Territory Groups 现在未排序并且以它们在层次结构上出现的顺序出现：Europe、NA、North America 和 Pacific。 其原因在于，仅对元组集合中最后一个层次结构 Product Subcategories 进行了排序。 若要重现 Analysis Services 2000 的行为，请使用一系列嵌套的 **Generate** 函数在交叉联接每个集之前对其进行排序，例如：
```
  
SELECT  
{[Measures].[Tax Amount]} ON 0,  
GENERATE(  
ORDER(  
[Sales Territory].[Sales Territory].[Group].MEMBERS  
,[Measures].[Tax Amount], DESC)  
,  
ORDER(  
[Sales Territory].[Sales Territory].CURRENTMEMBER  
*  
{[Product].[Product Categories].[subCategory].Members}  
,[Measures].[Tax Amount], DESC))  
ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


