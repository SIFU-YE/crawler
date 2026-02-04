#### 通过
# CASE 语句 (MDX)
允许您有条件地从多次比较中返回特定值。 有两种类型的 Case 语句：
  * 简单 Case 语句将某个表达式与一组简单表达式进行比较，以返回特定的值。
  * 搜索 Case 语句计算一组布尔表达式，以返回特定的值。

```
  
Simple Case Statement  
CASE [input_expression]  
WHEN when_expression THEN when_true_result_expression  
[...n]  
[ELSE else_result_expression]  
END  
  
Search Case Statement  
CASE   
WHEN Boolean_expression THEN when_true_result_expression  
[...n]  
[ELSE else_result_expression]  
END  

```

input_expression 解析为标量值的多维表达式 (MDX)。
_when_expression_ 计算 _input_expression_ 所针对的指定标量值，当计算结果为 true 时，返回 _else_result_expression_ 的标量值。
_when_true_result_expression_ 当 WHEN 子句计算结果为 True 时返回的标量值。
_else_result_expression_ 当没有任何 WHEN 子句的计算结果为 True 时返回的标量值。
_Boolean_expression_ 计算结果为标量值的 MDX 表达式。
如果没有 ELSE 子句，而且所有 WHEN 子句的计算结果都为 False，则结果是空单元。
## 简单 Case 表达式
MDX 通过将 _input_expression_ 解析为标量值来计算简单的 case 表达式。 然后将此标量值与 _when_expression_ 的标量值进行比较。 如果两个标量值匹配，则 CASE 语句返回 _when_true_expression_ 的值。 如果这两个标量值不匹配，则计算下一个 WHEN 子句。 如果所有 WHEN 子句的计算结果为 false，则返回 ELSE 子句 _中else_result_expression_ 的值（如果有）。
在下例中，对几个 WHEN 子句计算 Reseller Order Count 度量值，并且基于每年的 Reseller Order Count 度量值的值返回一个结果。 对于与 WHEN 子句when_expression中指定的标量值不匹配的 Reseller Order Count 值 _else_result_expression_ 的标量值。
```
WITH MEMBER [Measures].x AS   
CASE [Measures].[Reseller Order Count]  
   WHEN 0 THEN 'NONE'  
   WHEN 1 THEN 'SMALL'  
   WHEN 2 THEN 'SMALL'  
   WHEN 3 THEN 'MEDIUM'  
   WHEN 4 THEN 'MEDIUM'  
   WHEN 5 THEN 'LARGE'  
   WHEN 6 THEN 'LARGE'  
      ELSE 'VERY LARGE'  
END  
SELECT Calendar.[Calendar Year] on 0  
, NON EMPTY [Geography].[Postal Code].Members ON 1  
FROM [Adventure Works]  
WHERE [Measures].x  

```

## Case 搜索表达式
若要使用 Case 表达式执行更为复杂的计算，请使用 Case 搜索表达式。 使用此搜索表达式的变体可以计算输入表达式是否位于一个值范围内。 MDX 按 WHEN 子句出现在 CASE 语句中的顺序计算这些子句。
在以下示例中，针对多个 WHEN 子句中的每个子句，根据指定的 _Boolean_expression_ 计算经销商订单计数度量值。 根据每年的 Reseller Order Count 度量值的值返回一个结果。 因为按照 WHEN 子句出现的顺序计算这些子句，所以可简单地将所有大于 6 的值赋值为“VERY LARGE”，而无需显式地指定每个值。 对于未在 WHEN 子句中指定的 Reseller Order Count 值，返回 _else_result_expression_ 的标量值。
```
WITH MEMBER [Measures].x AS   
CASE   
   WHEN [Measures].[Reseller Order Count] > 6 THEN 'VERY LARGE'  
   WHEN [Measures].[Reseller Order Count] > 4 THEN 'LARGE'  
   WHEN [Measures].[Reseller Order Count] > 2 THEN 'MEDIUM'  
   WHEN [Measures].[Reseller Order Count] > 0 THEN 'SMALL'  
   ELSE "NONE"  
END  
SELECT Calendar.[Calendar Year] on 0,  
NON EMPTY [Geography].[Postal Code].Members on 1  
FROM [Adventure Works]  
WHERE [Measures].x  

```

1月27日 15时 - 1月27日 15时 


