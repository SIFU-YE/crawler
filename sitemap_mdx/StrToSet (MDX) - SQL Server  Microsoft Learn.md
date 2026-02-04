#### 通过
# StrToSet (MDX)
返回多维表达式指定的集， (MDX) 格式字符串。
```
  
StrToSet(Set_Specification [,CONSTRAINED] )   

```

_Set_Specification_ 直接或间接指定某个集的有效字符串表达式。
**StrToSet** 函数返回字符串表达式中指定的集。 **StrToSet** 函数通常与用户定义的函数一起使用，以便将集合规范从外部函数返回给 MDX 语句，或者在 MDX 查询参数化时返回。
  * 使用 CONSTRAINED 标志时，集规范必须包含限定或非限定成员名称，或者包含由大括号 括起来的限定或非限定成员名称的 {}元组集。 此标志通过指定字符串可降低注入攻击的风险。 如果提供的字符串不能直接解析为限定或非限定的成员名称，则会出现下列出错信息：“违反了 STRTOSET 函数中 CONSTRAINED 标志所规定的限制。”
  * 如果未使用 CONSTRAINED 标志，则指定的集规范可以解析为返回一个集的有效多维表达式 (MDX)。
  * 为了更好地理解集和成员之间的差异，请参阅“使用集表达式”和“使用成员表达式”。


下面的示例使用 **StrToSet** 函数返回State-Province属性层次结构的成员集。 该集规范提供一个有效的 MDX 集表达式。
```
SELECT StrToSet ('[Geography].[State-Province].Members')  
ON 0  
FROM [Adventure Works]  
  

```

下面的示例返回因 CONSTRAINED 标志而引起的错误。 如果集规范提供一个有效的 MDX 集表达式，则 CONSTRAINED 标志在集规范中需要限定或非限定的成员名称。
```
SELECT StrToSet ('[Geography].[State-Province].Members', CONSTRAINED)  
ON 0  
FROM [Adventure Works]  
  

```

以下示例返回德国和加拿大的“经销商销售额”度量值。 指定字符串中提供的集规范包含了 CONSTRAINED 标志所需的限定成员名称。
```
SELECT StrToSet ('{[Geography].[Geography].[Country].[Germany],[Geography].[Geography].[Country].[Canada]}', CONSTRAINED)  
ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


