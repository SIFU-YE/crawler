#### 通过
# Members（字符串）(MDX)
返回字符串表达式所指定的成员。
```
  
Members(Member_Name)   

```

_Member_Name_ 指定成员名称的有效字符串表达式。
**Members (String)** 函数返回指定名称的单个成员。 通常，将 **Members (String)** 函数与外部函数结合使用，向 **Members (String) 函数** 提供一个标识成员的字符串，而 **Members (String)** 函数返回此指定成员的值。
以下示例使用 **Members (String)** 函数将指定的字符串转换为有效成员，然后返回字符串中指定的成员的默认度量值。 指定的字符串用单引号引起来。 默认度量值为 Reseller Sales Amount 度量值。
```
SELECT Members ('[Geography].[Geography].[Country].&[United States] ') ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


