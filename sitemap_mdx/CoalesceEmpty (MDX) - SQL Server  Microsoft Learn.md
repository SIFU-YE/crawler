#### 通过
# CoalesceEmpty (MDX)
将空单元值转换为指定的非空单元值，该值可以是数字或字符串。
```
  
Numeric syntax  
CoalesceEmpty( Numeric_Expression1 [ ,Numeric_Expression2,...n] )  
  
String syntax  
CoalesceEmpty(String_Expression1 [ ,String_Expression2,...n] )  

```

_Numeric_Expression1_ 返回数字的有效数值表达式，通常为单元坐标的多维表达式 (MDX)。
_Numeric_Expression2_ 有效数值表达式，通常为指定的数值。
_String_Expression1_ 有效字符串表达式，通常为返回字符串的单元坐标的多维表达式 (MDX)。
_String_Expression2_ 有效字符串表达式，通常为指定的字符串值（该值被第一个字符串表达式返回的 NULL 代替）。
如果指定了一个或多个数值表达式， **CoalesceEmpty** 函数将从左到右返回第一个数值表达式 (的数值，) 可解析为非空值。 如果指定的所有数值表达式都不能被解析为非空值，则此函数返回空单元值。 通常情况下，第二个数值表达式的值是被第一个数值表达式返回的 NULL 代替的数值。
如果指定了一个或多个字符串表达式，此函数将返回可被解析为非空值的第一个（从左向右）字符串表达式的值。 如果指定的所有字符串表达式都不能被解析为非空值，则此函数返回空单元值。 通常情况下，第二个字符串表达式的值是被第一个字符串表达式返回的 NULL 代替的字符串值。
**CoalesceEmpty** 函数只能采用相同类型的值。 也就是说，指定的所有值表达式的值都必须为数值数据类型或空单元值，或者，指定的所有值表达式的值都必须为字符串数据类型或空单元值。 对此函数的一次调用不能同时包括数值表达式和字符串表达式。
有关空单元的详细信息，请参阅 OLE DB 文档。
以下示例查询 **Adventure Works** 多维数据集。 此示例将返回每个产品的订单数量以及按类别排列的订单数量百分比。 **CoalesceEmpty** 函数确保在格式化计算成员时，null 值表示为零 (0) 。
```
WITH   
   MEMBER [Measures].[Order Percent by Category] AS  
   CoalesceEmpty(   
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


