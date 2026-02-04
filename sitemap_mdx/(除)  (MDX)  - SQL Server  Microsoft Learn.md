#### 通过
# 除法 - MDX 运算符参考
执行算术运算，将一个数除以另一个数。
```
  
Dividend / Divisor  

```

_股利_ 返回数值的有效多维表达式 (MDX) 表达式。
_因子_ 返回数值的有效 MDX 表达式。
具有与优先级较高的参数相同的数据类型的值。
**/ (除法)** 运算符返回的实际值表示第一个表达式除以第二个表达式的商。
两个表达式必须具有相同的数据类型，或者其中一个表达式必须能够隐式转换为另一个表达式的数据类型。 如果 _Divisor_ 的计算结果为 null 值，运算符将引发错误。 如果 _Divisor_ 和 _Dividend_ 的计算结果均为 null 值，运算符将返回 null 值。
下面的示例演示了此运算符的用法。
```
-- This query returns the freight cost per user,  
-- for products, averaged by month.   
With Member [Measures].[Freight Per Customer] as  
    [Measures].[Internet Freight Cost]  
    /   
    [Measures].[Customer Count]  
  
SELECT   
    [Ship Date].[Calendar].[Calendar Year] Members ON 0,  
    [Product].[Category].[Category].Members ON 1  
FROM  
    [Adventure Works]  
WHERE  
    ([Measures].[Freight Per Customer])  

```

非零或非 null 值除以零或 null 将返回无穷大值，该值在查询结果中显示为“1.#INF”值。 在大多数情况下，应检查是否被零除，以避免出现这种情况。 以下示例说明具体情况：
```
//Returns 1.#INF when Internet Sales Amount is zero or null  
Member [Measures].[Reseller to Internet Ratio] AS  
[Measures].[Reseller Sales Amount]  
/  
[Measures].[Internet Sales Amount]  
//Traps the division by zero scenario and returns null instead of 1.#INF  
Member [Measures].[Reseller to Internet Ratio With Error Handling] AS  
IIF([Measures].[Internet Sales Amount]=0, NULL,  
[Measures].[Reseller Sales Amount]  
/  
[Measures].[Internet Sales Amount])  
SELECT  
{[Measures].[Reseller to Internet Ratio],[Measures].[Reseller to Internet Ratio With Error Handling]} ON 0,  
[Product].[Category].[Category].Members ON 1  
FROM  
[Adventure Works]  
WHERE([Date].[Calendar].[Calendar Year].&[2001])  

```

1月27日 15时 - 1月27日 15时 


