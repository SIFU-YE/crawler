#### 通过
# TupleToStr (MDX)
返回一个多维表达式（MDX）格式的字符串，该字符串对应于指定的元组。
```
  
TupleToStr(Tuple_Expression)   

```

_Tuple_Expression_ 返回元组的有效多维表达式 (MDX)。
此函数用于将元组的字符串表示形式传输给外部函数进行分析。 返回的字符串括在大括号 {} 中，如果元组中明确定义了多个成员，则用逗号分隔。
以下示例返回字符串 （[Date].[Calendar Year].&[2001]，[Geography]。[Geography]。[Country].&&[美国]） ：
```
WITH MEMBER Measures.x AS TupleToStr   
   (   
      ([Date].[Calendar Year].&[2001]  
         , [Geography].[Geography].[Country].&[United States]  
      )  
   )     
SELECT Measures.x ON 0  
FROM [Adventure Works]  

```

下面的示例与上面的示例返回相同的字符串。
```
WITH SET s AS   
   {  
      ([Date].[Calendar Year].&[2001],  
         [Geography].[Geography].[Country].&[United States]  
      )   
   }  
MEMBER Measures.x AS TupleToStr ( s.Item(0) )  
SELECT Measures.x ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


