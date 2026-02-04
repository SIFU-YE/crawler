#### 通过
# SetToStr (MDX)
返回多维表达式 (MDX) 格式的字符串，它对应于指定的集合。
```
  
SetToStr(Set_Expression)  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
该函数用于将某集的字符串表示形式传输到外部函数，以进行分析。 返回的字符串括在大括号 {}中，集中的每个项用逗号分隔。
下面的示例将返回包含 Geography.Country 属性层次结构的所有成员的字符串。
```
WITH MEMBER Measures.x AS SetToStr (Geography.Geography.Children)  
SELECT Measures.x ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


