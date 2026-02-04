#### 通过
# MemberToStr (MDX)
返回一个多维表达式（MDX）格式的字符串，该字符串对应于指定的成员。
```
  
MemberToStr(Member_Expression)   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
此函数返回包含成员的唯一名称的字符串。 它通常用于将成员的唯一名称传递给外部函数。
以下示例返回字符串 [Geography]。[Geography]。[Country].&&[美国] ：
```
WITH MEMBER Measures.x AS MemberToStr  
([Geography].[Geography].[Country].[United States])  
SELECT Measures.x ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


