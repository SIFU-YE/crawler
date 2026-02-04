#### 通过
# VisualTotals (MDX)
返回通过动态计算指定集内子成员的合计而生成的集，可以选择在得到的结果集内为父成员名称应用某种模式。
```
  
VisualTotals(Set_Expression[,Pattern])  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_模式_ 集中父成员的有效字符串表达式，包含星号 (*) 作为父名称的替代字符。
指定的集表达式可以指定包含单个维度内任何级别成员（通常是具有祖先-后代关系的成员）的集。 **VisualTotals** 函数对指定集中子成员的值进行求和，并在计算结果总计时忽略不在集中的子成员。 直观地对以层次结构顺序排序的集计算总和。 如果集中成员的顺序违背了层次结构，则结果就不是直观合计了。 例如，VisualTotals (USA, WA, CA, Seattle) 不将 WA 返回为 Seattle，而返回 WA、CA 和 Seattle 的值，然后计算这些值的总和作为 USA 的直观合计，同时计算两次 Seattle 的销售额。
将 **VisualTotals** 函数应用于与度量值无关或低于度量值组粒度的维度成员将导致值被替换为 null。
_模式_ （可选）指定总计标签的格式。 _Pattern_ 需要星号 (*) 作为父成员的替换字符，字符串中文本的其余部分显示在与父名称串联的结果中。 若要显示星号，请使用两个星号 (**)。
下面的示例根据所指定的一个后代 - 7 月，返回 2001 日历年第三季度的直观合计。
```
SELECT VisualTotals  
   ({[Date].[Calendar].[Calendar Quarter].&[2001]&[3]  
      ,[Date].[Calendar].[Month].&[2001]&[7]}) ON 0  
FROM [Adventure Works]  

```

下面的示例返回 Product 维度中 Category 属性层次结构的 [All] 成员及其四个子级中的两个。 对 Internet Sales Amount 度量值的 [All] 成员返回的合计是仅针对 Accessories 和 Clothing 成员的合计。 另外，模式参数用于指定 [All Products] 列的标签。 
```
SELECT  
   VisualTotals  
   ({[Product].[Category].[All Products]  
      ,[Product].[Category].[Accessories]  
      ,[Product].[Category].[Clothing]}  
      , '* - Visual Total'  
   ) ON Columns  
, [Measures].[Internet Sales Amount] ON Rows  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


