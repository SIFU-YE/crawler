#### 通过
# StrToMember (MDX)
返回由多维表达式指定的成员， (MDX) 格式字符串。
```
  
StrToMember(Member_Name [,CONSTRAINED] )   

```

_Member_Name_ 直接或间接指定成员的有效字符串表达式。
**StrToMember** 函数返回字符串表达式中指定的成员。 **StrToMember** 函数通常与用户定义的函数一起使用，以便将成员规范从外部函数返回给 MDX 语句，或者在 MDX 查询参数化时返回。
  * 如果使用 CONSTRAINED 标志，则成员名称必须可直接解析为限定或未限定的成员名称。 此标志通过指定字符串可降低注入攻击的风险。 如果所提供的字符串无法直接解析为限定或未限定的成员名称，将出现以下错误：“违反了 STRTOMEMBER 函数中 CONSTRAINED 标志所规定的限制。”
  * 如果未使用 CONSTRAINED 标志，指定的成员将能直接解析为成员名称，或解析为 MDX 表达式以解析为名称。
  * 为了更好地理解集和成员之间的差异，请参阅“使用集表达式”和“使用成员表达式”。


以下示例使用 **StrToMember** 函数返回 State-Province 属性层次结构中拜仁成员的经销商销售额度量值。 指定字符串提供了限定的成员名称。
```
SELECT {StrToMember ('[Geography].[State-Province].[Bayern]')}  
ON 0,  
{[Measures].[Reseller Sales Amount]} ON 1  
FROM [Adventure Works]  
  

```

以下示例使用 **StrToMember** 函数返回拜仁成员的经销商销售额度量值。 由于成员名称字符串仅提供了一个未限定的成员名称，因此该查询返回指定成员的第一个实例，而指定成员恰好在 Customer 维度（不与 Reseller Sales 相交）的 Customer Geography 层次结构中。 最佳做法要求指定限定名称以确保获得预期的结果。
```
SELECT {StrToMember ('[Bayern]').Parent}  
ON 0,  
{[Measures].[Reseller Sales Amount]} ON 1  
FROM [Adventure Works]  
  

```

以下示例使用 **StrToMember** 函数返回 State-Province 属性层次结构中拜仁成员的经销商销售额度量值。 所提供的成员名称字符串解析为限定的成员名称。
```
SELECT {StrToMember('[Geography].[Geography].[Country].[Germany].FirstChild', CONSTRAINED)}  
ON 0,  
{[Measures].[Reseller Sales Amount]} ON 1  
FROM [Adventure Works]  
  

```

下面的示例返回因 CONSTRAINED 标志而引起的错误。 虽然所提供的成员名称字符串包含一个可解析为限定的成员名称的有效 MDX 成员表达式，但是 CONSTRAINED 标志要求成员名称字符串包含限定或未限定的成员名称。
```
SELECT StrToMember ('[Geography].[Geography].[Country].[Germany].FirstChild', CONSTRAINED)  
ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


