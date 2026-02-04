#### 通过
# Members（集）(MDX)
返回某个维度、级别或层次结构中的成员集。
```
  
Hierarchy expression syntax  
Hierarchy_Expression.Members  
  
Level expression Syntax  
Level_Expression.Members  

```

_Hierarchy_Expression_ 返回层次结构的有效多维表达式 (MDX)。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
如果指定了层次结构表达式， **则 Members (Set)** 函数返回指定层次结构中所有成员的集合，不包括计算成员。 若要获取层次结构上所有成员（计算的或其他方式）的集合，请使用 AllMembers (MDX)  函数
如果指定了级别表达式， **则 Members (Set)** 函数返回指定级别内所有成员的集合。
如果维度仅包含单个可见层次结构，由于在此情况下维度名称将解析为其唯一可见的层次结构，所以既可以通过维度名称也可以通过层次结构名称来引用该层次结构。 例如，因为 Measures.Members 解析为 Measures 维度中唯一的层次结构，所以 Measures.Members 是有效的 MDX 表达式。
下例返回 Adventure Works 多维数据集中“日历年”层次结构的所有成员的集。
```
SELECT   
   [Date].[Calendar].[Calendar Year].Members ON 0  
FROM  
   [Adventure Works]  
  

```

下面的示例将返回 `[Product].[Products].[Product Line]` 级别中每个成员在 2003 年的订单数量。 **Members** 函数返回一个代表级别中的所有成员的集。
```
SELECT   
   {Measures.[Order Quantity]} ON COLUMNS,  
   [Product].[Product Line].[Product Line].Members ON ROWS  
FROM  
   [Adventure Works]  
WHERE  
   {[Date].[Calendar Year].[Calendar Year].&[2003]}  

```

1月27日 15时 - 1月27日 15时 


