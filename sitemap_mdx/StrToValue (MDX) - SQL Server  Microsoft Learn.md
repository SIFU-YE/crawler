#### 通过
# StrToValue (MDX)
返回多维表达式指定的数值， (MDX) 格式字符串。
```
  
StrToValue(MDX_Expression [,CONSTRAINED] )   

```

_MDX_Expression_ 直接或间接解析为单个单元的有效字符串表达式。
**StrToValue** 函数返回 MDX 表达式指定的数值。 **StrToValue** 函数通常与用户定义的函数一起使用，以将外部函数中的 MDX 表达式返回到可解析为单个单元格的 MDX 语句。
  * 如果使用 CONSTRAINED 标志，则 MDX 表达式只能包含一个标量值。 通过指定字符串，使用 CONSTRAINED 标志可降低发生注入攻击的风险。 如果提供的 MDX 表达式不能直接解析为标量值，则会出现下列出错信息：“违反了 STRTOVALUE 函数中 CONSTRAINED 标志所规定的限制。”
  * 当未使用 CONSTRAINED 标志时，指定的 MDX 表达式的复杂程度不受限制，只要该表达式可解析为能够返回单个单元的有效多维表达式 (MDX) 即可。


如果 MDX 表达式的结果以文本方式存储，并且您希望对返回值执行算术运算，那么将该结果作为数值返回将十分有用。
以下示例使用 **StrToValue** 函数将每辆自行车的重量作为值返回。
```
WITH MEMBER Measures.x AS   
StrToValue   
   ([Product].[Product].CurrentMember.Properties ('Weight')  
   ,CONSTRAINED  
   )  
SELECT Measures.x ON 0  
,[Product].[Product].[Product].Members ON 1  
FROM [Adventure Works]  
WHERE [Product].[Product Categories].[Bikes]  

```

1月27日 15时 - 1月27日 15时 


