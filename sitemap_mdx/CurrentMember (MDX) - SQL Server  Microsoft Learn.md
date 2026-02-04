#### 通过
# CurrentMember (MDX)
在遍历过程中返回当前成员以及指定层次结构。
```
  
Hierarchy_Expression.CurrentMember  

```

_Hierarchy_Expression_ 返回层次结构的有效多维表达式 (MDX)。
遍历一组层次结构成员时，在遍历过程的每一步，所操作的成员就是当前成员。 **CurrentMember** 函数返回该成员。
如果维度只包含一个可见的层次结构，则可以通过此维度的名称或此层次结构的名称引用此层次结构，原因是此维度的名称会解析为它唯一可见的层次结构。 例如，`Measures.CurrentMember` 是一个有效的 MDX 表达式，这是因为它会解析为 Measures 维度中唯一的层次结构。
以下查询演示如何使用 **Currentmember** 从列、行和切片轴上的层次结构中查找当前成员：
```
WITH
  MEMBER MEASURES.CURRENTDATE AS [Date].[Calendar].CURRENTMEMBER.NAME
  MEMBER MEASURES.CURRENTPRODUCT AS [Product].[Product Categories].CURRENTMEMBER.NAME
  MEMBER MEASURES.CURRENTMEASURE AS MEASURES.CURRENTMEMBER.NAME
  MEMBER MEASURES.CURRENTCUSTOMER AS [Customer].[Customer Geography].CURRENTMEMBER.NAME
SELECT
 [Product].[Product Categories].[Category].MEMBERS *
 {MEASURES.CURRENTDATE,
    MEASURES.CURRENTPRODUCT,
    MEASURES.CURRENTMEASURE,
    MEASURES.CURRENTCUSTOMER} ON 0, 
 [Date].[Calendar].MEMBERS ON 1  
FROM [Adventure Works]
WHERE ([Customer].[Customer Geography].[Country].&[Australia])

```

当前成员在查询中的轴上使用的层次结构上进行更改。 因此，在轴上使用的相同维度上其他层次结构上的当前成员也可能更改：此行为称为“自动存在”，可以在 MDX (Analysis Services) 中的关键概念 中找到更多详细信息。 例如，下面的查询说明当 Calendar 层次结构上的当前成员显示在行轴上时，Date 维度的 Calendar Year 层次结构上的当前成员如何随 Calendar 层次结构上的当前成员更改：
```
WITH
  MEMBER MEASURES.CURRENTYEAR AS [Date].[Calendar Year].CURRENTMEMBER.NAME
SELECT
 {MEASURES.CURRENTYEAR} ON 0,
 [Date].[Calendar].MEMBERS ON 1  
FROM [Adventure Works]

```

**CurrentMember** 对于使计算了解所使用的查询的上下文非常重要。 以下示例从 **Adventure Works** 多维数据集返回每个产品的订单数量以及按类别和型号划分的订单数量百分比。 **CurrentMember** 函数标识在计算过程中要使用的订单数量的产品。
```
WITH   
   MEMBER [Measures].[Order Percent by Category] AS  
   CoalesceEmpty  
(   
      ([Product].[Product Categories].CurrentMember,  
        Measures.[Order Quantity]) /   
          (  
           Ancestor  
           ( [Product].[Product Categories].CurrentMember,   
             [Product].[Product Categories].[Category]  
           ), Measures.[Order Quantity]  
       ), 0  
   ), FORMAT_STRING='Percent'  
SELECT   
   {Measures.[Order Quantity],  
      [Measures].[Order Percent by Category]} ON COLUMNS,  
{[Product].[Product].Members} ON ROWS  
FROM [Adventure Works]  
WHERE {[Date].[Calendar Year].[Calendar Year].&[2003]}  

```

1月27日 15时 - 1月27日 15时 


