#### 通过
# 一元运算符
在多维表达式 (MDX) 中，一元运算符对单个操作数执行操作，如返回数值表达式的负值或正值。
MDX 支持下表中列出的一维运算符。
返回数值表达式的负值。  
---  
返回数值表达式的正值。  
下面的示例显示了如何使用一维运算符返回度量值的负值：
```
WITH   
   MEMBER [Measures].[NegDiscountAmount] AS  
   -[Measures].[Discount Amount]  
SELECT   
   {[Measures].[Discount Amount],[Measures].[NegDiscountAmount]} on COLUMNS,  
   NON EMPTY [Product].[Product].MEMBERS  ON Rows  
FROM [Adventure Works]  
WHERE [Product].[Category].[Bikes]  

```

此外，MDX 使用特殊的一元运算符来确定 RollupChildren 函数执行的聚合操作。 有关这些特殊一元运算符的详细信息，请参阅 向维度添加自定义聚合。
1月27日 15时 - 1月27日 15时 


