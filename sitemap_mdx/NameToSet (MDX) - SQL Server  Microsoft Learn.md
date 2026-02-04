#### 通过
# NameToSet (MDX)
返回一个集，该集包含多维表达式 (MDX) 格式字符串指定的成员。
```
  
NameToSet(Member_Name)   

```

_Member_Name_ 代表成员名称的有效字符串表达式。
如果指定的成员名称存在， **则 NameToSet** 函数将返回包含该成员的集。 否则，此函数返回空集。
指定的成员名称只能是成员名称，不能是成员表达式。 若要使用成员表达式，请参阅 StrToSet (MDX) 。
下例返回指定成员名称的默认度量值。
```
SELECT NameToSet('[Date].[Calendar].[July 2001]') ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


